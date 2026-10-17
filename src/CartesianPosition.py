import copy
import robot_controller
from typing import Self

# - Modified by Charle Bennington on 9/16/2026

class CartesianPosition():
    def _check_if_in_sphere(pos : list[float], maxdist : float ) -> bool:
        return pos[0] ** 2 + pos[1] ** 2 + pos[2] ** 2 < maxdist ** 2


    def get_current(robot : robot_controller.robot):
        return CartesianPosition.to_cart(robot.read_current_cartesian_pose())


    def to_cart(inp_list : list[float] , **kwargs) -> Self:
        return CartesianPosition(
            inp_list[0],
            inp_list[1],
            inp_list[2],
            inp_list[3],
            inp_list[4],
            inp_list[5],
            **kwargs
        )

    def __str__(self) -> str:
        return (
            f"CartesianPosition(X={self.X:.2f}, Y={self.Y:.2f}, Z={self.Z:.2f}, "
            f"W={self.W:.2f}, P={self.P:.2f}, R={self.R:.2f} )"
        )

    def __init__(self ,
        X: float,
        Y: float,
        Z: float,
        W: float,
        P: float,
        R: float,
        max_mm_limit_reach_robot = 1249
    ):
        self.X = X
        self.Y = Y
        self.Z = Z
        self.W = W
        self.P = P
        self.R = R
        if self.W > 179.9 or self.W < -179.9:
            raise Warning(f"W, P and R should be in the range of [-179.9, 179.9], got {self.W}")
        if self.P > 179.9 or self.P < -179.9:
            raise Warning(f"W, P and R should be in the range of [-179.9, 179.9], got {self.P}")
        if self.R > 179.9 or self.R < -179.9:
            raise Warning(f"W, P and R should be in the range of [-179.9, 179.9], got {self.R}")

        cart_point = [self.X , self.Y , self.Z]
        if CartesianPosition._check_if_in_sphere(cart_point , max_mm_limit_reach_robot) == False: 
            raise Warning(f"The cartesian point {cart_point} may be out of reach of the robot. Please check the robot and your coordanates.")


    def move_to(self , crx10 : robot_controller.robot):
        crx10.write_cartesian_position([
            self.X,
            self.Y,
            self.Z,
            self.W,
            self.P,
            self.R 
        ])
        