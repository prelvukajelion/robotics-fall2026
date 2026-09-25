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