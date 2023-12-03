#! /usr/bin/env python3

#Importing Python Libraries 
import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg 
import geometry_msgs.msg
import math


#Initialising the moveit Package Scenes and Command Libraries 
moveit_commander.roscpp_initialize(sys.argv)
#Initialising a node 
rospy.init_node('move_group_python_interface_tutorial', anonymous=True,)
robot = moveit_commander.RobotCommander()
scene = moveit_commander.PlanningSceneInterface()
move_group = moveit_commander.MoveGroupCommander("arm")



#Implementing Forward Kinematics using Moveit Python Script
print("-----------------PRESSS ENTER TO DISPLAY -------------")
wpose = move_group.get_current_pose().pose
tau= 2*math.pi
joint_goal = move_group.get_current_joint_values()
joint_goal[0] = tau/4
joint_goal[1] = -tau/6
joint_goal[2] = -tau/4
joint_goal[3] = 0
joint_goal[4] = tau/6

success = move_group.go(joint_goal, wait=True)
print("SUCCCESSSSSSSSSS")
print(success)


print("-----------------PRESSS ENTER-------------")
#Initialising waypoints 
waypoints = []
scale=1


print("hello I got you. Dont worry")
for i in range(0,10):
    wpose.position.z -= scale * 0.01  # First move down (z)
    waypoints.append(copy.deepcopy(wpose))


print(waypoints)
print("Waypoint Lengths")
print(len(waypoints))
#creating a plan for that
(plan, fraction) = move_group.compute_cartesian_path(
    waypoints, 0.01, 0.0  # waypoints to follow  # eef_step
)  # jump_threshold


#displaying the inverse trajectory 
display_trajectory_publisher =rospy.Publisher('/move_group/display_planned_path',moveit_msgs.msg.DisplayTrajectory,queue_size=10)
display_trajectory = moveit_msgs.msg.DisplayTrajectory()
display_trajectory.trajectory_start = robot.get_current_state()
display_trajectory.trajectory.append(plan)
# Publish the trajectory 
display_trajectory_publisher.publish(display_trajectory)
rospy.sleep(5)
print("-----------------PRESSS ENTER PATHSSSSSSS-------------")
move_group.execute(plan, wait=True)
rospy.sleep(5)
moveit_commander.roscpp_shutdown()