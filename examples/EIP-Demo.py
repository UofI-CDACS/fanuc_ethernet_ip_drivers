#!/usr/bin/env python3
'''
This was the example code from Robotics 1 in Spring 2024 
demoing simple commands to the robot.
Last updated 2/1/2024 by Kris Olds
'''

import sys
sys.path.append("Your/Path/To /fanuc_ethernet_ip_drivers/src")
from robot_controller import robot
from time import sleep

robot_ip = '172.29.208.124' # Beaker
# robot_ip = '172.29.208.123 # Bunsen

theRobot = robot(robot_ip)

cartPose = theRobot.read_current_cartesian_pose()
print(cartPose)

theRobot.write_cartesian_position(-600.0, -200.0, -80.0, cartPose[3], cartPose[4],cartPose[5])
theRobot.start_robot()

cartPose = theRobot.read_current_cartesian_pose()
print(cartPose)

theRobot.conveyor('forward')
sleep(5) # Wait for 5 seconds
theRobot.conveyor('stop')
