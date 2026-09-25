# Mission 2

## Snapshot

{'source': 'reference', 'captured_at': '2026-09-25T14:50:58.990066+00:00', 'description': 'Instructor-defined frame geometry. No live ROS transforms were measured.', 'frames': ['odom', 'base_link', 'base_scan', 'rear_camera_link', 'hall_camera'], 'transforms': {'base_scan_to_base_link': {'translation': {'x': 0.2, 'y': 0.0, 'z': 0.14}, 'yaw': 0.0}, 'rear_camera_to_base_link': {'translation': {'x': -0.18, 'y': 0.0, 'z': 0.22}, 'yaw': 3.141592653589793}, 'hall_camera_to_base_link': {'translation': {'x': -1.5, 'y': 0.5, 'z': 1.2}, 'yaw': -1.5707963267948966}}}

## Frame Context

The rear camera is attached to the robot, so it moves along with base_link. No matter where the robot goes, the camera stays in the same spot on the robot, 0.18 m behind the center, 0.22 m up, and facing backward, so the transform between them never changes. The hallway camera is fixed to the wall and doesn't move with the robot. When the robot drives or turns, its position and direction change compared to the camera, so the transform between the hallway camera and base_link keeps changing and has to be updated as the robot moves.

## Initial Prompt

Write ROS 2 Python code that converts a point detected by the hallway camera into the robot's base_link frame.

## Initial Output

his node listens for detected points, uses tf2 to look up the hallway camera to base_link transform at the moment each point was detected, and publishes the converted point.

Since the prompt left out details, the code makes these assumptions:

Detections come in as PointStamped messages on /hallway_camera/point, with the frame name hallway_camera.
The hallway camera's position in the map frame is published as a static transform. For example: ros2 run tf2_ros static_transform_publisher --x 1.0 --y 2.0 --z 1.2 --yaw 0.0 --frame-id map --child-frame-id hallway_camera (replace these numbers with the camera's real position).
The robot's position is tracked through map -> odom -> base_link by localization and odometry. Without this, there's no way to connect the fixed camera to the moving robot.
The detected point is already in the camera's regular frame, not a camera optical frame (where z points forward). If it's in an optical frame, that needs to be part of the TF tree too.
If a transform isn't available, the point is skipped with a warning instead of crashing the node.

The code file is below.

## Initial Source

#!/usr/bin/env python3
"""
Convert points detected by a fixed hallway camera into the robot's base_link frame.

Assumptions:
- Detections arrive as geometry_msgs/PointStamped on /hallway_camera/point,
  with header.frame_id = "hallway_camera".
- The TF tree connects hallway_camera to base_link, for example:
    map -> hallway_camera      (static: the camera is fixed in the hallway)
    map -> odom -> base_link   (dynamic: from localization + odometry)
"""

import rclpy
from rclpy.node import Node
from rclpy.duration import Duration

from geometry_msgs.msg import PointStamped
from tf2_ros import Buffer, TransformListener, TransformException
import tf2_geometry_msgs  # noqa: F401  (lets tf2 transform PointStamped messages)


class HallwayPointConverter(Node):
    def __init__(self):
        super().__init__('hallway_point_converter')

        # Topic and frame names can be changed at launch time
        self.declare_parameter('input_topic', '/hallway_camera/point')
        self.declare_parameter('output_topic', '/hallway_camera/point_base_link')
        self.declare_parameter('target_frame', 'base_link')

        input_topic = self.get_parameter('input_topic').value
        output_topic = self.get_parameter('output_topic').value
        self.target_frame = self.get_parameter('target_frame').value

        # TF buffer stores recent transforms; the listener fills it from /tf and /tf_static.
        # spin_thread=True lets the listener keep receiving TF while we wait in a callback.
        self.tf_buffer = Buffer()
        self.tf_listener = TransformListener(self.tf_buffer, self, spin_thread=True)

        self.sub = self.create_subscription(PointStamped, input_topic, self.on_point, 10)
        self.pub = self.create_publisher(PointStamped, output_topic, 10)

        self.get_logger().info(
            f'Converting points from {input_topic} into {self.target_frame}, '
            f'publishing on {output_topic}'
        )

    def on_point(self, msg: PointStamped):
        # The robot keeps moving, so use the transform at the time the point was detected
        # (msg.header.stamp). Wait briefly in case TF data is slightly behind.
        try:
            point_base = self.tf_buffer.transform(
                msg, self.target_frame, timeout=Duration(seconds=0.1)
            )
        except TransformException as ex:
            self.get_logger().warn(
                f'Could not transform {msg.header.frame_id} -> {self.target_frame}: {ex}'
            )
            return

        self.pub.publish(point_base)
        p = point_base.point
        self.get_logger().info(
            f'Point in {self.target_frame}: x={p.x:.3f}, y={p.y:.3f}, z={p.z:.3f}'
        )


def main(args=None):
    rclpy.init(args=args)
    node = HallwayPointConverter()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()

## Initial Analysis

The response assumed the camera frame is called hallway_camera and that it connects to base_link through a map frame. It assumed the camera sets the PointStamped frame name and timestamp correctly, and that the camera and robot clocks match. It used the default TF buffer and a short 0.1 s wait without thinking about late or delayed data. It avoided hard-coding the table offsets, which is good since the robot moves, but it didn't say where the camera's real position comes from. If a transform isn't available, the point is just skipped and lost. It also assumed the robot's movement is published as map -> odom -> base_link without naming any topics like odom.

## Improved Changes

The improved prompt removed the guessing. Instead of the AI choosing frame names, the prompt set them as hall_camera to base_link and required rejecting any other frame. It also required using the point's timestamp so the transform matches when the point was seen. For TF, it had the code use a buffer that's passed in, import tf2_geometry_msgs, and avoid hard-coded offsets. For failures, it made the code return None if the transform isn't available, raise an error for the wrong frame, and never publish or move the robot.

## Live Pending

True

## Synthesis

The first AI output guessed a lot, like the camera frame name, the topic names, and that the robot's position was already being published, and it just logged a warning and skipped the point when the transform failed. The improved prompt fixed this by setting the exact frames (hall_camera to base_link), rejecting points from the wrong frame, using the supplied TF buffer and the point's timestamp, returning None on failure, and never publishing motion. If the wrong transform were used, the robot could think a person is in the wrong spot, such as on its left when they're really on its right, or farther away than they are, and it could drive toward them instead of away. The tests test_uses_camera_as_source_and_body_as_target and test_uses_buffer_result_including_rotation catch this by checking that the frames aren't swapped and that rotation isn't ignored. When transform data is unavailable, the robot shouldn't guess where the person is. It should ignore that detection and slow down or stop until it has reliable data again.

## Live Issue

When I ran the live check, all 5 unit tests passed, but the live test failed and returned no point with no error message. This means my function returned None because it couldn't find the transform from hall_camera to base_link. I tried running the full tests and reading the output, which showed my code logic works. What's still unverified is why the live transform wasn't available, whether the transforms weren't being published, the 0.1 s timeout was too short, or the timestamp didn't match, and whether the function gives a correct point on the real system.
