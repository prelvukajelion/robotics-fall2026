# Mission 3

## Specification

The robot starts at (0, 0) facing forward and drives four arcs: left 45°, right 45°, left 45°, then right 45°. Each arc has a radius of 0.30 m. To get that radius, I'll use 0.12 m/s forward and 0.40 rad/s for the turn (positive for left, negative for right), since 0.12 / 0.40 = 0.30. Both speeds are under the limits. Each arc takes about 1.96 seconds and covers about 0.24 m, so the whole path is under 1 m and takes about 8 seconds, which fits easily in the 2 m by 2 m space. At the end, the robot gets a zero speed command so it stops, and it should also stop right away if anything goes wrong. The robot should end up around (0.85, 0.35) facing the same direction it started. It's a success if each arc is within 0.02 m of the right distance and radius and within 0.04 rad of 45°, and if the real robot hits each checkpoint within 0.15 m and 0.20 rad.

## Saved Specification

The robot starts at (0, 0) facing forward and drives four arcs: left 45°, right 45°, left 45°, then right 45°. Each arc has a radius of 0.30 m. To get that radius, I'll use 0.12 m/s forward and 0.40 rad/s for the turn (positive for left, negative for right), since 0.12 / 0.40 = 0.30. Both speeds are under the limits. Each arc takes about 1.96 seconds and covers about 0.24 m, so the whole path is under 1 m and takes about 8 seconds, which fits easily in the 2 m by 2 m space. At the end, the robot gets a zero speed command so it stops, and it should also stop right away if anything goes wrong. The robot should end up around (0.85, 0.35) facing the same direction it started. It's a success if each arc is within 0.02 m of the right distance and radius and within 0.04 rad of 45°, and if the real robot hits each checkpoint within 0.15 m and 0.20 rad.

## Assigned Pattern

alternating_arcs

## Original Prompt

I'm working on a ROS 2 robot motion project. Here is my specification for the path I want the robot to drive:

This is a ROS 2 Jazzy Python package. Implement only build_pattern(pattern_name: str) -> list[Segment] for 'alternating_arcs' in the existing pattern.py.
The course-provided pattern_node.py calls this function, publishes the returned segments repeatedly through /student_cmd_vel, and sends the final zero command.
Use the existing Segment class with linear_x (m/s), angular_z (rad/s), and duration (s).
Return the ordered segments for the assigned specification and raise ValueError for an unknown pattern name.
Stay within 0.22 m/s, 0.80 rad/s, 30 seconds per segment, and 60 seconds total.
Do not replace the wrapper or course checks. Explain assumptions and propose tests.

## Original Output

The function returns four arc segments: left, right, left, right. Each one uses 0.12 m/s and 0.40 rad/s for about 1.96 s, which gives a 0.30 m radius and a 45° turn. Any name other than alternating_arcs raises a ValueError. It creates no publishers and doesn't touch the wrapper or the course checks.

I checked the math by simulating the path. The robot should pass through these points:

After arc	Position (m)	Heading (rad)
1 (left)	(0.21, 0.09)	0.785
2 (right)	(0.42, 0.18)	0
3 (left)	(0.64, 0.26)	0.785
4 (right)	(0.85, 0.35)	0

Total time is about 7.9 s, and each arc is about 0.236 m long.

Assumptions

Segment is already defined in pattern.py and accepts linear_x, angular_z, and duration as keyword arguments. That's why the file only contains the function.
The robot starts at rest at (0, 0) facing +x, and the wrapper runs the segments back to back with no pause between them.
The math uses the ideal model with instant speed changes. The real robot needs time to speed up and to switch from turning left to turning right, so its real path will come up a little short. That's why the live tolerances are bigger.
I picked 0.40 rad/s because it's well under the limit and makes each arc last long enough that speed-up time is a small part of it. It's also not so slow that friction becomes a problem.
The robot ends facing its starting direction because the left and right turns cancel out.

Proposed tests

Calling it with an unknown name like "square" raises ValueError.
It returns exactly 4 segments.
Every segment has linear_x between 0 and 0.22, abs(angular_z) at most 0.80, and duration greater than 0 and at most 30. The durations add up to 60 or less.
Each arc's radius (linear_x / abs(angular_z)) is within 0.02 m of 0.30.
Each arc's turn (abs(angular_z) * duration) is within 0.04 rad of 0.785, and the turn signs go +, −, +, −.
Each arc's length (linear_x * duration) is within 0.02 m of 0.236.
The total heading change adds up to 0 within 0.04 rad.
Simulating the path gives the checkpoints in the table above and stays inside the 2 m by 2 m area.

## Original Source

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

## Assumptions

The AI assumed the Segment class already exists in pattern.py and takes linear_x, angular_z, and duration as keyword arguments. It used meters per second, radians per second, seconds, and radians for angles. It assumed the robot starts at (0, 0) facing +x and that positive angular_z means turning left. It also assumed the segments run back to back with no pause and that the robot changes speed instantly, which a real robot can't do.

## Problems

The radius is 0.12 / 0.40 = 0.30 m, each turn is 0.40 × 1.96 ≈ 0.785 rad (45°), and each arc is 0.12 × 1.96 ≈ 0.236 m. The turn signs go +, −, +, −, so they cancel out and the robot ends facing forward. The total time is about 7.9 s, which is under 60 s. I also checked the first checkpoint by hand and got about (0.21, 0.09). One thing I'm unsure about is whether Segment really accepts keyword arguments, since the AI never saw the original file. Another is that the robot switches straight from turning left to turning right, so the real robot might lag and come up a little short.

## Test Plan

For the pattern behavior test, I'll call build_pattern("alternating_arcs") and check that it returns 4 segments with turns of +, −, +, −, each about 0.785 rad with a 0.30 m radius. I expect the path to end near (0.85, 0.35) facing heading 0. For the velocity-limit test, I'll check that every segment has a forward speed of 0.22 m/s or less, a turn speed of 0.80 rad/s or less, and a duration between 0 and 30 s, with a total of 60 s or less. I expect every segment to be 0.12 m/s, 0.40 rad/s, and about 1.96 s, so it should pass. For the stop test, I'll check that the last command sent on /student_cmd_vel is zero and that the robot actually stops moving after the last arc. I expect it to stop near (0.85, 0.35) and stay there.

## Modifications

The AI's code was mostly correct, so I only made small changes. I put the function into the course's pattern.py and kept the existing Segment class, and I checked that it works with the way the AI created segments. I added import math below the from __future__ line because the code uses math.pi and that line has to be first. I kept the duration calculated from the formula instead of typing 1.96, so each turn stays exactly 45°, which the angle test checks. I left out the final stop because the wrapper already sends it.

## Live Pending

False

## Evidence Analysis

My tests show that build_pattern returns 4 arcs that each move forward with a 0.30 m radius, a 0.236 m length, and a 45° turn, with all speeds and duration inside the course limits. They also show the turns go left, right, left, right. The evaluator ran 9 tests and all 9 passed, including my 2. The assigned geometry, command limits, and stop decision checks also passed, and the predicted endpoint was (0.849, 0.351) with heading 0, which matches what I expected. The live motion and stop check passed too, so the robot followed the path closely enough and stopped at the end. However, this was only one live run in a clear area, so it doesn't show that the robot does this every time or that it's safe around people or obstacles. One more test I would want is to repeat the live run several times and record how far off each checkpoint is, to make sure the results stay within 0.15 m and 0.20 rad every time.

## Ai Disclosure

I used Claude. It helped me understand the motion and frame concepts, generated the build_pattern code and my test file, and helped me draft some of my written answers. I reviewed the code by checking the math myself: the radius (0.12 / 0.40 = 0.30 m), the turn per arc (about 0.785 rad), the arc length (about 0.236 m), and that the turn signs cancel so the robot ends facing forward. I put the function into the course's pattern.py, kept the existing Segment class, and made sure the imports were in the right order. I verified it by running the evaluator, which passed all 9 tests and every check, including the live run.
