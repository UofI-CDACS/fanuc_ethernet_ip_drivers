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
import sys
import time
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
    crx10.set_speed(100)

    loops = 1
    while(loops <= 1):
        print("==============================")
        print(f"Current loops: {loops}/3")
        print("==============================")

        # Home position (set all positions to 1)
        crx10.set_joints_to_home_position()
        # Execute move action
        crx10.start_robot()

        # Read current cartesian coordinates
        crx10.read_current_cartesian_position()

        crx10.write_cartesian_coordinates(808, 106, 550)
        # Execute move action
        crx10.start_robot()

        #crx10.write_cartesian_coordinates(808, 106, 604)
        # Execute move action
        #crx10.start_robot()

        # Home position (set all positions to 1)
        crx10.set_joints_to_home_position()
        # Execute move action
        crx10.start_robot()

        # Print Final position list
        print("*************************")
        print(" Final Joint Positions")
        print("*************************")
        crx10.read_current_cartesian_position()

        # increment loops
        loops += 1

    # End program
    print("==============================")
    print("END OF PROGRAM")
    print("==============================")

if __name__=="__main__":
    main()
