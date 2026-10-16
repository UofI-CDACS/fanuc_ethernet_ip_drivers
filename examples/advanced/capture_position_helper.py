import os
import sys
sys.path.append('../src')
from robot_controller import robot

# Global Constants
#drive_path = '129.101.98.214' # Bill
drive_path = '129.101.98.215' # DJ
#drive_path = '129.101.98.244' # Larry

crx10 =robot(drive_path)

def write_to_file(file_path, text):
    with open(file_path, 'a') as file:
        file.write(text+ '\n')

current_directory = os.getcwd()

file_path = os.path.join(current_directory, 'positionLog.txt')
pose_num = 1

while True:
    choice = input("Please choose an option:\n1. Capture Position\n2. Quit program\n")

    if choice == "1":
        # Code to capture position goes here
        text = "pose " + str(pose_num) + ": " + crx10.read_current_joint_position()
        write_to_file(file_path, text)
        print("Position captured!")
        pose_num += 1

    elif choice == "2":
        print("Quitting the program...")
        break

    else:
        print("Invalid choice. Please try again.")
