# Week 1: Discovering a Robot Through ROS 2

## Student

- Name: Elion Prelvukaj
- Email: elion.prelvukaj38@login.cuny.edu

## final.architecture_evidence

The node is reactive because every command comes straight from the current sensor reading, with no stored state, no memory of past scans, and no larger goal being pursued. Making it hybrid would mean adding a deliberative layer on top that holds a map or destination and plans a route, handing off only the moment-to-moment obstacle avoidance to this reflex loop.

## final.course_reflection

This made me understand how technical and difficult robotics really is. As a computer science student I'm usually not overwhelmed by a new topic, but this one stumped me more than I expected. I can see myself getting more interested in robotics as a hobby, and I have a lot more respect for people who do it professionally.
I think there's real value in this field, especially around accessibility. We can help people in ways technology never allowed before, and it seems important to use that and reach as many people as possible. Maybe working in an environment I had no experience with is what threw me off, but I'd like to see how this work gets done at a professional level.

## final.hardware_next

I'd test the edge cases the simulator rarely produces: scans that stop arriving or show up late mid-motion, distances sitting right at the threshold where an off-by-one would flip the decision, and readings that look valid but are wildly wrong inside the front sector. I'd also confirm the guard actually intercepts an unsafe command end to end on real hardware, since latency and dropped messages behave very differently outside simulation.

## final.middleware_debugging

The ROS graph shows who publishes and subscribes to each topic, so you can walk the pipeline one node at a time and check whether your node is actually publishing, whether the guard is subscribed to that same topic name, and whether the types match, since a mismatched name or message type is a classic silent failure. Using ros2 topic echo and ros2 node info at each link isolates exactly where the message stops flowing instead of guessing across the whole system.

## final.system_synthesis

Robotics software is difficult because it sits between unreliable physical sensing and real-world consequences. A LiDAR scan can return infinite or missing values because of reflective surfaces, sensor noise, or timing gaps. In a normal application bad input produces a wrong number on screen. Here it drives a robot into a wall. Robotics systems are also concurrent, so sensors, decision logic, and actuators run asynchronously and have to agree on timing, units, and what counts as failure. Even setting up the environment took real time. Gazebo would not start under the old gazebo command. None of that is robotics, but it was still delaying the process. The architecture I implemented is a linear decision pipeline. A perception step (front_distance) filters the raw range array down to the nearest valid reading in front of the robot, and a decision step (decide_velocity) turns that distance into a bounded forward speed. Keeping both as pure functions independent of ROS made them testable without a running simulation. ROS 2 middleware connected four components through three publish/subscribe relationships. The simulator publishes laser data on /scan. My node subscribes to it and publishes a Twist on /student_cmd_vel. The course guard subscribes there, checks the command against its limits, and republishes on /cmd_vel, which the ROS-Gazebo bridge converts for the simulator. No component needs to know the others' internals. Timing and invalid data affect safety because a stale measurement looks exactly like an empty room. If front_distance returns None and decide_velocity did not default to stopping, the robot would treat "I don't know" as "it's clear." The guard is the layer best positioned to restrict unsafe motion. It sits between the decision logic and the motors, independent of the higher-level reasoning, so even if a bug slips through the decision function it can clamp or reject the command before it reaches hardware.

## final.timing_evidence

The distance is None case was the clearest one, since a single missing or invalid LiDAR reading, if left unhandled, would silently be treated as "path clear." That taught me safety-critical code has to treat missing information as a hazard by default, because a false "clear" costs far more than an unnecessary stop

## mission_1.command_path_explanation

student_cmd_vel carries your node's proposed velocity, which a guard node checks against scan before republishing it on cmd_vel. That split means the safety filter can't be bypassed by a bug in your control code, since the base controller only ever listens to cmd_vel.

## mission_1.graph_explanation

A ROS2 shows the live components running in the software. Nodes such as rivz2 being a support tool for the person, and topics such as odom running an estimate of its position, direction, and movement.

## mission_1.guided_checks

{'bridge_info': True, 'command_topics': True, 'guard_info': True, 'node_list': True, 'scan_info': True, 'scan_message': True}

## mission_1.scan_observation

I noticed some infinities in the message. Could indicate the open space in the model.

## mission_1.tools_explanation

Gazebo is responsible for creating the world and the data, while RViz is responsible for showing you what the robot believes about that data.

## mission_2.measurement_explanation

For the right hand curve test, the robot curved way more to the right than I anticipated. I also did not expect the robot to be facing fully to the right at the end of the test.

## mission_2.modified_settings

{'linear_x': 0.12, 'angular_z': 0.6, 'duration': 4.0}

## mission_2.motion_comparison

The measured motion was actually less than my prediction, 0.389 to my 0.5. Also a little extra bit of delay with it being 3.05 seconds instead of being a little less than 3.

## mission_2.prediction_locks

{'curve': '2026-09-10T18:11:40.271262+00:00', 'curve_modified': '2026-09-10T18:30:08.972271+00:00', 'rotation': '2026-09-10T17:59:46.483647+00:00', 'straight': '2026-09-10T17:33:02.789140+00:00'}

## mission_2.predictions

{'curve': 'I predict it will move close to .60 meters forward along the curve and it will turn to the right about 1.6 radians.', 'curve_modified': 'The curve will be more tighter. Perhaps it will result in a Shape.', 'rotation': 'I predict the robot will do 1 and a half rotation, and will end up facing northwest.', 'straight': 'I predict the robot will be about half a meter from where it started.'}

## mission_2.safety_explanation

The command guard checks every proposed velocity before it reaches the base controller, clamping anything above the speed limit and rejecting malformed values like NaN or inf.
The final zero command is the deliberate end of a trial, explicitly telling the robot to stop rather than leaving it holding the last velocity it received. 
The timeout is needed if your program never gets there, because it crashed, was killed, or lost communication mid-motion. The guard runs as a separate process, so it can notice the silence and publish a stop after 0.5 seconds on its own.

## mission_3.data_to_command

front_distance scans the LiDAR range list, keeps only readings that are both finite and positive and within the front window, and returns the closest one. decide_velocity then takes that distance and turns it into a command: None or too close, (≤ stop_distance) yields 0.0 (stop), otherwise it returns forward_speed between 0.0 and 0.18 m/s.



## mission_3.missing_data_safety

Because no valid measurement could just mean the sensor failed, returned noise, or the obstacle is at an odd angle to register a finite reading, so treating it as clear would be a dangerous assumption. Stopping is the safe default when you lack information, since wrongly stopping is far more safe than wrongly moving into something you couldn't see.

## mission_3.system_layers

The ROS node subscribes to the LiDAR scan topic, calls your front_distance to extract the nearest front reading, then passes that to decide_velocity to get a bounded speed, and publishes that as the robot's velocity command. The command guard sits between that output and the actual motors as a final safety check, so even if your decision logic had a bug, the guard can still catch an unsafe command.

## part_1.activity

{'sensor': {'normal': True, 'changed': True}, 'timing': {'normal': True, 'changed': True}, 'hardware': {'normal': True, 'changed': True}}

## part_2.activity

{'reactive': {'normal': True, 'changed': True}, 'behavior': {'normal': True, 'changed': True}, 'deliberative': {'normal': True, 'changed': True}, 'hybrid': {'normal': True, 'changed': True}, 'safety': {'normal': True, 'changed': True}}

## part_3.activity

{'middleware': {'single': True, 'multiple': True}, 'communication': {'topic': True, 'service': True}, 'failure': {'healthy': True, 'sensor': True, 'type': True, 'visualization': True}, 'inspection': {'nodes': True, 'node_info': True, 'topics': True, 'topic_info': True, 'echo': True, 'services': True, 'broken': True}}
