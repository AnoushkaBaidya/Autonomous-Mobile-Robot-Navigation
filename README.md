# Autonomous-Mobile-Robot-Navigation
Mobile Robot Navigation and Manipulation
# Mobile Robot Navigation and Manipulation


This project involves the design and simulation of a mobile robot capable of navigating through a complex simulated environment and manipulating objects. The main application of this project is in the field of warehouse automation, where the robot can navigate through a warehouse, pick up items, and deliver them to their desired locations.

### 1. Mobile Robot Base
Downloaded the mesh files of the robot base, which consists of four wheels and a base.
Created a Robot base URDF file defining the base, wheels, and 4 interlinking joints.
Added the configuration and control files for the robot base.
Created launch files to visualize the base in the Gazebo simulation environment.
Implemented a GUI to control the robot base using velocity commands.

![base](https://github.com/upasana099/Autonomous-Navigation-of-Mobile-Manipulator/assets/89516193/47be5231-27ac-4bb8-8c66-add1c1eefd47)



### 2. Mobile Robot Arm
Downloaded mesh files of the robot arm, which consists of 5 links.
Modified the end effector using Solidworks to incorporate a cylinder for wheel rotation.
Created a Robot arm URDF file defining the base, links, and 5 interlinking joints.
Added the configuration and control files for the robot arm.
Created launch files to visualize the arm in the Gazebo simulation environment.
Combined the base and arm to launch them together in Gazebo.

![arm](https://github.com/upasana099/Autonomous-Navigation-of-Mobile-Manipulator/assets/89516193/c82bd995-21b0-4a9d-b9e3-4c7cc8dd4fa1)


### 3. Forward Kinematics
Developed a Python script to compute the forward kinematics of the mobile robot arm.
Created a service-client node to request joint angle values and publish them to the robot joints.
### 4. World File
Downloaded a post office world file environment and visualized it in Gazebo using a launch file.
Created a launch file to visualize the robot and the world together in Gazebo.

![aaaa](https://github.com/upasana099/Autonomous-Navigation-of-Mobile-Manipulator/assets/89516193/075b8847-9253-4020-8367-97893a2d896b)


### 5. Navigation Stack


**5.1 LIDAR**


Added a LIDAR to scan the robot's surroundings.
Edited the URDF file to incorporate the LIDAR for better performance and used a Gazebo plugin.


**5.2 Configuring Parameters for ROS Navigation**


Configured two costmaps: Global Costmap for long-term goals and Local Costmap for short-term goals like obstacle avoidance.


**5.3 Mapping The Environment**


Built a map of the environment using Hector Slam with laser scanner data.
Saved the map in the ROS directory and visualized it.
Iteratively refined the map until the desired representation of the environment was achieved.

![map](https://github.com/upasana099/Autonomous-Navigation-of-Mobile-Manipulator/assets/89516193/40e0f300-32a2-4ca4-8e03-5f235ad8423b)


**5.4 EKF Package**


Added an inertial measurement unit to improve localization accuracy.
Set up the robot_pose_ekf package, which utilizes an extended Kalman Filter for pose estimation.


**5.5 AMCL Package**


Implemented the AMCL (Adaptive Monte Carlo Localization) package for probabilistic localization in a 2D plane.


**5.6 Script**


Created a C++ script for autonomous robot movement.
Defined goal points for the robot to reach.
Enabled obstacle avoidance while following the planned path.


### 6. Object Creation
Modeled the wheel and switch using Solidworks.
Created URDF and launch files to spawn the objects in the Gazebo environment.
Adjusted dynamic properties and redesigned the objects to ensure proper spawning.

![obj](https://github.com/upasana099/Autonomous-Navigation-of-Mobile-Manipulator/assets/89516193/90baad05-c201-4b68-9970-e48319eed63c)



### 7. Motion Planning of Robot Arm
Configured a robotic arm using MoveIt for planning groups, end effectors, ROS control, and path planning algorithms.
Utilized a GUI to define poses and plan trajectories from one pose to another.
Developed a Python script to execute the desired trajectory.
Implemented forward and inverse kinematics for the robot arm.


![rviz2](https://github.com/upasana099/Autonomous-Navigation-of-Mobile-Manipulator/assets/89516193/f2b2660b-2203-4e37-b0f6-902a04723e48)



### Simulation Results
The robot successfully lifted the switch.
Due to the weight of the switch, it exerted force on the manipulator and pushed the robot backward.


![ddd](https://github.com/upasana099/Autonomous-Navigation-of-Mobile-Manipulator/assets/89516193/c8fdd40d-8947-4ea1-a548-d21188ef8233)

