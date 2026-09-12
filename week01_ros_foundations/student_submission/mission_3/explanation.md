# Mission 3

## Data To Command

front_distance scans the LiDAR range list, keeps only readings that are both finite and positive and within the front window, and returns the closest one. decide_velocity then takes that distance and turns it into a command: None or too close, (≤ stop_distance) yields 0.0 (stop), otherwise it returns forward_speed between 0.0 and 0.18 m/s.



## Missing Data Safety

Because no valid measurement could just mean the sensor failed, returned noise, or the obstacle is at an odd angle to register a finite reading, so treating it as clear would be a dangerous assumption. Stopping is the safe default when you lack information, since wrongly stopping is far more safe than wrongly moving into something you couldn't see.

## System Layers

The ROS node subscribes to the LiDAR scan topic, calls your front_distance to extract the nearest front reading, then passes that to decide_velocity to get a bounded speed, and publishes that as the robot's velocity command. The command guard sits between that output and the actual motors as a final safety check, so even if your decision logic had a bug, the guard can still catch an unsafe command.
