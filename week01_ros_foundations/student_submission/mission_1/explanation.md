# Mission 1

## Command Path Explanation

student_cmd_vel carries your node's proposed velocity, which a guard node checks against scan before republishing it on cmd_vel. That split means the safety filter can't be bypassed by a bug in your control code, since the base controller only ever listens to cmd_vel.

## Graph Explanation

A ROS2 shows the live components running in the software. Nodes such as rivz2 being a support tool for the person, and topics such as odom running an estimate of its position, direction, and movement.

## Guided Checks

{'bridge_info': True, 'command_topics': True, 'guard_info': True, 'node_list': True, 'scan_info': True, 'scan_message': True}

## Scan Observation

I noticed some infinities in the message. Could indicate the open space in the model.

## Tools Explanation

Gazebo is responsible for creating the world and the data, while RViz is responsible for showing you what the robot believes about that data.
