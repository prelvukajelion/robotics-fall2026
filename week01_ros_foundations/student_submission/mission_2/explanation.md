# Mission 2

## Measurement Explanation

For the right hand curve test, the robot curved way more to the right than I anticipated. I also did not expect the robot to be facing fully to the right at the end of the test.

## Motion Comparison

The measured motion was actually less than my prediction, 0.389 to my 0.5. Also a little extra bit of delay with it being 3.05 seconds instead of being a little less than 3.

## Prediction Locks

{'straight': '2026-09-10T17:33:02.789140+00:00', 'rotation': '2026-09-10T17:59:46.483647+00:00', 'curve': '2026-09-10T18:11:40.271262+00:00', 'curve_modified': '2026-09-10T18:30:08.972271+00:00'}

## Predictions

{'rotation': 'I predict the robot will do 1 and a half rotation, and will end up facing northwest.', 'straight': 'I predict the robot will be about half a meter from where it started.', 'curve': 'I predict it will move close to .60 meters forward along the curve and it will turn to the right about 1.6 radians.', 'curve_modified': 'The curve will be more tighter. Perhaps it will result in a Shape.'}

## Safety Explanation

The command guard checks every proposed velocity before it reaches the base controller, clamping anything above the speed limit and rejecting malformed values like NaN or inf.
The final zero command is the deliberate end of a trial, explicitly telling the robot to stop rather than leaving it holding the last velocity it received. 
The timeout is needed if your program never gets there, because it crashed, was killed, or lost communication mid-motion. The guard runs as a separate process, so it can notice the silence and publish a stop after 0.5 seconds on its own.

## Modified Settings

{'linear_x': 0.12, 'angular_z': 0.6, 'duration': 4.0}
