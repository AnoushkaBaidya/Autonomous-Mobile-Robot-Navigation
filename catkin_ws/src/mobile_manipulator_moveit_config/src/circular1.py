#! /usr/bin/env python3

import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg 
import geometry_msgs.msg
import math
import numpy as np


moveit_commander.roscpp_initialize(sys.argv)
rospy.init_node('move_group_python_interface_tutorial', anonymous=True,)
robot = moveit_commander.RobotCommander()
scene = moveit_commander.PlanningSceneInterface()
move_group = moveit_commander.MoveGroupCommander("arm")

print("-----------------PRESSS ENTER TO DISPLAY CARTESIAN PATHSSSSSSS-------------")
waypoints = []
scale=1
wpose = move_group.get_current_pose().pose
wpose.position.z -= scale * 0.1 
waypoints.append(copy.deepcopy(wpose))

wpose.position.z -= scale * 0.01 
waypoints.append(copy.deepcopy(wpose))


for i in range(0,30):
    wpose.position.z += scale * 0.01  # First move down (z)
    waypoints.append(copy.deepcopy(wpose))

print(waypoints)
print("yessss")
print(len(waypoints))
print(math.cos(60))
(plan, fraction) = move_group.compute_cartesian_path(
    waypoints, 0.01, 0.0  # waypoints to follow  # eef_step
)  # jump_threshold
#
#
#
#
display_trajectory_publisher =rospy.Publisher('/move_group/display_planned_path',moveit_msgs.msg.DisplayTrajectory,queue_size=10)
display_trajectory = moveit_msgs.msg.DisplayTrajectory()
display_trajectory.trajectory_start = robot.get_current_state()
display_trajectory.trajectory.append(plan)
# Publish
display_trajectory_publisher.publish(display_trajectory)
rospy.sleep(5)
print("-----------------PRESSS ENTER PATHSSSSSSS-------------")
move_group.execute(plan, wait=True)
rospy.sleep(5)
rospy.sleep(5)

moveit_commander.roscpp_shutdown()