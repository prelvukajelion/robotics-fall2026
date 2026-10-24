# Week 6: SLAM and Mapping

- email: elion.prelvukaj38@login.cuny.edu
- name: Elion Prelvukaj

## final.course_reflection

This activity made me realize how difficult mapping even a relatively simple room can be. I was surprised by how easily errors could occur from small movements, sharp turns, or inaccurate sensor readings. Something that seems easy actually requires a lot of precision and patience. One thing that stood out to me was how much the way I controlled the robot affected the final map. Even when I thought I was moving carefully, certain movements could cause walls to become misaligned or create unnecessary noise in the scan. It was interesting to see how small mistakes could build up and affect the overall result. This lab showed me that creating an accurate map requires careful planning and consistent movement.

## final.synthesis

Throughout both missions, I learned how the robot uses LiDAR scans and motion estimates to build a map of the TurtleBot3 House. LiDAR helps detect walls and obstacles, while motion estimates track where the robot is moving. However, the robot cannot always accurately determine its position or detect areas it hasn't explored. One of the biggest challenges was actually maneuvering the robot. I noticed that making sharp turns while barely moving forward could mess up the scan rather than improve it. Moving slowly and continuously seemed to work better because the robot could collect more consistent measurements. Revisiting areas also helped SLAM recognize previously mapped walls and potentially correct positioning errors. Both missions took some time, but the second route produced better results. Map coverage increased from 44.83% to 54%, while the quality score improved from 68.3 to 85.8. The second map also had less scattered noise and better wall alignment which shows that the route and how the robot moves can be just as important as the time spent mapping. I would trust the second map more for a later task because it provides better coverage and fewer visible errors. However, neither map is perfect, and unexplored areas could still cause problems.

## mission_1.drift_and_revisit

It did at first once I scanned the left side, but once I went back to the bigger room that's where it all fell apart. It duplicated walls and rooms and just completely messed it up.

## mission_1.limitations

Honestly a majority of the outline looks wrong, I think the biggest issue was when it got to the bigger rooms. Since it didn't fully understand the room since I stuck close to the walls, it led to the scan looking like there was extra rooms/halls.

## mission_1.route.original_prediction

The robot will drive forward and enter the house. From there it will turn left, and follow the house alongside the walls so it can map out the layout of the house. It will end by the time it reaches the front door again. With this route, the robot will most likely have good map coverage for the smaller rooms, but might be weaker for the two bigger rooms/halls in the house.

## mission_1.route.prediction_draft

The robot will drive forward and enter the house. From there it will turn left, and follow the house alongside the walls so it can map out the layout of the house. It will end by the time it reaches the front door again. With this route, the robot will most likely have good map coverage for the smaller rooms, but might be weaker for the two bigger rooms/halls in the house.

## mission_2.comparison

Both routes took 7 minutes, but Mission 2 had better coverage (54% vs. 44.83%) and a higher quality score (85.8 vs. 68.3). My prediction was supported because exploring the interior first improved map quality without taking more time. Slower, careful driving can improve accuracy, but may take longer.

## mission_2.map_choice

I would trust Mission 2 more because the walls appear better aligned and there is less scattered noise. However, some areas are still unmapped, and the images and scores alone cannot prove the map is completely accurate.

## mission_2.strategy.original_prediction

For my second route, I plan to explore the interior rooms first instead of focusing on the perimeter. I'll drive slowly around corners and revisit key areas to improve map accuracy while trying to complete the map faster than my first route.

## mission_2.strategy.prediction_draft

For my second route, I plan to explore the interior rooms first instead of focusing on the perimeter. I'll drive slowly around corners and revisit key areas to improve map accuracy while trying to complete the map faster than my first route.
