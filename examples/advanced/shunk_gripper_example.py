#!/usr/bin/env python3
"""! @brief Example python program using robot_controller.py"""

##
# @mainpage robot controller example project
#
# @section description_main Description
# An example python program demonstrating how to use robot_controller class.
# 
# @section todo_robot_controller_example TODO
# - Clean up
#
# @section author_robot_controller_example Author(s)
# - Created by James Lasso on 6/13/2023

# Imports
import time
import sys
sys.path.append('../src')
from robot_controller import robot

# Global Constants
#drive_path = '129.101.98.214' # Bill
drive_path = '129.101.98.215' # DJ
#drive_path = '129.101.98.244' # Larry

def main():
    """! Main program entry"""

    # Create new robot object
    crx10 = robot(drive_path)

    # Set robot speed
    crx10.set_speed(300)

    loops = 1
    while(loops <= 1):
        
        # Set robot speed
        #crx10.set_speed(random.randrange(200, 300))
        print("==============================")
        print(f"Current loops: {loops}/3")
        print("==============================")

        # Home position (set all positions to 1)
        #crx10.set_joints_to_home_position()

        # Open Gripper
        crx10.gripper('open')
        time.sleep(2)

        # Close Gripper
        crx10.gripper('close')
        time.sleep(2)

        # increment loops
        loops += 1

    # End program
    print("==============================")
    print("END OF PROGRAM")
    print("==============================")

if __name__=="__main__":
    main()
