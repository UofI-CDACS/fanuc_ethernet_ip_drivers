"""! @brief Defines the robot controller class."""

##
# @file robot_controller.py
#
# @brief Defines the roboot controller class.
#
# @section description_robot_controller Description
# Defines the base and end user class for controlling robot using FANUC-EthernetIP library
#
# @section todo_robot_controller todo_robot_controller
# - Add cartesian functions
# - Update/Modify/Refactor all functions for clarity and use
# - Add more useful functions
# -
# - Function Ideas:
# - Move robot function: Moves robot and checks register until finished
# 
# @section author_robot_controller Authors(s)
# - Original Code by John Shovic
# - Modified by James Lasso on 6/12/2023

# Imports
import sys
sys.path.append('./pycomm3/pycomm3')
import struct
import random
import time
import FANUCethernetipDriver

FANUCethernetipDriver.DEBUG = False

class robot:
    def __init__(self, robotIP):
        self.robot_IP = robotIP
        self.CurJointPosList = FANUCethernetipDriver.returnJointCurrentPosition(self.robot_IP)
        self.CurCartesianPosList = FANUCethernetipDriver.returnCartesianCurrentPostion(self.robot_IP)
        self.PRNumber = 1 # This is the position register for holding coordinates

    ##
    #
    # Joint movement functions
    #
    ##

    # read CURPOS from Robot
    def read_current_joint_position(self):
        print("-----------------------------------------")
        print(" Read current position from Robot")
        print("-----------------------------------------")
        self.CurJointPosList = FANUCethernetipDriver.returnJointCurrentPosition(self.robot_IP)
        print("CURPOS=", self.CurJointPosList)

    # read PR[1] Joint Coordinates
    def read_joint_position_register(self):
        print("------------------------")
        print(" read PR[1] Joint Coordinate")
        print("------------------------")
        PRNumber = 1
        PR_1_Value = FANUCethernetipDriver.readJointPositionRegister(self.robot_IP, self.PRNumber)
        print("PR[%d]"% self.PRNumber)
        print("list=", PR_1_Value)

    # write PR[1] offset
    def write_joint_offset(self, joint, value):
        print("------------------------")
        print(" write PR[1] Joint Coordinate")
        print("------------------------")
        joint = joint + 1

        newPosition = self.CurJointPosList[joint] + value

        self.CurJointPosList[joint] = newPosition

        myList = self.CurJointPosList

        W_PR_1_return = FANUCethernetipDriver.writeJointPositionRegister(self.robot_IP, self.PRNumber, myList)

        # print("W_PR_1_return =", W_PR_1_return)

    # write PR[1] Joint value
    def write_joint_position(self, joint, value):
        print("------------------------")
        print(" write PR[1] Joint Coordinate")
        print("------------------------")
        joint = joint + 1

        newPosition = value

        self.CurJointPosList[joint] = newPosition

        myList = self.CurJointPosList

        W_PR_1_return = FANUCethernetipDriver.writeJointPositionRegister(self.robot_IP, self.PRNumber, myList)

        # print("W_PR_1_return =", W_PR_1_return)

    # Put robot in home position
    def set_joints_to_home_position(self):
        print("----------------------------------")
        print(" Robot Returning to Home Position ")
        print("----------------------------------")

        # Set positions DO NOT USE 0
        # joint coordinates start at list item 2, ie: Joint2 = CurPosList[3]
        self.CurJointPosList[2] = 1.0 # J1
        self.CurJointPosList[3] = 1.0 # J2
        self.CurJointPosList[4] = 1.0 # J3
        self.CurJointPosList[5] = 1.0 # J4
        self.CurJointPosList[6] = 1.0 # J5 PB50IB does not like this join, OK on CRX10
        self.CurJointPosList[7] = 1.0 # J6

        myList = self.CurJointPosList

        W_PR_1_return = FANUCethernetipDriver.writeJointPositionRegister(self.robot_IP, self.PRNumber, myList)

        # print("W_PR_1_return =", W_PR_1_return)

    ##
    #
    # Cartesian Movement Functions
    #
    ##

    # read current cartesian position from Robot
    def read_current_cartesian_position(self):
        print("------------------------")
        print(" read CURPOS from Robot")
        print("------------------------")
        CurPosList = FANUCethernetipDriver.returnCartesianCurrentPostion(self.robot_IP)

        print("CURPOS=", CurPosList)

    # read PR[1] Cartesian Coordinates
    def read_cartesian_position_register(self):
        print("------------------------")
        print(" read PR[1] Cartesian Coordinate")
        print("------------------------")

        PR_1_Value = FANUCethernetipDriver.readCartesianPositionRegister(self.robot_IP, self.PRNumber)
        print("PR[%d]"% self.PRNumber)
        print("list=", PR_1_Value)

    # write PR[1] Cartesian Coordinates
    #def write_cartesian_coordinates(self):
    #    print("------------------------")
    #    print(" write PR[1] Cartesian Coordinate")
    #    print("------------------------")

    #    newZ = CurPosList[4]+random.randrange(-50.0, 50)

    #    CurPosList[4] = newZ
    #    print("CURPOS(Zoffset)=", CurPosList)

    #    myList = CurPosList

    #    W_PR_1_return = FANUCethernetipDriver.writeCartesianPositionRegister(self.robot_IP, self.PRNumber, myList)

    #    print("W_PR_1_return =", W_PR_1_return)

    ##
    #
    # Utility Functions
    #
    ##

    # write R[5] to set Speed in mm/sec
    def set_speed(self, value):
        speedRegister = 5 # R[5]
        print("------------------------")
        print(" Speed set to {value}mm/sec")
        print("------------------------")
        W_R_5_return = FANUCethernetipDriver.writeR_Register(self.robot_IP, speedRegister, value)

        # print ("W_R_5_return=",W_R_5_return)


    # write R[1] to start Robot
    def start_robot(self):  
        print("------------------------")
        print(" write R[1] to move arm ")
        print("------------------------")

        RegNum = 1 # This register is used to start the robot when set to 1
        Value = 1
        W_R_2_return = FANUCethernetipDriver.writeR_Register(self.robot_IP, RegNum, Value)

        # print ("W_R_2_return=",W_R_2_return)

        print("******************************")
        print(" Moving Joint(s) to Position")
        print("******************************")
        # Wait till robot is done moving
        moving = self.read_robot_start_register()
        while(moving):
            moving = self.read_robot_start_register()

        # Signal end of move action
        print("*************************")
        print(" Joint Move Complete")
        print("*************************")

    # read R[1]
    def read_robot_start_register(self):
        #print("------------------------")
        #print(" read R[1] Register")
        #print("------------------------")

        RegNum = 1

        R_R_2_return = FANUCethernetipDriver.readR_Register(self.robot_IP, RegNum)
        return R_R_2_return
        #print ("R_R_2_return=",R_R_2_return)

    # Control conveyor belt
    def conveyor(self, command):

        #R21 is forward
        #R22 is reverse
        forward_register = 21
        reverse_register = 22
        on = 1
        off = 0
        sync_register = 2
        sync_value = 1

        if command == 'forward':
            # Make sure belt is not moving
            W_R_21_return = FANUCethernetipDriver.writeR_Register(self.robot_IP, reverse_register, off)
            W_R_20_return = FANUCethernetipDriver.writeR_Register(self.robot_IP, forward_register, off)
            W_R_2_return = FANUCethernetipDriver.writeR_Register(self.robot_IP, sync_register, sync_value)

            print("------------------------")
            print("Moving Conveyor Forward")
            print("------------------------")

            W_R_20_return = FANUCethernetipDriver.writeR_Register(self.robot_IP, forward_register, on)
            ## Set sync bit to update
            W_R_2_return = FANUCethernetipDriver.writeR_Register(self.robot_IP, sync_register, sync_value)
        elif command == 'reverse':
            W_R_21_return = FANUCethernetipDriver.writeR_Register(self.robot_IP, reverse_register, off)
            W_R_20_return = FANUCethernetipDriver.writeR_Register(self.robot_IP, forward_register, off)
            W_R_2_return = FANUCethernetipDriver.writeR_Register(self.robot_IP, sync_register, sync_value)

            print("------------------------")
            print("Moving Conveyor in Reverse")
            print("------------------------")

            W_R_21_return = FANUCethernetipDriver.writeR_Register(self.robot_IP, reverse_register, on)
            ## Set sync bit to update
            W_R_2_return = FANUCethernetipDriver.writeR_Register(self.robot_IP, sync_register, sync_value)
        elif command == 'stop':
            print("------------------------")
            print("Stopping conveyor Belt")
            print("------------------------")
            W_R_21_return = FANUCethernetipDriver.writeR_Register(self.robot_IP, reverse_register, off)
            W_R_20_return = FANUCethernetipDriver.writeR_Register(self.robot_IP, forward_register, off)
            ## Set sync bit to update
            W_R_2_return = FANUCethernetipDriver.writeR_Register(self.robot_IP, sync_register, sync_value)
        else:
            W_R_21_return = FANUCethernetipDriver.writeR_Register(self.robot_IP, reverse_register, off)
            W_R_20_return = FANUCethernetipDriver.writeR_Register(self.robot_IP, forward_register, off)
            ## Set sync bit to update
            W_R_2_return = FANUCethernetipDriver.writeR_Register(self.robot_IP, sync_register, sync_value)

            









