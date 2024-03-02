# Imports
import time
import sys
sys.path.append('../../src')
from robot_controller import robot

# Global Constants
drive_path = '172.29.208.123' # Bunsen

pose_above =[[650.7,-240.3,-153.1,-177.5,1.5,-154.9],
             [408.8,3.3,-142.7,-177.4,-0.6,-155.4],
             [775.0,260.7,-160.0,-178.5,4.7,-154.4]
            ]
pose_grab =[[644.5,-239.5,-194.3,-179.2,-1.3,-154.9],
            [406.5,6.9,-188.0,-177.9,0.3,-153.6],
            [785.3,257.1,-196.9,179.7,0.0,-151.1]
           ]
pose_middle = [505.3,-62.6,181.7,179.0,3.2,-156.2]

def main():
    """! Main program entry"""

    # Create new robot object
    crx10 = robot(drive_path)

    # Set robot speed
    crx10.set_speed(300)

    first = 0
    second = 1
    while True:

        crx10.write_cartesian_position(pose_above[first])
        # Set robot speed
        crx10.set_speed(180)
        crx10.write_cartesian_position(pose_grab[first])
        crx10.schunk_gripper('close')
        crx10.set_speed(280)
        crx10.write_cartesian_position(pose_above[first])

        crx10.write_cartesian_position(pose_middle)

        crx10.write_cartesian_position(pose_above[second])
        crx10.set_speed(180)
        crx10.write_cartesian_position(pose_grab[second])
        crx10.schunk_gripper('open')
        crx10.set_speed(280)
        crx10.write_cartesian_position(pose_above[second])
        crx10.write_cartesian_position(pose_middle)

        first += 1
        second += 1

        if first == 3:
            first = 0
        if second == 3:
            second = 0


if __name__=="__main__":
    main()
