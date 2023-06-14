
# CURJPOS Read and read and write PR[1] Joint Coordinates
#

import sys
sys.path.append('./pycomm3/pycomm3')
import struct
import random
import time

import FANUCethernetipDriver

drive_path = '129.101.98.214'    # CRX10 Bill

# read CURPOS from Robot
print("------------------------")
print(" read CURPOS from Robot")
print("------------------------")
CurPosList = FANUCethernetipDriver.returnJointCurrentPosition(drive_path)

print("CURPOS=", CurPosList)

# read PR[1] Joint Coordinates
print("------------------------")
print(" read PR[1] Joint Coordinate")
print("------------------------")

PRNumber = 1
PR_1_Value = FANUCethernetipDriver.readJointPositionRegister(drive_path, PRNumber)
print("PR[%d]"% PRNumber)
print("list=", PR_1_Value)

# write PR[1] Joint Coordinates
print("------------------------")
print(" write PR[1] Joint Coordinate")
print("------------------------")

# take CurPos and add random amount to J2 axis
newJ2 = CurPosList[3]+random.randrange(-10.0, 10)

CurPosList[3] = newJ2
print("CURPOS(J2offset)=", CurPosList)

PRNumber = 1
myList = CurPosList

W_PR_1_return = FANUCethernetipDriver.writeJointPositionRegister(drive_path, PRNumber, myList)

print("W_PR_1_return =", W_PR_1_return)

# write R[5] to set Speed in mm/sec
print("------------------------")
print(" write R[5] to set arm speed")
print("------------------------")

RegNum = 5
Value = 100
W_R_5_return = FANUCethernetipDriver.writeR_Register(drive_path, RegNum, Value)

print ("W_R_5_return=",W_R_5_return)


# write R[1] to start Robot
print("------------------------")
print(" write R[1] to move arm ")
print("------------------------")

RegNum = 1
Value = 1
W_R_2_return = FANUCethernetipDriver.writeR_Register(drive_path, RegNum, Value)

print ("W_R_2_return=",W_R_2_return)


# read R[1]
print("------------------------")
print(" read R[1] Register")
print("------------------------")

RegNum = 1

R_R_2_return = FANUCethernetipDriver.readR_Register(drive_path, RegNum)
print ("R_R_2_return=",R_R_2_return)


# read new CURPOS from Robot
print("------------------------")
print(" read new CURPOS from Robot")
print("------------------------")
CurPosList = FANUCethernetipDriver.returnJointCurrentPosition(drive_path)

print("CURPOS=", CurPosList)

