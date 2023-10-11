import os
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
        text = "pose" + str(pose_num) + " " + "= [" + str(crx10.CurJointPosList[2]) + "," + str(crx10.CurJointPosList[3]) + "," + str(crx10.CurJointPosList[4]) + "," + str(crx10.CurJointPosList[5]) + "," + str(crx10.CurJointPosList[6]) + "," + str(crx10.CurJointPosList[7]) + "]"
        write_to_file(file_path, text)
        print("Position captured!")
        pose_num += 1

    elif choice == "2":
        print("Quitting the program...")
        break

    else:
        print("Invalid choice. Please try again.")
