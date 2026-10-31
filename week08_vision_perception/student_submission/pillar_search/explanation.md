# pillar_search

## diagnosis
In attempt 20261031T020812-dee81cd1, the robot successfully found and centered the blue pillar. The camera picked up the blue color, and the mask separated it from the background. The robot turned toward the pillar as the centroid error got closer to zero, until it was centered. I kept the same settings since they were already working well, so there wasn't really anything to improve or fix.

## evidence
In the four-color attempt, the robot successfully centered red, green, turquoise, and blue. The camera images showed each pillar being detected, and the error graph showed the robot turning until each color was centered. The robot was able to hold its position before moving to the next color. However, just because a color is centered doesn't mean the robot knows what the object actually is or how far away it is. It only knows that the detected color is near the middle of the camera.

