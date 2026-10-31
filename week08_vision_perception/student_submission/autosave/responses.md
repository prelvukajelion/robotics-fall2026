# Lab 7 saved answers

## mission_1.diagnosis
In normal 1, the detector finds the mug, but the box also includes part of the desk because of their similar colors. In dim 1, the detector still finds the mug, but the darker lighting causes some parts of the mug to disappear from the mask. This shows how lighting and similar colors can affect the detector's accuracy.

## mission_1.limitations
I increased the minimum saturation to 122 to try to filter out more of the background. It helped a little, but the detector still picked up parts of the desk. It could also have trouble with other cups or backgrounds that have similar colors.

## line_following.comparison
For the straight practice, I used a gain of 0.08 and the robot stayed pretty close to the line, although it lost it once. I kept the same gain for my first curved-track attempt, but the robot had trouble staying centered around the turns. For my second track attempt, I increased the gain to 0.20, which helped quite a bit. The average error dropped from 0.4852 to 0.2444, and the robot finished faster. The mask was still detecting the line, but the stronger steering helped the robot stay closer to it around curves.

## line_following.limits
During the straight practice, the robot lost the line once, which caused it to stop tracking. This was an issue with detecting the line in the camera rather than knowing where to steer. For a real delivery robot around people, I think it would need something like depth cameras or lidar to detect obstacles and know how far away they are. It would also need more testing around people, different lighting conditions, and unexpected obstacles to make sure it can stop safely.

## pillar_search.diagnosis
In attempt 20261031T020812-dee81cd1, the robot successfully found and centered the blue pillar. The camera picked up the blue color, and the mask separated it from the background. The robot turned toward the pillar as the centroid error got closer to zero, until it was centered. I kept the same settings since they were already working well, so there wasn't really anything to improve or fix.

## pillar_search.evidence
In the four-color attempt, the robot successfully centered red, green, turquoise, and blue. The camera images showed each pillar being detected, and the error graph showed the robot turning until each color was centered. The robot was able to hold its position before moving to the next color. However, just because a color is centered doesn't mean the robot knows what the object actually is or how far away it is. It only knows that the detected color is near the middle of the camera.


## mission_2.comparison
For normal, the classical detector had 0 correct boxes, 2 false boxes, and missed both mugs. The learned detector did much better, finding both mugs without any false boxes. For dim, the classical detector had the same results, while the learned detector found 1 mug and missed the other. For occluded, neither detector found the mugs, but the classical detector still had 2 false boxes. In normal 1, the learned detector had a much better box around the mug, while the classical one picked up too much of the desk. This matters because the robot needs to know where the mug actually is.

## mission_2.choice
I would go with the learned detector at a threshold of 0.30. It did a better job finding the mug, even though it was slower at around 30 ms per image compared to 2–5 ms for the classical detector. In normal 1, the foreground mask had an IoU of 0.5461, but it also picked up parts of the desk. So even though the mask showed a lot of detail, it couldn't really tell which object was the mug. The test also used a pretty small set of images, so it's hard to say how well it would work in other situations.

## final.synthesis
These three missions showed me how important it is for a robot to correctly understand what its camera is seeing. In Mission 1, the classical detector kept picking up parts of the desk along with the mug, while the learned detector did a better job finding it. In Mission 2, the robot was able to find and center all four colored pillars using the camera, although that doesn't mean it actually knows what the objects are or how far away they are. In Mission 3, I noticed how much the steering gain affected the robot's ability to follow the line. Increasing it from 0.08 to 0.20 on the curved track lowered the average error from 0.4852 to 0.2444 and helped the robot finish faster. Overall, I learned that even small changes in detection or steering can make a big difference in how a robot behaves. There's still a lot to consider though, especially with different lighting, obstacles, and making sure the robot can operate safely around people.

## final.course_reflection
This lab made me realize how much goes into getting a robot to do something that seems pretty simple. What stood out to me most was how changing one setting could make such a big difference, especially when adjusting the steering gain for the curved track. It was interesting to see how the robot used its camera to make decisions and correct itself. It also reminded me how important safety is in robotics, since even small mistakes could cause problems around people. Overall, I enjoyed the hands-on experience, and it made me more interested in how robotics and software work together.
