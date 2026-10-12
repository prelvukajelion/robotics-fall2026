# Mission 3

## Assistive.prediction_draft

I expect the smaller caution margin to reduce unnecessary stops, but it might also make the robot react later when someone gets too close. This could increase the risk of unsafe decisions.

## Warehouse.prediction_draft

I expect the larger caution margin to make the robot more careful and slow down sooner. This might reduce unsafe decisions but could also increase unnecessary stops compared to the baseline.

## context_comparison

The warehouse robot used a 0.75 m stopping threshold and 0.20 m caution margin, giving a 0.62% false-safe rate and 0-second maximum delay. The assistive robot used a 0.95 m threshold and 0.10 m margin, giving 0% false-safe errors and a 0.20-second delay. The higher threshold helps protect nearby people, while the warehouse settings balance safety and work efficiency.


## error_costs

In the warehouse, false-safe errors could damage equipment or hurt workers, while unnecessary stops delay work. The baseline and revised policies both had a 0.62% false-safe rate and 5.61% unnecessary stops. For the assistive robot, unsafe movements could injure people, while unnecessary stops could limit their independence. Both assistive tests had 0% false-safe errors and 1.35% unnecessary stops.


## limitations

The tests show how the robots handle different sensor problems, including missing readings, fast approaches, and conflicting sensors. However, passing these tests does not guarantee safety in every real-world situation. I would consult warehouse workers and people who use assistive robots, then test the robots around moving people and unexpected obstacles before deployment.
