# ur_control
Ur5 Control About Peg-In-Hole 

Computer Operation System:Linux Ubuntu 18.04

ROS:melodic

__Usage__

First of all, compile workspace：

```catkin_make```

___1.1 With real Hardware___

To bring up the real robot, run in the workspace root:

```source devel/setup.bash```

```roslaunch ur_bringup ur5_bringup.launch robot_ip:=IP_OF_THE_ROBOT [reverse_port:=REVERSE_PORT]```

replace `IP_OF_THE_ROBOT ` with `XXX.XXX.XXX.XXX`, depending on which IP address you have set.

CAUTION:  
Remember that you should always have your hands on the big red button in case there is something in the way or anything unexpected happens.

___1.2 MoveIt! with real Hardware___  

Additionally, you can use MoveIt! to control the robot.  
There exist MoveIt! configuration packages for both robots.  

For setting up the MoveIt! nodes to allow motion planning, open a new terminal and run in the workspace root :

```source devel/setup.bash```

```roslaunch ur5_moveit_config ur5_moveit_planning_execution.launch```

For starting up RViz with a configuration including the MoveIt! Motion Planning plugin, open a new terminal and run in the workspace root :

```source devel/setup.bash```

```roslaunch ur5_moveit_config moveit_rviz.launch config:=true```

___1.3 Programming in Python or c++___

Then,you can control ur5 via programming with Python or c++

When you use python to control ur5 to a given position and attitude in Cartesian space,  open a new terminal and run in the workspace root :

```source devel/setup.bash```

```rosrun marm_planning moveit_ik_demo.py```

When you use c++ to control ur5 to a given position and attitude in Cartesian space, open a new terminal and run in the workspace root :

```catkin_make```

```source devel/setup.bash```

```rosrun marm_planning test_custom_node```

___2.1 Usage with Gazebo Simulation___  

To bring up the simulated robot in Gazebo, run in the workspace root:

```source devel/setup.bash```

```roslaunch ur_gazebo ur5.launch```


___2.2 MoveIt! with a simulated robot___  

Again, you can use MoveIt! to control the simulated robot.  

For setting up the MoveIt! nodes to allow motion planning, open a new terminal and run in the workspace root :

```source devel/setup.bash```

```roslaunch ur5_moveit_config ur5_moveit_planning_execution.launch sim:=true```

For starting up RViz with a configuration including the MoveIt! Motion Planning plugin, open a new terminal and run in the workspace root :

```source devel/setup.bash```

```roslaunch ur5_moveit_config moveit_rviz.launch config:=true```

___2.3 Programming in Python or c++___

Then,you can control ur5 via programming with Python or c++

When you use python to control ur5 to a given position and attitude in Cartesian space,  open a new terminal and run in the workspace root :

```source devel/setup.bash```

```rosrun marm_planning moveit_ik_demo.py```

When you use c++ to control ur5 to a given position and attitude in Cartesian space, open a new terminal and run in the workspace root :

```catkin_make```

```source devel/setup.bash```

```rosrun marm_planning test_custom_node```
