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
sys.path.append('../../src')
from robot_controller import robot

# Global Constants
drive_path = '129.101.98.214' # Bill
#drive_path = '129.101.98.215' # DJ
#drive_path = '129.101.98.244' # Larry

def main():
    """! Main program entry"""

    # Create new robot object
    crx10 = robot(drive_path)

    # Set robot speed
    crx10.set_speed(300)

    loops = 1
    while(loops <= 2):
        
        # Set robot speed
        #crx10.set_speed(random.randrange(200, 300))
        print("==============================")
        print(f"Current loops: {loops}/2")
        print("==============================")

        # Home position (set all positions to 1)
        crx10.set_joints_to_home_position()
        time.sleep(1)

        # Write new position in joint 2 to -30
        crx10.write_joint_offset(2, -30)
        time.sleep(1)

        # write new position in join 2 to 30
        crx10.write_joint_offset(2, 30)
        time.sleep(1)

        # write new position in join 3-6 to 30
        crx10.write_joint_offset(3, -20)
        crx10.write_joint_offset(4, 30)
        crx10.write_joint_offset(5, -30)
        crx10.write_joint_offset(6, -30)
        time.sleep(1)

        crx10.write_joint_offset(4, -30)
        time.sleep(1)

        crx10.write_joint_offset(4, 30)
        time.sleep(1)

        # Home position (set all positions to 1)
        crx10.set_joints_to_home_position()
        time.sleep(1)

        crx10.write_joint_offset(6, -30)
        time.sleep(1)

        crx10.write_joint_offset(6, 30)
        time.sleep(1)

        # Home position (set all positions to 1)
        crx10.set_joints_to_home_position()
        time.sleep(1)

        # Print Final position list
        print("*************************")
        print(" Final Joint Positions")
        print("*************************")
        crx10.read_current_joint_position()

        # increment loops
        loops += 1

    # End program
    print("==============================")
    print("END OF PROGRAM")
    print("==============================")

if __name__=="__main__":
    main()
