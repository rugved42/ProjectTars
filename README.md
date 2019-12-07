# ProjectTars
This project deals with simulation in Autowrare and Carla. The repository built above has taken the required files from final assignemnt of coursera's Autonomous Driving Vehicle simulation. We used those files to run the simulation on Carla. on the top of the coursera's project files we built the collision checker.py file which would help the vehicle avoid obstacle. The possible number of paths are calculated in the coursera's file, we simulated the parked vahicles in Carla and used them as obstacle. The global path is given from the autoware OpenPlanner using Rviz visualizer. The waypoints created through that file are acessed in Carla Simulator.

Obstacle Avoidance: 

The Possible number of paths a car can take is provided through Coursera's project, Once we simulate the obstacle in the path on which we are running the vehicle, the possible number of paths a car can take to avoid obstacle is then searched. The best one is chosen by calculating the distance between the points covering the obstacle and the possible path a vehicle can take also the current lane and the possible path. The best one is chosen as " The path which is at the shortest distance from the curent path and farthest distance from the obstacle". This is done by just calculating the euclidean ditance between the available point and obstacle point. 

Refer to videos here: 

https://youtu.be/puOrnJJhpXE  Autoware Demo Data Running
https://youtu.be/y5Ca-Ql_FAY  OpenPlanner on Aufoware. 
https://youtu.be/IlybENfTtZM  Carla Simulation.  
