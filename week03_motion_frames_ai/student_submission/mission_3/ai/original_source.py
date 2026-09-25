import math

# Segment is already defined in the existing pattern.py (linear_x, angular_z, duration).


def build_pattern(pattern_name: str) -> list[Segment]:
    """Return the ordered motion segments for the named pattern."""
    if pattern_name != 'alternating_arcs':
        raise ValueError(f"Unknown pattern name: {pattern_name!r}")

    # Four 45-degree arcs of radius 0.30 m: left, right, left, right.
    radius = 0.30                              # m
    arc_angle = math.pi / 4                    # 45 degrees = 0.785 rad
    angular_speed = 0.40                       # rad/s (limit 0.80)
    linear_speed = angular_speed * radius      # 0.12 m/s (limit 0.22), so v / w = 0.30 m
    duration = arc_angle / angular_speed       # about 1.96 s per arc (limit 30 s)

    turn_directions = [1, -1, 1, -1]           # +1 = turn left, -1 = turn right

    return [
        Segment(
            linear_x=linear_speed,
            angular_z=direction * angular_speed,
            duration=duration,
        )
        for direction in turn_directions
    ]