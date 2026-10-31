# line_following

## comparison
For the straight practice, I used a gain of 0.08 and the robot stayed pretty close to the line, although it lost it once. I kept the same gain for my first curved-track attempt, but the robot had trouble staying centered around the turns. For my second track attempt, I increased the gain to 0.20, which helped quite a bit. The average error dropped from 0.4852 to 0.2444, and the robot finished faster. The mask was still detecting the line, but the stronger steering helped the robot stay closer to it around curves.

## limits
During the straight practice, the robot lost the line once, which caused it to stop tracking. This was an issue with detecting the line in the camera rather than knowing where to steer. For a real delivery robot around people, I think it would need something like depth cameras or lidar to detect obstacles and know how far away they are. It would also need more testing around people, different lighting conditions, and unexpected obstacles to make sure it can stop safely.
