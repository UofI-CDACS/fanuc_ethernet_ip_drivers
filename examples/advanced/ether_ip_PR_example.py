

# CURPOS Read and read and write PR[1] Cartesian Coordinates
#

import sys
sys.path.append('./pycomm3/pycomm3')
import random
sys.path.append('../src')
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

# take CurPos and add random amount to Z axis
newZ = CurPosList[4]+random.randrange(-50.0, 50)

CurPosList[4] = newZ
print("CURPOS(Zoffset)=", CurPosList)

PRNumber = 1
myList = CurPosList

W_PR_1_return = FANUCethernetipDriver.writeCartesianPositionRegister(drive_path, PRNumber, myList)

print("W_PR_1_return =", W_PR_1_return)
