import sys
sys.path.append('../src')

import FANUCethernetipDriver as EIP
from robot_controller import robot

drive_path = '172.29.208.124' # Beaker

# Read in a list of inputs
inputList = EIP.readDigitalInputs(drive_path)
print("Returned list")
print(inputList)

# Read in 1 input
print("input 1: ", EIP.readDigitalInput(drive_path, 1)) # DI[1]
print("input 137: ", EIP.readDigitalInput(drive_path, 137)) # DI[137]

print("output 5: ", EIP.readDigitalOutput(drive_path, 5)) # DO[5]
