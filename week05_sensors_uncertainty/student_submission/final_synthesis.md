# Final synthesis

In Mission 1, I learned that sensors are not always accurate. My sensor had a mean of 1.9859 m instead of 2.00 m, with a small bias of -0.0141 m. Out of 240 readings, 6 were missing and 1 was an outlier. This showed how sensor errors can affect measurements.

In Mission 2, I tested different filters and sensor weights to improve accuracy. The median filter handled outliers better than the moving average. Using a median filter with window 3 and weight 0.50 gave the lowest RMSE of 0.1270. However, increasing Sensor A's weight to 0.75 reduced the response delay to 0.45 seconds. This showed that accuracy and speed need to be balanced.

In Mission 3, I tested policies for warehouse and assistive robots. The revised warehouse policy had a 0.62% false-safe rate and no detection delay. The assistive robot had a 0% false-safe rate, but changing its caution margin increased the delay from 0.05 to 0.20 seconds.

Overall, I learned that sensors have limitations, and robots need to balance accuracy, speed, and safety depending on where they are used. Testing helps find problems, but more testing is needed before using robots around people.