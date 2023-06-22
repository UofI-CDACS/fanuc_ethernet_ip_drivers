# CURPOS Read and read and write PR[1] Cartesian Coordinates
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
CurPosList = FANUCethernetipDriver.returnCartesianCurrentPostion(drive_path)

print("CURPOS=", CurPosList)

# read PR[1] Cartesian Coordinates
print("------------------------")
print(" read PR[1] Cartesian Coordinate")
print("------------------------")

PRNumber = 1
PR_1_Value = FANUCethernetipDriver.readCartesianPositionRegister(drive_path, PRNumber)
print("PR[%d]"% PRNumber)
print("list=", PR_1_Value)

# write PR[1] Cartesian Coordinates
print("------------------------")
print(" write PR[1] Cartesian Coordinate")
print("------------------------")

# take CurPos and add to Z axis
newZ = CurPosList[4]+10.0

CurPosList[4] = newZ
print("CURPOS(Zoffset)=", CurPosList)

PRNumber = 2
SyncDInput = 10
myList = CurPosList

W_PR_1_return = FANUCethernetipDriver.writeCartesianPositionRegister(drive_path, PRNumber, myList)

print("W_PR_1_return =", W_PR_1_return)



# write R[2]
print("------------------------")
print(" write R[2] Register")
print("------------------------")

RegNum = 2
Value = 1
W_R_2_return = FANUCethernetipDriver.writeR_Register(drive_path, RegNum, Value)

print ("W_R_2_return=",W_R_2_return)


# read R[2]
print("------------------------")
print(" read R[2] Register")
print("------------------------")

RegNum = 2

R_R_2_return = FANUCethernetipDriver.readR_Register(drive_path, RegNum)
print ("R_R_2_return=",R_R_2_return)

# read All Digital Inputs to Robot
print("------------------------")
print(" read All Digital Inputs to Robot")
print("------------------------")

DigitalInputList = FANUCethernetipDriver.readDigitalInputs(drive_path)

# conveyor 1 Left Prox
print("bitNumber[%d]=%x"% (137,FANUCethernetipDriver.returnBit(137, DigitalInputList)))
# conveyor 1 Right Prox
print("bitNumber[%d]=%x"% (139,FANUCethernetipDriver.returnBit(139, DigitalInputList)))

# read All Digital Outputs From Robot
print("------------------------")
print(" read All Digital Outputs From Robot")
print("------------------------")

DigitalOutputList = FANUCethernetipDriver.readDigitalOutputs(drive_path)

#count = 1
#for x in DigitalOutputList:
#        print("DO[%d-%d]=%x"%(count, count+7,x))
#        count=count+8

print("bitNumber[%d]=%x"% (137,FANUCethernetipDriver.returnBit(137, DigitalOutputList)))
print("bitNumber[%d]=%x"% (138,FANUCethernetipDriver.returnBit(138, DigitalOutputList)))



# Start Conveyor Forward 
print("------------------------")
print(" Start Conveyor Forward")
print("------------------------")
# R21 is forward
# R22 is reverse

RegNum = 21
Value = 1
W_R_21_return = FANUCethernetipDriver.writeR_Register(drive_path, RegNum, Value)

print ("W_R_21_return=",W_R_21_return)


# set Sync Bit to Update
print("------------------------")
print(" Set IO sync bit to update")
print("------------------------")

RegNum = 2
Value = 1
W_R_2_return = FANUCethernetipDriver.writeR_Register(drive_path, RegNum, Value)

print ("W_R_2_return=",W_R_2_return)

time.sleep(2)

# Stop Conveyor Forward 
print("------------------------")
print(" Stop Conveyor Forward")
print("------------------------")

RegNum = 21
Value = 0
W_R_21_return = FANUCethernetipDriver.writeR_Register(drive_path, RegNum, Value)

print ("W_R_21_return=",W_R_21_return)

# set Sync Bit to Update
print("------------------------")
print(" Set IO sync bit to update")
print("------------------------")

RegNum = 2
Value = 1
W_R_2_return = FANUCethernetipDriver.writeR_Register(drive_path, RegNum, Value)

print ("W_R_2_return=",W_R_2_return)

