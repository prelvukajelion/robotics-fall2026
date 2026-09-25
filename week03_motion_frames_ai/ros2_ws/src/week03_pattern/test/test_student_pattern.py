import math
import os
import unittest

from week03_pattern.pattern import build_pattern

RADIUS = 0.30               # m
ARC_ANGLE = math.pi / 4     # 45 degrees in radians
ARC_LENGTH = RADIUS * ARC_ANGLE   # about 0.236 m


class MyPatternTests(unittest.TestCase):
    def test_my_pattern_geometry(self):
        segments = build_pattern(os.environ.get("WEEK03_ASSIGNED_PATTERN", "alternating_arcs"))

        # Four arcs
        self.assertEqual(len(segments), 4)

        for seg in segments:
            # Every arc moves forward and turns
            self.assertGreater(seg.linear_x, 0.0)
            self.assertNotEqual(seg.angular_z, 0.0)

            # Radius R = |v / w| is 0.30 m
            self.assertAlmostEqual(abs(seg.linear_x / seg.angular_z), RADIUS, delta=0.02)

            # Distance v * t is the arc length
            self.assertAlmostEqual(seg.linear_x * seg.duration, ARC_LENGTH, delta=0.02)

            # Turn |w| * t is 45 degrees
            self.assertAlmostEqual(abs(seg.angular_z) * seg.duration, ARC_ANGLE, delta=0.04)

            # Speeds and duration stay inside the course limits
            self.assertLessEqual(seg.linear_x, 0.22)
            self.assertLessEqual(abs(seg.angular_z), 0.80)
            self.assertGreater(seg.duration, 0.0)
            self.assertLessEqual(seg.duration, 30.0)

        self.assertLessEqual(sum(seg.duration for seg in segments), 60.0)

    def test_my_pattern_order(self):
        segments = build_pattern(os.environ.get("WEEK03_ASSIGNED_PATTERN", "alternating_arcs"))

        # Turn order is left, right, left, right
        signs = [1 if seg.angular_z > 0 else -1 for seg in segments]
        self.assertEqual(signs, [1, -1, 1, -1])

        # Walk through the arcs to find the final pose
        x, y, heading = 0.0, 0.0, 0.0
        for seg in segments:
            new_heading = heading + seg.angular_z * seg.duration
            r = seg.linear_x / seg.angular_z
            x += r * (math.sin(new_heading) - math.sin(heading))
            y -= r * (math.cos(new_heading) - math.cos(heading))
            heading = new_heading

        # Ends facing the starting direction, near (0.85, 0.35)
        self.assertAlmostEqual(heading, 0.0, delta=0.04)
        self.assertAlmostEqual(x, 0.849, delta=0.02)
        self.assertAlmostEqual(y, 0.351, delta=0.02)


if __name__ == "__main__":
    unittest.main()