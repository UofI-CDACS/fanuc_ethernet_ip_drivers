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
import random
from robot_controller import robot

# Global Constants
drive_path = '129.101.98.214' # Bill
#drive_path = '129.101.98.215' # DJ
#drive_path = '129.101.98.244' # Larry
sleep_time = 0.5

def main():
    """! Main program entry"""

    # Create new robot object
    crx10 = robot(drive_path)

    # Set robot speed
    crx10.set_speed(400)

    crx10.get_coords()

    loops = 0
    while(loops < 10):
        crx10.send_coords(90.000,-188.000,500.000)
        crx10.start_robot()
        crx10.get_coords()
        crx10.send_coords(300.000,-188.000,500.000)
        crx10.start_robot()
        crx10.send_coords(300.000,-188.000,200.000)
        crx10.start_robot()
        crx10.send_coords(90.000,-188.000,200.000)
        crx10.start_robot()
        crx10.send_coords(90.000,-188.000,500.000)
        crx10.start_robot()
        loops += 1


    print("END OF PROGRAM")

if __name__=="__main__":
    main()
