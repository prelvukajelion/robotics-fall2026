# Week 5: Sensors, Noise, and Uncertainty

- name: Elion Prelvukaj
- email: elion.prelvukaj38@stu-mail.cuny.edu
- course_id: CSCI 39536

## concepts.observation

Increasing noise caused the readings to spread out more, increasing the variance and standard deviation. Increasing bias shifted the readings and their mean away from the true value without significantly changing their spread.


## final.course_reflection

This activity showed me how meticulous robotics can be, since even small changes in sensor readings or settings can affect how a robot behaves. It also showed me the importance of ethics and human considerations in robotics. With the warehouse and assistive robots, I saw how even small decisions can affect both safety and people's daily lives. It further confirmed that robotics is not just about making something work but also making sure it is safe and reliable for the people around it.

## final.synthesis

In Mission 1, I learned that sensors are not always accurate. My sensor had a mean of 1.9859 m instead of 2.00 m, with a small bias of -0.0141 m. Out of 240 readings, 6 were missing and 1 was an outlier. This showed how sensor errors can affect measurements.

In Mission 2, I tested different filters and sensor weights to improve accuracy. The median filter handled outliers better than the moving average. Using a median filter with window 3 and weight 0.50 gave the lowest RMSE of 0.1270. However, increasing Sensor A's weight to 0.75 reduced the response delay to 0.45 seconds. This showed that accuracy and speed need to be balanced.

In Mission 3, I tested policies for warehouse and assistive robots. The revised warehouse policy had a 0.62% false-safe rate and no detection delay. The assistive robot had a 0% false-safe rate, but changing its caution margin increased the delay from 0.05 to 0.20 seconds.

Overall, I learned that sensors have limitations, and robots need to balance accuracy, speed, and safety depending on where they are used. Testing helps find problems, but more testing is needed before using robots around people.

## mission_1.bias

-0.0141

## mission_1.bias_vs_variance

Bias measures how far the average is from the true value, while variance measures how spread out the readings are. The sensor had a small bias of -0.0141 m and a variance of 0.00431 m², showing that it was mostly accurate.

## mission_1.dropouts

6

## mission_1.mean

1.9859

## mission_1.median

2.00

## mission_1.more_samples

No, more samples would not completely fix the problem because the sensor can still produce outliers. Out of 240 readings, there was one large outlier and 6 missing readings.

## mission_1.outliers

1

## mission_1.prediction

A biased sensor would give readings that are consistently too high or too low. A noisy sensor would give readings that vary a lot but stay around 2.00 m on average.

## mission_1.prediction_draft

A biased sensor would give readings that are consistently too high or too low. A noisy sensor would give readings that vary a lot but stay around 2.00 m on average.

## mission_1.profile

quantized

## mission_1.robot_consequence

A robot could incorrectly detect an obstacle as being closer than it really is and suddenly stop. This could delay someone relying on the robot or interrupt its task.

## mission_1.variance

0.00431

## mission_2.comparison

For the moving average, window 3 had the lowest RMSE of 0.1395, compared to 0.1504 for window 7 and 0.1601 for window 11. All three had a delay of 1.1 seconds. The median with window 3 was slightly better, with an RMSE of 0.1389 and the same delay.

## mission_2.fusion_choice

With the median filter, weight 0.25 had an RMSE of 0.1389 and a delay of 1.1 seconds. Weight 0.50 improved these to 0.1270 and 0.9 seconds, while weight 0.75 had 0.1335 and 0.45 seconds. I would choose 0.50 because it had the lowest RMSE while balancing Sensor A's noise and Sensor B's slower, biased readings.

## mission_2.manual_average

4.1667

## mission_2.manual_fusion

2.25

## mission_2.manual_median

2.3

## mission_2.prediction_draft

I predict a faster response because Sensor A has more weight, but its noise may cause more error.

## mission_2.responsiveness

Larger moving average windows did not increase the measured delay, which stayed at 1.1 seconds for all three. However, giving Sensor A more weight reduced the delay to 0.45 seconds. A slower response could cause a robot to react too late when someone walks in front of it.

## mission_2.selected

0

## mission_3.Assistive.prediction_draft

I expect the smaller caution margin to reduce unnecessary stops, but it might also make the robot react later when someone gets too close. This could increase the risk of unsafe decisions.

## mission_3.Warehouse.prediction_draft

I expect the larger caution margin to make the robot more careful and slow down sooner. This might reduce unsafe decisions but could also increase unnecessary stops compared to the baseline.

## mission_3.context_comparison

The warehouse robot used a 0.75 m stopping threshold and 0.20 m caution margin, giving a 0.62% false-safe rate and 0-second maximum delay. The assistive robot used a 0.95 m threshold and 0.10 m margin, giving 0% false-safe errors and a 0.20-second delay. The higher threshold helps protect nearby people, while the warehouse settings balance safety and work efficiency.


## mission_3.error_costs

In the warehouse, false-safe errors could damage equipment or hurt workers, while unnecessary stops delay work. The baseline and revised policies both had a 0.62% false-safe rate and 5.61% unnecessary stops. For the assistive robot, unsafe movements could injure people, while unnecessary stops could limit their independence. Both assistive tests had 0% false-safe errors and 1.35% unnecessary stops.


## mission_3.limitations

The tests show how the robots handle different sensor problems, including missing readings, fast approaches, and conflicting sensors. However, passing these tests does not guarantee safety in every real-world situation. I would consult warehouse workers and people who use assistive robots, then test the robots around moving people and unexpected obstacles before deployment.
