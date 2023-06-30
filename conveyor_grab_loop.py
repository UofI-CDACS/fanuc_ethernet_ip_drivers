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
#drive_path = '129.101.98.214' # Bill
drive_path = '129.101.98.215' # DJ
#drive_path = '129.101.98.244' # Larry
sleep_time = 0.5

def main():
    """! Main program entry"""

    # Create new robot object
    crx10 = robot(drive_path)

    # Set robot speed
    crx10.set_speed(200)

    # Move robot to home position and open gripper
    crx10.set_joints_to_home_position()
    # Sync bit and move robot
    crx10.start_robot()
    # Open gripper
    crx10.gripper("open")

    # Move to FIRST position (PREPARE TO PICK UP DICE)
    crx10.write_joint_position(1, 14.000)
    crx10.write_joint_position(2, 20.000)
    crx10.write_joint_position(3, -45.000)
    crx10.write_joint_position(4, -0.737)
    crx10.write_joint_position(5, -46.000)
    crx10.write_joint_position(6, 16.00)
    # Sync bit and move robot
    crx10.start_robot()

    time.sleep(sleep_time)


    # Move to SECOND position (MOVE DOWN TO GRAB DICE)
    crx10.write_joint_position(1, 14.000)
    crx10.write_joint_position(2, 24.000)
    crx10.write_joint_position(3, -52.690)
    crx10.write_joint_position(4, -0.867)
    crx10.write_joint_position(5, -38.678)
    crx10.write_joint_position(6, 15.582)
    # Sync bit and move robot
    crx10.start_robot()

    time.sleep(sleep_time)

    # Close gripper
    crx10.gripper("close")
    # Pause briefly so gripper can close
    time.sleep(1)

    # Move back to SECOND position (HOLDING DICE, CLEAR TABLE)
    crx10.write_joint_position(1, 14.000)
    crx10.write_joint_position(2, 20.000)
    crx10.write_joint_position(3, -45.000)
    crx10.write_joint_position(4, -0.737)
    crx10.write_joint_position(5, -46.000)
    crx10.write_joint_position(6, 16.00)
    # Sync bit and move robot
    crx10.start_robot()

    # Move to THIRD position (PREPARE TO PLACE DICE)
    crx10.write_joint_position(1, 56.128)
    crx10.write_joint_position(2, 23.078)
    crx10.write_joint_position(3, -14.487)
    crx10.write_joint_position(4, -1.349)
    crx10.write_joint_position(5, -76.180)
    crx10.write_joint_position(6, -26.270)
    # Sync bit and move robot
    crx10.start_robot()

    # Move to FOURTH position(MOVE DOWN AND LET GO OF DICE)
    crx10.write_joint_position(1, 56.234)
    crx10.write_joint_position(2, 26.204)
    crx10.write_joint_position(3, -22.890)
    crx10.write_joint_position(4, -1.416)
    crx10.write_joint_position(5, -67.776)
    crx10.write_joint_position(6, -26.162)
    # Sync bit and move robot
    crx10.start_robot()
    # Open gripper
    crx10.gripper("open")
    # Pause briefly so gripper can open
    time.sleep(sleep_time)

    # Move back to THIRD position (NOT HOLDING DICE, CLEAR TABLE)
    crx10.write_joint_position(1, 56.128)
    crx10.write_joint_position(2, 23.078)
    crx10.write_joint_position(3, -14.487)
    crx10.write_joint_position(4, -1.349)
    crx10.write_joint_position(5, -76.180)
    crx10.write_joint_position(6, -26.270)
    # Sync bit and move robot
    crx10.start_robot()

    # Move to HOME position
    # Move robot to home position and open gripper
    crx10.set_joints_to_home_position()

    #start conveyor
    crx10.conveyor("forward")

    # Sync bit and move robot
    crx10.start_robot()
    time.sleep(sleep_time)

    loops = 1
    while(loops <= 5):
        crx10.conveyor("forward")
        print(f"Loops: {loops}/10")

        try:
            conveyor_on = True
            while(conveyor_on):
                # Check Sensors
                right = crx10.conveyor_proximity_sensor("right")
                left = crx10.conveyor_proximity_sensor("left")

                # Sensor check
                if right and not left:
                    crx10.conveyor("stop")
                    conveyor_on = False
                    time.sleep(0.5)
                elif not right and left:
                    crx10.conveyor("stop")
                    conveyor_on = False
                    time.sleep(0.5)

                # Brief sleep to check sensors
                time.sleep(0.1)
        finally:
            print("Stopping conveyor belt...")
            crx10.conveyor("stop")

        time.sleep(sleep_time)

        # Wait for proximity sensor to trigger

        # Move to FIFTH position (PREPARE TO PICK UP DICE)
        crx10.write_joint_position(1, 105.8661117553711)
        crx10.write_joint_position(2, 6.044949531555176)
        crx10.write_joint_position(3, -22.301790237426758)
        crx10.write_joint_position(4, -0.9746052622795105)
        crx10.write_joint_position(5, -67.01868438720703)
        crx10.write_joint_position(6, -74.2422103881836)
        # Sync bit and move robot
        crx10.start_robot()
        time.sleep(sleep_time)

        # Move to SIXTH position (MOVE DOWN AND PICK UP DICE)
        crx10.write_joint_position(1, 106.07597351074219)
        crx10.write_joint_position(2, 9.101266860961914)
        crx10.write_joint_position(3, -31.484973907470703)
        crx10.write_joint_position(4, -1.0569950342178345)
        crx10.write_joint_position(5, -57.83364486694336)
        crx10.write_joint_position(6, -74.26985168457031)
        # Sync bit and move robot
        crx10.start_robot()
        time.sleep(sleep_time)

        # Close gripper
        crx10.gripper("close")
        # Pause briefly so gripper can close
        time.sleep(1)

        # Move back to FIFTH position (HOLDING DICE, CLEAR TABLE)
        crx10.write_joint_position(1, 105.8661117553711)
        crx10.write_joint_position(2, 6.044949531555176)
        crx10.write_joint_position(3, -22.301790237426758)
        crx10.write_joint_position(4, -0.9746052622795105)
        crx10.write_joint_position(5, -67.01868438720703)
        crx10.write_joint_position(6, -74.2422103881836)
        # Sync bit and move robot
        crx10.start_robot()
        time.sleep(sleep_time)

        # Move to THIRD position (PREPARE TO PLACE DICE)
        crx10.write_joint_position(1, 56.128)
        crx10.write_joint_position(2, 23.078)
        crx10.write_joint_position(3, -14.487)
        crx10.write_joint_position(4, -1.349)
        crx10.write_joint_position(5, -76.180)
        crx10.write_joint_position(6, -26.270)
        # Sync bit and move robot
        crx10.start_robot()

        # Move to FOURTH position (MOVE DOWN AND LET GO OF DICE)
        crx10.write_joint_position(1, 56.234)
        crx10.write_joint_position(2, 26.204)
        crx10.write_joint_position(3, -22.890)
        crx10.write_joint_position(4, -1.416)
        crx10.write_joint_position(5, -67.776)
        crx10.write_joint_position(6, -26.162)
        # Sync bit and move robot
        crx10.start_robot()
        # Open gripper
        crx10.gripper("open")
        # Pause briefly so gripper can open
        time.sleep(1)

        # Move back to THIRD position (NOT HOLDING DICE, CLEAR TABLE)
        crx10.write_joint_position(1, 56.128)
        crx10.write_joint_position(2, 23.078)
        crx10.write_joint_position(3, -14.487)
        crx10.write_joint_position(4, -1.349)
        crx10.write_joint_position(5, -76.180)
        crx10.write_joint_position(6, -26.270)
        # Sync bit and move robot
        crx10.start_robot()

        #start conveyor
        crx10.conveyor("forward")

        #  MOVE INTO WAIT POSITION IN MIDDLE
        crx10.write_joint_position(1, 73.16226196289062)
        crx10.write_joint_position(2, 10.072640419006348)
        crx10.write_joint_position(3, -8.073392868041992)
        crx10.write_joint_position(4, -1.1352527141571045)
        crx10.write_joint_position(5, -81.83869171142578)
        crx10.write_joint_position(6, -41.75325012207031)
        # Sync bit and move robot
        crx10.start_robot()
        time.sleep(sleep_time)

        loops += 1

    # Move robot to home position and open gripper
    crx10.set_joints_to_home_position()
    # Sync bit and move robot
    crx10.start_robot()
    # Open gripper
    crx10.gripper("open")

    # End program
    print("==============================")
    print("END OF PROGRAM")
    print("==============================")

if __name__=="__main__":
    main()
