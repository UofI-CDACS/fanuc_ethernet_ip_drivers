#/bin/python3
import os
import argparse
from fanuc_ethernet_ip_drivers import robot_controller
from fanuc_ethernet_ip_drivers import fanuc_eip_driver

# Global Constants
robot = robot_controller.robot
#drive_path = '129.101.98.214' # Bill
drive_path = '129.101.98.215' # DJ
#drive_path = '129.101.98.244' # Larry


def write_to_file(file_path, text):
    with open(file_path, 'a') as file:
        file.write(text+ '\n')


def main(args):

    crx10 =robot(args.robot_ip_addr)

    current_directory = os.getcwd()
    file_path = os.path.join(current_directory, args.output_file)
    pose_num = 1

    header = ''
    if args.capture_mode == 'cartesian':
        header = 'mode, index, position (xyzwpr)'

    else:
        header = 'mode, index, position (j1-6)'

    write_to_file(file_path, header)

    while True:
        choice = input("Please choose an option:\nc: Capture Position\nq Quit program\n")

        if choice == "c":
            # Code to capture position goes here
            text = ''
            if args.capture_mode == 'cartesian':
                current_cart_pos = fanuc_eip_driver.returnCartesianCurrentPostion(args.robot_ip_addr)
                text = args.capture_mode + ', ' + str(pose_num) + f',[{current_cart_pos[2]},{current_cart_pos[3]}, {current_cart_pos[4]}, {current_cart_pos[5]}, {current_cart_pos[6]}, {current_cart_pos[7]}]'

            elif args.capture_mode == 'joint':
                crx10.read_current_joint_position()
                text = args.capture_mode + ', ' + str(pose_num) + ", " + "[" + str(crx10.CurJointPosList[2]) + "," + str(crx10.CurJointPosList[3]) + "," + str(crx10.CurJointPosList[4]) + "," + str(crx10.CurJointPosList[5]) + "," + str(crx10.CurJointPosList[6]) + "," + str(crx10.CurJointPosList[7]) + "]"

            write_to_file(file_path, text)
            print("Position captured!", text)
            pose_num += 1

        elif choice == "q":
            print("Quitting the program...")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
                prog='Position Capture',
                description='Allows the user to move the robot in manual guided teaching mode and then record position to file.'
            )

    parser.add_argument('-rip',
                        '--robot-ip-address',
                        action='store',
                        dest='robot_ip_addr',
                        default=drive_path,
                        help='Sets the ip address of the robot on your network.'
                        )

    parser.add_argument('-m',
                        '--capture-mode',
                        action='store',
                        dest='capture_mode',
                        default='cartesian',
                        choices=['cartesian', 'joint'],
                        help='Select whether to capture robot position in \'joint\' mode or \'cartesian\' mode.'
                        )

    parser.add_argument('-o',
                        '--output-file',
                        action='store',
                        dest='output_file',
                        default='position_log.csv',
                        help='Designate a file that robot position data (in CSV format) will be logged to.'
                        )

    args = parser.parse_args()

    print(f'Logging poses from: \n\trobot @ {args.robot_ip_addr} \n\tcapture mode -> {args.capture_mode} \n\toutput file -> {args.output_file}')

    main(args)
