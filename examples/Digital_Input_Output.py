import sys
sys.path.append('../') # This allows us to access files in src

import src.FANUCethernetipDriver as EIP

drive_path = '172.29.208.124' # Beaker

# Read in a list of inputs
inputList = EIP.readDigitalInputs(drive_path)
print("Returned list")
print(inputList)

# Read in 1 input
# EIP.readDigitalInput(drive_path, 1) # DI[1]
# EIP.readDigitalInput(drive_path, 137) # DI[137]

# EIP.readDigitalOutput(drive_path, 5) # DO[5]

erorr = EIP.writeR_Register(drive_path,1,0)
EIP.writeR_Register(drive_path,2,1)
print("Error:",erorr)
