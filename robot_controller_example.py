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
drive_path = '129.101.98.214' # Bill
#drive_path = '129.101.98.215' # DJ
#drive_path = '129.101.98.244' # Larry

def main():
    """! Main program entry"""

    # Create new robot object
    crx10 = robot(drive_path)

    loops = 1
    while(loops < 3):
        # Home position (set all positions to 1)
        crx10.set_joints_to_home_position()

        # Execute move action
        crx10.start_robot()

        # set moving variable to 1 from R[1]
        moving = crx10.read_robot_start_register()
        while(moving):
            time.sleep(2)
            print("******************************")
            print(" Moving Joint(s) to Position")
            print("******************************")
            # Update variable from R[1]
            moving = crx10.read_robot_start_register()

        # Signal end of move action
        print("*************************")
        print(" Joint Move Complete")
        print("*************************")

        # Write new position in joint 2 to -30
        crx10.write_joint_offset(2, -30)

        # Execute move action
        crx10.start_robot()

        moving = crx10.read_robot_start_register()
        while(moving):
            time.sleep(2)
            print("******************************")
            print(" Moving Joint(s) to Position")
            print("******************************")
            # Update variable from R[1]
            moving = crx10.read_robot_start_register()

        # signal end of move action
        print("*************************")
        print(" Joint Move Complete")
        print("*************************")

        # write new position in join 2 to 30
        crx10.write_joint_offset(2, 30)

        # Execute move action
        crx10.start_robot()

        moving = crx10.read_robot_start_register()
        while(moving):
            time.sleep(2)
            print("******************************")
            print(" Moving Joint(s) to Position")
            print("******************************")
            # Update variable from R[1]
            moving = crx10.read_robot_start_register()

        # Signal end of move action
        print("*************************")
        print(" Joint Move Complete")
        print("*************************")

        # write new position in join 3-6 to 30
        crx10.write_joint_offset(3, -50)
        crx10.write_joint_offset(4, 30)
        crx10.write_joint_offset(5, -30)
        crx10.write_joint_offset(6, -30)

        # Execute move action
        crx10.start_robot()

        moving = crx10.read_robot_start_register()
        while(moving):
            time.sleep(2)
            print("******************************")
            print(" Moving Joint(s) to Position")
            print("******************************")
            # Update variable from R[1]
            moving = crx10.read_robot_start_register()

        # Signal end of move action
        print("*************************")
        print(" Joint Move Complete")
        print("*************************")

        # Home position (set all positions to 1)
        crx10.set_joints_to_home_position()

        # Execute move action
        crx10.start_robot()

        # set moving variable to 1 from R[1]
        moving = crx10.read_robot_start_register()
        while(moving):
            time.sleep(2)
            print("*************************")
            print(" Moving Joint(s) to Position")
            print("*************************")
            # Update variable from R[1]
            moving = crx10.read_robot_start_register()

        # Signal end of move action
        print("*************************")
        print(" Joint Move Complete")
        print("*************************")

        # Print Final position list
        print("*************************")
        print(" Final Joint Positions")
        print("*************************")
        crx10.read_current_joint_position()

        # increment loops
        loops += 1

    # End program
    print("END OF PROGRAM")

if __name__=="__main__":
    main()
