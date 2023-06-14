"""! @brief Defines the robot controller class."""

##
# @file robot_controller.py
#
# @brief Defines the roboot controller class
#
# @section description_robot_controller Description
# Defines the base and end user class for controlling robot using FANUC-EthernetIP library
#
# @section todo_robot_controller todo_robot_controller
# - Add other functions
# 
# @section author_robot_controller Authors(s)
# - Created by James Lasso on 6/12/2023

# Imports
import sys
sys.path.append('./pycomm3/pycomm3')
import struct
import random
import time
import FANUCethernetipDriver

class robot:
    def __init__(self, robotIP):
        self.robot_IP = robotIP
        self.CurPosList = FANUCethernetipDriver.returnJointCurrentPosition(self.robot_IP)

    # read CURPOS from Robot
    def read_current_position(self):
        print("-----------------------------------------")
        print(" Read current position from Robot")
        print("-----------------------------------------")
        CurPosList = FANUCethernetipDriver.returnJointCurrentPosition(self.robot_IP)
        print("CURPOS=", CurPosList)

    # read PR[1] Joint Coordinates
    def read_joint_coordinates(self):
        print("------------------------")
        print(" read PR[1] Joint Coordinate")
        print("------------------------")
        PRNumber = 1
        PR_1_Value = FANUCethernetipDriver.readJointPositionRegister(self.robot_IP, PRNumber)
        print("PR[%d]"% PRNumber)
        print("list=", PR_1_Value)

    # write PR[1] offset
    def write_joint_offset(self, joint, value):
        print("------------------------")
        print(" write PR[1] Joint Coordinate")
        print("------------------------")
        joint = joint + 1

        newPosition = self.CurPosList[joint] + value

        self.CurPosList[joint] = newPosition

        PRNumber = 1
        myList = self.CurPosList

        W_PR_1_return = FANUCethernetipDriver.writeJointPositionRegister(self.robot_IP, PRNumber, myList)

        print("W_PR_1_return =", W_PR_1_return)

    # write PR[1] Joint value
    def write_joint_position(self, joint, value):
        print("------------------------")
        print(" write PR[1] Joint Coordinate")
        print("------------------------")
        joint = joint + 2

        newPosition = value

        self.CurPosList[joint] = newPosition

        PRNumber = 1
        myList = self.CurPosList

        W_PR_1_return = FANUCethernetipDriver.writeJointPositionRegister(self.robot_IP, PRNumber, myList)

        print("W_PR_1_return =", W_PR_1_return)
    
    # write R[5] to set Speed in mm/sec
    def set_speed(self, value):
        speedRegister = 5 # R[5]
        print("------------------------")
        print(" Speed set to {value}mm/sec")
        print("------------------------")
        W_R_5_return = FANUCethernetipDriver.writeR_Register(self.robot_IP, speedRegister, Value)

        print ("W_R_5_return=",W_R_5_return)


    # write R[1] to start Robot
    def start_robot(self):  
        print("------------------------")
        print(" write R[1] to move arm ")
        print("------------------------")

        RegNum = 1
        Value = 1
        W_R_2_return = FANUCethernetipDriver.writeR_Register(self.robot_IP, RegNum, Value)

        print ("W_R_2_return=",W_R_2_return)


    # read R[1]
    def read_robot_start_register(self):
        print("------------------------")
        print(" read R[1] Register")
        print("------------------------")

        RegNum = 1

        R_R_2_return = FANUCethernetipDriver.readR_Register(self.robot_IP, RegNum)
        return R_R_2_return
        #print ("R_R_2_return=",R_R_2_return)

    # Put robot in home position
    def set_joints_to_home_position(self):
        print("----------------------------------")
        print(" Robot Returning to Home Position ")
        print("----------------------------------")

        # Set positions DO NOT USE 0
        self.CurPosList[3] = 1.0 # J1
        self.CurPosList[4] = 1.0 # J2
        self.CurPosList[5] = 1.0 # J3
        self.CurPosList[6] = 1.0 # J4
        self.CurPosList[7] = 1.0 # J5
        self.CurPosList[8] = 1.0 # J6

        PRNumber = 1
        myList = self.CurPosList

        W_PR_1_return = FANUCethernetipDriver.writeJointPositionRegister(self.robot_IP, PRNumber, myList)

        print("W_PR_1_return =", W_PR_1_return)
