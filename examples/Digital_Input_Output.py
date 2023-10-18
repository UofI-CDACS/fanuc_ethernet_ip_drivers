import sys
sys.path.append('../src') # This allows us to access files in src

import FANUCethernetipDriver as EIP
from robot_controller import robot

drive_path = '172.29.209.124' # Beaker

# Read in a list of inputs
inputList = EIP.readDigitalInputs(drive_path)
print("Returned list")
print(inputList)

# Read in 1 input
# EIP.readDigitalInput(drive_path, 1) # DI[1]
# EIP.readDigitalInput(drive_path, 137) # DI[137]

# EIP.readDigitalOutput(drive_path, 5) # DO[5]

crx10 = robot(drive_path)
crx10.write_robot_connection_bit(0)
crx10.write_robot_connection_bit(1)

print("After")

