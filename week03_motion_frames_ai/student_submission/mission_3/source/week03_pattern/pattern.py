"""AI-assisted motion pattern implementation.

Preserve the original AI response in Streamlit. Review it, then implement a safe
version here. The node accepts only segments returned by ``build_pattern``.
"""
from __future__ import annotations

import math
from dataclasses import dataclass


@dataclass(frozen=True)
class Segment:
    linear_x: float
    angular_z: float
    duration: float


def build_pattern(pattern_name: str) -> list[Segment]:
    """Return ordered, bounded motion segments for the assigned pattern.

    Supported assignments are ``rounded_rectangle``, ``l_path``, and
    ``alternating_arcs``. Do not include the final stop; the ROS wrapper always
    publishes it and the evaluator verifies it.
    """
    if pattern_name != 'alternating_arcs':
        raise ValueError(f"Unknown pattern name: {pattern_name!r}")

    # Four 45-degree arcs of radius 0.30 m: left, right, left, right.
    radius = 0.30                              # m
    arc_angle = math.pi / 4                    # 45 degrees = 0.785 rad
    angular_speed = 0.40                       # rad/s (limit 0.80)
    linear_speed = angular_speed * radius      # 0.12 m/s (limit 0.22), R = v / w = 0.30 m
    duration = arc_angle / angular_speed       # t = |dtheta / w|, about 1.96 s per arc

    turn_directions = [1, -1, 1, -1]           # +1 = turn left, -1 = turn right

    return [
        Segment(
            linear_x=linear_speed,
            angular_z=direction * angular_speed,
            duration=duration,
        )
        for direction in turn_directions
    ]