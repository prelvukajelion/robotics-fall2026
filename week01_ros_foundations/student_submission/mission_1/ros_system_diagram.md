# Observed ROS 2 system diagram

```mermaid
flowchart LR
  n0["/course_cmd_vel_guard"]
  n1["/course_evidence_collector"]
  n2["/obstacle_guard"]
  n3["/robot_state_publisher"]
  n4["/ros_gz_bridge"]
  n5["/rviz2"]
  n6["/transform_listener_impl_aaaad626ee90"]
  t0(["/cmd_vel<br/>TwistStamped"])
  n0 -->|publishes| t0
  t0 -->|subscribes| n4
  t1(["/odom<br/>Odometry"])
  n4 -->|publishes| t1
  t1 -->|subscribes| n1
  t2(["/scan<br/>LaserScan"])
  n4 -->|publishes| t2
  t2 -->|subscribes| n1
  t2 -->|subscribes| n2
  t3(["/student_cmd_vel<br/>Twist"])
  n2 -->|publishes| t3
  t3 -->|subscribes| n0
  t3 -->|subscribes| n1
  t4(["/tf<br/>TFMessage"])
  n3 -->|publishes| t4
  n4 -->|publishes| t4
  t4 -->|subscribes| n6
```

This diagram is generated from the captured publisher and subscriber endpoints. A missing arrow records a missing live endpoint, not an assumed connection.

## Guided terminal observations

| Observation | Completed |
|---|---|
| Listed the running nodes | Yes |
| Inspected the command guard | Yes |
| Inspected the simulator bridge | Yes |
| Inspected the scan connections | Yes |
| Viewed one scan message | Yes |
| Compared proposed and approved command topics | Yes |
