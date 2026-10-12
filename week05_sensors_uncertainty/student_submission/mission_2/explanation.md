# Mission 2

## comparison

For the moving average, window 3 had the lowest RMSE of 0.1395, compared to 0.1504 for window 7 and 0.1601 for window 11. All three had a delay of 1.1 seconds. The median with window 3 was slightly better, with an RMSE of 0.1389 and the same delay.

## fusion_choice

With the median filter, weight 0.25 had an RMSE of 0.1389 and a delay of 1.1 seconds. Weight 0.50 improved these to 0.1270 and 0.9 seconds, while weight 0.75 had 0.1335 and 0.45 seconds. I would choose 0.50 because it had the lowest RMSE while balancing Sensor A's noise and Sensor B's slower, biased readings.

## manual_average

4.1667

## manual_fusion

2.25

## manual_median

2.3

## prediction_draft

I predict a faster response because Sensor A has more weight, but its noise may cause more error.

## responsiveness

Larger moving average windows did not increase the measured delay, which stayed at 1.1 seconds for all three. However, giving Sensor A more weight reduced the delay to 0.45 seconds. A slower response could cause a robot to react too late when someone walks in front of it.

## selected

0
