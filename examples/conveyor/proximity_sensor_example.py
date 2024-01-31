#!/usr/bin/env python3
"""! @brief Example of using proximity_sensor_example.py"""

##
# @mainpage Proximity Sensor Example
#
# @section description_main Description
# An example of using the robot_controller to read the proximity sensor 
# @section todo_robot_controller_example TODO
# - none
#
# @section author_robot_controller_example Author(s)
# - Created by James Lasso on 6/27/2023

# Imports
import time
from src.robot_controller import robot

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

    # Start belt
    crx10.conveyor("forward")

    # Ping pong an object back and forth between sensors and then stop when program exits
    try:
        pingpong = 0
        while(pingpong <= 5):
            # Check Sensors
            right = crx10.conveyor_proximity_sensor("right")
            left = crx10.conveyor_proximity_sensor("left")

            # Sensor check
            if right and not left:
                pingpong += 1
                crx10.conveyor("forward")
                time.sleep(0.5)
            elif not right and left:
                pingpong += 1
                crx10.conveyor("reverse")
                time.sleep(0.5)

            # Brief sleep to check sensors
            time.sleep(0.1)
    finally:
        print("Stopping conveyor belt...")
        crx10.conveyor("stop")

if __name__=="__main__":
    main()
