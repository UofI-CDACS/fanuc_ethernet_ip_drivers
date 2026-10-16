import sys
sys.path.append('../src')
from robot_controller import robot
from CartesianPosition import CartesianPosition
from JointPosition import JointPosition
from typing import NamedTuple
import time
import FANUCethernetipDriver as EIP
import copy






# NOTE: The robot I.P. is required.
ROBOT_IP = "10.1.1.31"
crx10 = robot(ROBOT_IP)
crx10.set_speed(90) # mm per second


# Example : Moving to a hardcoded joint position.
# NOTE : It is reccommended to reser the robot to a hardcoded joint position before and after running a program.
RECALIBRATION_POSITION = JointPosition(
    j1=0,
    j2=0,
    j3=0,
    j4=0,
    j5=-90,
    j6=0
).move_to(crx10)


# Example : Moving to a hardcoded cartesian position.
EXAMPLE_CART_1 = CartesianPosition(
    X=740,
    Y=-150,
    Z=550,
    W=-179,
    P=0,
    R=0
).move_to(crx10)



# Example :  Read Current Cartesian pose
print(f" Current Robot Cartesian Pose : {CartesianPosition.get_current(crx10)}")


# Example :  Read Current Joint pose
print(f" Current Robot Joint Pose : {JointPosition.get_current(crx10)}")


# Example : Conveyor Sensing Logic
right = crx10.conveyor_proximity_sensor("right")
left = crx10.conveyor_proximity_sensor("left")
print(f"The Left Conveyor Proximity Sesnor is {left}")
print(f"The Right Conveyor Proximity Sesnor is {right}")


# Example : Turn on conveyor for a little bit.
crx10.conveyor("reverse")
time.sleep(0.5)
crx10.conveyor("stop")
time.sleep(0.5)
crx10.conveyor("forward")
time.sleep(0.5)
crx10.conveyor("stop")



# Example : The OnRobot Grabber
crx10.onRobot_gripper(
    150, # Width
    80, # force
    wait=True
)
time.sleep(1)


# Example : The Shunk Grabber
crx10.schunk_gripper('open')
time.sleep(1)
crx10.schunk_gripper('close')
time.sleep(1)
crx10.schunk_gripper('open')
time.sleep(1)