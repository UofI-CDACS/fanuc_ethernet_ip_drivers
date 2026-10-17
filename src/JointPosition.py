import copy
import robot_controller
from typing import Self

# - Modified by Charle Bennington on 9/16/2026


class JointPosition():
    def __init__(self,
        j1 : float,
        j2 : float,
        j3 : float,
        j4 : float,
        j5 : float,
        j6 : float
    ):
        self.j1 = j1
        self.j2 = j2
        self.j3 = j3
        self.j4 = j4
        self.j5 = j5
        self.j6 = j6

    def move_to(self, robot : robot_controller.robot):
        robot.write_joint_pose([
            self.j1,
            self.j2,
            self.j3,
            self.j4,
            self.j5,
            self.j6,
        ])

    def get_current(robot : robot_controller.robot):
            return JointPosition.to_joint(robot.read_current_joint_position())

    def __str__(self) -> str:
        return (
            f"JointPosition( J1={self.j1:.2f}, J2={self.j2:.2f}, J3={self.j3:.2f}, "
            f"J4={self.j4:.2f}, J5={self.j5:.2f}, J6={self.j6:.2f} )"
        )


    def to_joint(inp_list : list[float] , **kwargs) -> Self:
        return JointPosition(
            inp_list[0],
            inp_list[1],
            inp_list[2],
            inp_list[3],
            inp_list[4],
            inp_list[5],
            **kwargs
        )