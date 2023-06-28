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
# - Add more useful functions
# -
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
        self.sync_register = 2
        self.sync_value = 1

    ##
    #
    # Joint movement functions
    #
    ##

    # read CURPOS from Robot
    def read_current_joint_position(self):
        print("------------------------------------")
        print("| Read current position from Robot |")
        print("------------------------------------")
        self.CurJointPosList = FANUCethernetipDriver.returnJointCurrentPosition(self.robot_IP)
        print("CURPOS=", self.CurJointPosList)

    # read PR[1] Joint Coordinates
    def read_joint_position_register(self):
        # print("------------------------")
        # print(" read PR[1] Joint Coordinate")
        # print("------------------------")
        PRNumber = 1
        PR_1_Value = FANUCethernetipDriver.readJointPositionRegister(self.robot_IP, self.PRNumber)
        print("PR[%d]"% self.PRNumber)
        print("list=", PR_1_Value)

    # write PR[1] offset
    def write_joint_offset(self, joint, value):
        print("***********************************************")
        print(f" Write Joint Offset Value:[{value}] to Joint:[{joint}] ")
        print("***********************************************")
        joint = joint + 1

        newPosition = self.CurJointPosList[joint] + value

        self.CurJointPosList[joint] = newPosition

        myList = self.CurJointPosList

        W_PR_1_return = FANUCethernetipDriver.writeJointPositionRegister(self.robot_IP, self.PRNumber, myList)

        # print("W_PR_1_return =", W_PR_1_return)

    # write PR[1] Joint value
    def write_joint_position(self, joint, value):
        print("--------------------------------")
        print("| write PR[1] Joint Coordinate |")
        print("--------------------------------")
        joint = joint + 1

        newPosition = value

        self.CurJointPosList[joint] = newPosition

        myList = self.CurJointPosList

        W_PR_1_return = FANUCethernetipDriver.writeJointPositionRegister(self.robot_IP, self.PRNumber, myList)

        # print("W_PR_1_return =", W_PR_1_return)

    # Put robot in home position
    def set_joints_to_home_position(self):
        print("*************************************************")
        print("* Setting Joint Positions to Home Configuration *")
        print("*************************************************")

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

    ##
    #
    # Cartesian Movement Functions
    #
    ##

    # read current cartesian position from Robot
    def read_current_cartesian_position(self):
        print("--------------------------")
        print("| read CURPOS from Robot |")
        print("--------------------------")
        CurPosList = FANUCethernetipDriver.returnCartesianCurrentPostion(self.robot_IP)

        print("CURPOS=", CurPosList)

    # read PR[1] Cartesian Coordinates
    def read_cartesian_position_register(self):
        print("-----------------------------------")
        print("| read PR[1] Cartesian Coordinate |")
        print("-----------------------------------")

        PR_1_Value = FANUCethernetipDriver.readCartesianPositionRegister(self.robot_IP, self.PRNumber)
        print("PR[%d]"% self.PRNumber)
        print("list=", PR_1_Value)

    # write PR[1] Cartesian Coordinates
    def write_cartesian_coordinates(self, newX, newY, newZ):
        self.CurCartesianPosList[2] = newX
        self.CurCartesianPosList[3] = newY
        self.CurCartesianPosList[4] = newZ
        
        print("------------------------")
        print(" write PR[1] Cartesian Coordinate")
        print("------------------------")

        newPositionList = self.CurCartesianPosList

        W_PR_1_return = FANUCethernetipDriver.writeCartesianPositionRegister(self.robot_IP, self.PRNumber, newPositionList)

    ##
    #
    # Utility Functions
    #
    ##

    # write R[5] to set Speed in mm/sec
    def set_speed(self, value):
        speedRegister = 5 # R[5]
        print("------------------------------")
        print(f"| Speed set to {value}mm/sec |")
        print("------------------------------")
        W_R_5_return = FANUCethernetipDriver.writeR_Register(self.robot_IP, speedRegister, value)

        # print ("W_R_5_return=",W_R_5_return)


    # write R[1] to start Robot
    def start_robot(self):  
        # Old printout, not needed
        # print("------------------------")
        # print(" write R[1] to move arm ")
        #print("------------------------")

        RegNum = 1 # This register is used to start the robot when set to 1
        Value = 1
        W_R_2_return = FANUCethernetipDriver.writeR_Register(self.robot_IP, RegNum, Value)

        # print ("W_R_2_return=",W_R_2_return)

        # Wait till robot is done moving
        moving = self.read_robot_start_register()
        while(moving):
            moving = self.read_robot_start_register()

        # Signal end of move action
        print("********************************************")
        print("* Moving Joint(s) to Position(s): COMPLETE *")
        print("********************************************")

    # Put CRX10 in a mount position to change end tooling
    # !!! -- THIS JOIN CONFIGURATION IS FOR THE CRX10 ROBOT -- !!!
    def set_joints_to_mount_position(self):
        print("**************************************************")
        print("* Setting Joint Positions to Mount Configuration *")
        print("**************************************************")

        # Set positions DO NOT USE 0
        # joint coordinates start at list item 2, ie: Joint2 = CurPosList[3]
        self.CurJointPosList[2] = 1.0 # J1
        self.CurJointPosList[3] = 58.0 # J2
        self.CurJointPosList[4] = -12.0 # J3
        self.CurJointPosList[5] = -2.0 # J4
        self.CurJointPosList[6] = 11.0 # J5 PB50IB does not like this join, OK on CRX10
        self.CurJointPosList[7] = -6.0 # J6

        myList = self.CurJointPosList

        W_PR_1_return = FANUCethernetipDriver.writeJointPositionRegister(self.robot_IP, self.PRNumber, myList)
        # print("W_PR_1_return =", W_PR_1_return)

    # read R[1]
    def read_robot_start_register(self):
        #print("------------------------")
        #print(" read R[1] Register")
        #print("------------------------")

        RegNum = 1

        R_R_2_return = FANUCethernetipDriver.readR_Register(self.robot_IP, RegNum)
        return R_R_2_return
        #print ("R_R_2_return=",R_R_2_return)

    # NOT CURRENTLY WORKING
    def gripper(self, command):
        # Register number for the gripper
        gripperReg = 20
        sync_register = 2
        sync_value = 1

        # Get current gripper state
        gripper_open = FANUCethernetipDriver.readR_Register(self.robot_IP, gripperReg)
        print(f"Gripper Register Value: {gripper_open}")
        open_status = FANUCethernetipDriver.readR_Register(self.robot_IP, 32)
        print(f"Grippen open status: {open_status}\n")
        closed_status = FANUCethernetipDriver.readR_Register(self.robot_IP, 33)
        print(f"Grippen closed status: {closed_status}\n")

        if command == 'open':
            print("Opening Gripper...\n")
            FANUCethernetipDriver.writeR_Register(self.robot_IP, 20, 0)
            W_R_2_return = FANUCethernetipDriver.writeR_Register(self.robot_IP, sync_register, sync_value)

        elif command == 'close':
            print("Closing Gripper...\n")
            FANUCethernetipDriver.writeR_Register(self.robot_IP, 20, 1)
            W_R_2_return = FANUCethernetipDriver.writeR_Register(self.robot_IP, sync_register, sync_value)

        else:
            print("Invalid command.")

    # Read conveyor belt sensor: returns value of 1 or 0
    def conveyor_proximity_sensor(self, sensor):
        right_sensor_register = 31
        left_sensor_register = 30

        if sensor == "right":
            return FANUCethernetipDriver.readR_Register(self.robot_IP, right_sensor_register)
        elif sensor == "left":
            return FANUCethernetipDriver.readR_Register(self.robot_IP, left_sensor_register)
        else:
            print("Invalid Sensor, Try 'right' or 'left'\n")

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
            FANUCethernetipDriver.writeR_Register(self.robot_IP, reverse_register, off)
            FANUCethernetipDriver.writeR_Register(self.robot_IP, forward_register, off)
            FANUCethernetipDriver.writeR_Register(self.robot_IP, sync_register, sync_value)

            FANUCethernetipDriver.writeR_Register(self.robot_IP, forward_register, on)
            ## Set sync bit to update
            FANUCethernetipDriver.writeR_Register(self.robot_IP, sync_register, sync_value)
        elif command == 'reverse':
            FANUCethernetipDriver.writeR_Register(self.robot_IP, reverse_register, off)
            FANUCethernetipDriver.writeR_Register(self.robot_IP, forward_register, off)
            FANUCethernetipDriver.writeR_Register(self.robot_IP, sync_register, sync_value)

            FANUCethernetipDriver.writeR_Register(self.robot_IP, reverse_register, on)
            ## Set sync bit to update
            FANUCethernetipDriver.writeR_Register(self.robot_IP, sync_register, sync_value)
        elif command == 'stop':
            print("--------------------------")
            print("| Stopping conveyor Belt |")
            print("--------------------------")
            FANUCethernetipDriver.writeR_Register(self.robot_IP, reverse_register, off)
            FANUCethernetipDriver.writeR_Register(self.robot_IP, forward_register, off)
            ## Set sync bit to update
            FANUCethernetipDriver.writeR_Register(self.robot_IP, sync_register, sync_value)
        else:
            FANUCethernetipDriver.writeR_Register(self.robot_IP, reverse_register, off)
            FANUCethernetipDriver.writeR_Register(self.robot_IP, forward_register, off)
            ## Set sync bit to update
            FANUCethernetipDriver.writeR_Register(self.robot_IP, sync_register, sync_value)

            









