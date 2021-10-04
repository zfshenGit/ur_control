#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import rospy, sys
import moveit_commander
from moveit_msgs.msg import RobotTrajectory
from trajectory_msgs.msg import JointTrajectoryPoint

from geometry_msgs.msg import PoseStamped, Pose
from tf.transformations import euler_from_quaternion, quaternion_from_euler

class MoveItIkDemo:
    def __init__(self):
        # 初始化move_group的API
        moveit_commander.roscpp_initialize(sys.argv)
        
        # 初始化ROS节点
        rospy.init_node('moveit_ik_demo')
                
        # 初始化需要使用move group控制的机械臂中的arm group
        manipulator = moveit_commander.MoveGroupCommander('manipulator')
                
        # 获取终端link的名称
        end_effector_link = manipulator.get_end_effector_link()
                        
        # 设置目标位置所使用的参考坐标系
        reference_frame = 'base_link'
        manipulator.set_pose_reference_frame(reference_frame)
                
        # 当运动规划失败后，允许重新规划
        manipulator.allow_replanning(True)
        
        # 设置位置(单位：米)和姿态（单位：弧度）的允许误差
        manipulator.set_goal_position_tolerance(0.01)
        manipulator.set_goal_orientation_tolerance(0.05)
        
        # 控制机械臂先回到初始化位置
        #manipulator.set_named_target('home')
        #manipulator.go()
        #rospy.sleep(2)
               
        # 设置机械臂工作空间中的目标位姿，位置使用x、y、z坐标描述，
        # 姿态使用四元数描述，基于base_link坐标系
        target_pose = PoseStamped()
        target_pose.header.frame_id = reference_frame
        target_pose.header.stamp = rospy.Time.now()     
        target_pose.pose.position.x = 0.5
        target_pose.pose.position.y = 0.5
        target_pose.pose.position.z = 0.5
        target_pose.pose.orientation.x = 0.011822
        target_pose.pose.orientation.y = -0.0269758
        target_pose.pose.orientation.z = 0.005694
        target_pose.pose.orientation.w = -0.003653
        
        # 设置机器臂当前的状态作为运动初始状态
        manipulator.set_start_state_to_current_state()
        
        # 设置机械臂终端运动的目标位姿
        manipulator.set_pose_target(target_pose, end_effector_link)
        
        # 规划运动路径
        traj = manipulator.plan()
        
        # 按照规划的运动路径控制机械臂运动
        manipulator.execute(traj)
        rospy.sleep(1)
         
        # 控制机械臂终端向右移动5cm
        #manipulator.shift_pose_target(1, -0.05, end_effector_link)
        #manipulator.go()
        #rospy.sleep(1)
  
        # 控制机械臂终端反向旋转90度
        #manipulator.shift_pose_target(3, -1.57, end_effector_link)
        #manipulator.go()
        #rospy.sleep(1)
           
        # 控制机械臂回到初始化位置
        #manipulator.set_named_target('home')
        #manipulator.go()

        # 关闭并退出moveit
        moveit_commander.roscpp_shutdown()
        moveit_commander.os._exit(0)

if __name__ == "__main__":
    MoveItIkDemo()

    
    
