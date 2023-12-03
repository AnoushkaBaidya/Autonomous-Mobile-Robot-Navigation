#!/usr/bin/env python3

import numpy as np
import time
import math
import rospy
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
import sys
import copy
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

display_trajectory_publisher = rospy.Publisher('/move_group/display_planned_path', moveit_msgs.msg.DisplayTrajectory, queue_size=20)
wpose = move_group.get_current_pose().pose


def talker():
    while not rospy.is_shutdown():
        r = 0.09
        angle = 0 
        for angle in np.arange(0,3.1415,0.314):
            z = 0.1
            x = r*math.cos(angle)
            y = r*math.sin(angle)
            go_goal(wpose.position.x + x ,wpose.position.y + y,wpose.position.z + z)
            print('done')


def go_goal(x,y,z):
    pose_goal = geometry_msgs.msg.Pose()
    pose_goal.orientation.w = 1.0
    pose_goal.position.x = x
    pose_goal.position.y = y
    pose_goal.position.z = z
    move_group.set_pose_target(pose_goal)
    print("starting plan")
    print(pose_goal)
    plan = move_group.go(wait=True)
    # move_group.execute(plan, wait=True)
    # Calling `stop()` ensures that there is no residual movement
    move_group.stop()
    # It is always good to clear your targets after planning with poses.
    # Note: there is no equivalent function for clear_joint_value_targets()
    move_group.clear_pose_targets()


if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
