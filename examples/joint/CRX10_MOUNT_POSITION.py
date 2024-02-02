#!/usr/bin/env python3
"""! @brief move robot into mount position"""

##
# @mainpage robot controller example project
#
# @section description_main Description
# Move CRX10 robot into mount posiiton to change end tooling
# 
# @section todo_robot_controller_example TODO
# - Clean up
#
# @section author_robot_controller_example Author(s)
# - Created by James Lasso on 6/27/2023

# Imports
import sys
sys.path.append('../../src')
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
    crx10.set_speed(200)

    # Home position (set all positions to 1)
    # crx10.set_joints_to_home_position()

    # Set joints to mount position
    crx10.set_joints_to_mount_position()


    # Print Final position list
    print("*************************")
    print(" Final Joint Positions")
    print("*************************")
    crx10.read_current_joint_position()

    # End program
    print("==============================")
    print("END OF PROGRAM")
    print("==============================")

if __name__=="__main__":
    main()
