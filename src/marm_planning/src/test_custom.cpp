//给定期望的ur5末端执行器的位置和姿态，在笛卡尔空间上控制ur5

// 包含miveit的API头文件
#include <moveit/move_group_interface/move_group_interface.h>

int main(int argc, char **argv)
{
  ros::init(argc, argv, "moveit_custom_demo");
  ros::NodeHandle node_handle; 
  ros::AsyncSpinner spinner(1);
  spinner.start();

  moveit::planning_interface::MoveGroupInterface group("manipulator");

  // 设置机器人终端的目标位置
  geometry_msgs::Pose target_pose1;
  target_pose1.orientation.w = 0.026282;
  target_pose1.orientation.x= 0.04423e-07;
  target_pose1.orientation.y = -0.087396;
  target_pose1.orientation.z = 0.01813e-07;

  target_pose1.position.x = 0.5;
  target_pose1.position.y = 0.5;
  target_pose1.position.z = 0.6;
  group.setPoseTarget(target_pose1);

  // 进行运动规划，计算机器人移动到目标的运动轨迹，此时只是计算出轨迹，并不会控制机械臂运动
  moveit::planning_interface::MoveGroupInterface::Plan my_plan;
  moveit::planning_interface::MoveItErrorCode success = group.plan(my_plan);

  ROS_INFO("Visualizing plan 1 (pose goal) %s",success?"":"FAILED");   

  //让机械臂按照规划的轨迹开始运动。
  if(success)
      group.execute(my_plan);

  ros::shutdown(); 
  return 0;
}
