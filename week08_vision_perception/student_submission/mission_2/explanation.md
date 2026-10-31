# mission_2

## comparison
For normal, the classical detector had 0 correct boxes, 2 false boxes, and missed both mugs. The learned detector did much better, finding both mugs without any false boxes. For dim, the classical detector had the same results, while the learned detector found 1 mug and missed the other. For occluded, neither detector found the mugs, but the classical detector still had 2 false boxes. In normal 1, the learned detector had a much better box around the mug, while the classical one picked up too much of the desk. This matters because the robot needs to know where the mug actually is.

## choice
I would go with the learned detector at a threshold of 0.30. It did a better job finding the mug, even though it was slower at around 30 ms per image compared to 2–5 ms for the classical detector. In normal 1, the foreground mask had an IoU of 0.5461, but it also picked up parts of the desk. So even though the mask showed a lot of detail, it couldn't really tell which object was the mug. The test also used a pretty small set of images, so it's hard to say how well it would work in other situations.
