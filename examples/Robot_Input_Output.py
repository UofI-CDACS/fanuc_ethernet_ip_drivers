import sys
sys.path.append('../src')

import FANUCethernetipDriver as EIP
from robot_controller import robot

drive_path = '172.29.208.124' # Beaker

"""
This is a test to read the Robot Input/Output registers, RI[] & RO[] 
"""
# Read in a list of inputs
inputList = EIP.readRobotInputs(drive_path)
print("Returned list")
print(inputList)

# Read in 1 input
print("input 1: ", EIP.readRobotInput(drive_path, 1)) # RI[1] Schunk Gripper off
print("input 2: ", EIP.readRobotInput(drive_path, 2)) # RI[2] Schunk Gripper on

print("output 5: ", EIP.readRobotOutput(drive_path, 5)) # RO[5]
