"""Mission 2 student implementation.

Complete only ``transform_camera_point`` after preserving the initial AI output
in the guide. Course tests supply both real and simulated TF buffers.
"""
from geometry_msgs.msg import PointStamped
from rclpy.duration import Duration
from tf2_ros import TransformException
import tf2_geometry_msgs  # noqa: F401  Registers PointStamped so tf2_ros can transform it.

SOURCE_FRAME = 'hall_camera'
TARGET_FRAME = 'base_link'

# Short wait in case TF data for the point's timestamp hasn't arrived yet.
TRANSFORM_TIMEOUT = Duration(seconds=0.1)


def transform_camera_point(tf_buffer, point: PointStamped) -> PointStamped | None:
    """Return a hall_camera point expressed in base_link, or None if unavailable."""
    if point.header.frame_id != SOURCE_FRAME:
        raise ValueError(
            f"Expected point in frame '{SOURCE_FRAME}', got '{point.header.frame_id}'"
        )

    try:
        # tf2 looks up the transform at point.header.stamp, so the result
        # matches where the robot was when the camera saw the point.
        transformed = tf_buffer.transform(point, TARGET_FRAME, timeout=TRANSFORM_TIMEOUT)
    except TransformException:
        # Covers lookup, connectivity, extrapolation, and timeout errors.
        return None

    # Keep the original observation time on the result.
    transformed.header.stamp = point.header.stamp
    return transformed