# Mission 1

## bias

-0.0141

## bias_vs_variance

Bias measures how far the average is from the true value, while variance measures how spread out the readings are. The sensor had a small bias of -0.0141 m and a variance of 0.00431 m², showing that it was mostly accurate.

## dropouts

6

## mean

1.9859

## median

2.00

## more_samples

No, more samples would not completely fix the problem because the sensor can still produce outliers. Out of 240 readings, there was one large outlier and 6 missing readings.

## outliers

1

## prediction

A biased sensor would give readings that are consistently too high or too low. A noisy sensor would give readings that vary a lot but stay around 2.00 m on average.

## prediction_draft

A biased sensor would give readings that are consistently too high or too low. A noisy sensor would give readings that vary a lot but stay around 2.00 m on average.

## profile

quantized

## robot_consequence

A robot could incorrectly detect an obstacle as being closer than it really is and suddenly stop. This could delay someone relying on the robot or interrupt its task.

## variance

0.00431
