import numpy as np
from time import sleep
import time
from adafruit_servokit import ServoKit

import leg
from leg import *

class Spider:
    def __init__(self, leg_objects):
        self.deg1, self.deg2, self.deg3 = 90, 70, 90
        """Initialize spider
        """
        self.hat1 = ServoKit(channels=16, address=0x40)
        self.hat2 = ServoKit(channels=16, address=0x41)

       
        self.legs =leg_objects
        self.start_position()


    def move_all_legs(self, arr_deg):
        for leg in self.legs:
            leg.move(arr_deg)
    def start_position(self):
        """Position where the spider is standing stable
        """
        self.move_all_legs([self.deg1, self.deg2, self.deg3])


    def change_single(self, index_leg, change_deg):
        if index_leg < len(self.legs):
            leg = self.legs[index_leg]
            leg.move([leg.degrees[0], leg.degrees[1] + 30, leg.degrees[2]])
            leg.move([leg.degrees[0] + change_deg, leg.degrees[1] + 30, leg.degrees[2]])
            leg.move([leg.degrees[0] + change_deg, leg.degrees[1], leg.degrees[2]])
        else:
            print("Invalid leg index.")

    def reset_pos(self):
        for leg in self.legs:
            leg.reset_horizontal()


    def change_all(self, change_deg):
        for leg in self.legs:
            self.change_single(leg, change_deg)
            sleep(0.1)

    def single_turn(self):
        self.change_all(30)
        sleep(.5)
        self.change_all(30)
        sleep(.5)
        self.change_all(30)
        sleep(.5)
        self.reset_pos()
        sleep(.2)

    def turns(self, N):
        for i in range(N):
            self.single_turn()


    def standup(self):
        for leg in self.legs:
            leg.move([leg.degrees[0], 0, 60])


    def sit_stand_steps(self, N=10, delay=0.5):
        for _ in range(N):
            for i, leg in enumerate(self.legs):
                if leg.degrees[1] > 90 and leg.degrees[2] > 120:
                    change = -1
                    changing_deg2 = abs(leg.current_degrees[1] - leg.degrees[1])
                    changing_deg3 = abs(leg.current_degrees[2] - leg.degrees[2])
                    deg_stand_steps_2 = changing_deg2 / N * change
                    deg_stand_steps_3 = changing_deg3 / N * change
                else:
                    change = 1
                    changing_deg2 = abs(175 - leg.degrees[1])
                    changing_deg3 = abs(162 - leg.degrees[2])
                    deg_stand_steps_2 = changing_deg2 / N * change
                    deg_stand_steps_3 = changing_deg3 / N * change

                new_degrees = [
                    leg.current_degrees[0],
                    leg.current_degrees[1] + deg_stand_steps_2,
                    leg.current_degrees[2] + deg_stand_steps_3
                ]
                leg.move(new_degrees)
            sleep(delay)




    def sitdown_steps(self, N=10, delay=0.5):
        deg_stand_steps_2 = 110 / N
        deg_stand_steps_3 = 90 / N
        for _ in range(N - 1):
            for leg in self.legs:
                new_degrees = [
                    leg.current_degrees[0],
                    leg.current_degrees[1] + deg_stand_steps_2,
                    leg.current_degrees[2] + deg_stand_steps_3
                ]
                leg.move(new_degrees)
            sleep(delay)

    def sitdown(self, delay):
        for leg_index in [0, 2, 3, 5, 1, 4]:
            current_leg = self.legs[leg_index]
            current_leg.move([current_leg.current_degrees[0], 90, 90])

        sleep(delay)

        for leg_index in [0, 2, 3, 5, 1, 4]:
            current_leg = self.legs[leg_index]
            current_leg.move([current_leg.current_degrees[0], 90, 60])

        sleep(delay)

        for leg_index in [0, 2, 3, 5, 1, 4]:
            current_leg = self.legs[leg_index]
            current_leg.move([current_leg.current_degrees[0], 90, 30])


    def turn3_0(self, steps, direction, speed=.5):
        if direction == 'right':
            angle = -30
            go = True
        elif direction == 'left':
            angle = 30
            go = True
        else:
            print('what direction is the turn, right or left?')
            go = False

        if go:
            start_values = [leg.current_degrees for leg in self.legs]
            for _ in range(steps):
                # Lift and move legs 0,1, 2 3, 4, 5 forward

                for leg_index in [0, 3, 4, 2, 1, 5]:
                    self.change_single(leg_index, angle)
                    time.sleep(speed)

                # Reset legs to starting position
                for i, leg in enumerate(self.legs):
                    leg.move(start_values[i])

    def walk_forward(self, steps, speed=0.5):
        start_values_1 = self.leg_1[2]
        start_values_2 = self.leg_2[2]
        start_values_3 = self.leg_3[2]
        start_values_4 = self.leg_4[2]
        start_values_5 = self.leg_5[2]
        start_values_6 = self.leg_6[2]
        for _ in range(steps):
            # Lift and move legs 0, 3, 4 forward
            self.change_single(0,30)
            time.sleep(speed)

            self.change_single(4,-30)
            time.sleep(speed)

            self.change_single(3,-30)
            time.sleep(speed)

            # Reset legs to starting position
            self.leg_1.move(start_values_1)
            self.leg_2.move(start_values_2)
            self.leg_3.move(start_values_3)
            self.leg_4.move(start_values_4)
            self.leg_5.move(start_values_5)
            self.leg_6.move(start_values_6)


            self.change_single(5,-30)
            time.sleep(speed)

            # Lift and move legs 1, 2, 5 forward
            self.change_single(1,30)
            time.sleep(speed)

            self.change_single(2,30)
            time.sleep(speed)

            # Reset legs to starting position
            self.leg_1.move(start_values_1)
            self.leg_2.move(start_values_2)
            self.leg_3.move(start_values_3)
            self.leg_4.move(start_values_4)
            self.leg_5.move(start_values_5)
            self.leg_6.move(start_values_6)




    def walk_forward_diagonal(self, steps, speed=0.5):
        start_values_1 = self.leg_1[2]
        start_values_2 = self.leg_2[2]
        start_values_3 = self.leg_3[2]
        start_values_4 = self.leg_4[2]
        start_values_5 = self.leg_5[2]
        start_values_6 = self.leg_6[2]
        for _ in range(steps):
            # Lift and move legs 0, 4 forward
            self.change_single(0, 30)
            time.sleep(speed)
            self.change_single(4, -30)

            # Reset legs to starting position
            # self.start_position()

            # Lift and move legs 1, 5 forward
            self.change_single(1, 30)
            time.sleep(speed)

            self.leg_1.move(start_values_1)
            self.leg_2.move(start_values_2)
            self.leg_3.move(start_values_3)
            self.leg_4.move(start_values_4)
            self.leg_5.move(start_values_5)
            self.leg_6.move(start_values_6)

            self.change_single(3, -30)

            # Reset legs to starting position
            # self.start_position()
            time.sleep(speed)

            # Lift and move legs 2, 3 forward
            self.change_single(2, 30)
            self.change_single(5, -30)
            time.sleep(speed)
            # Reset legs to starting position
            self.leg_1.move(start_values_1)
            self.leg_2.move(start_values_2)
            self.leg_3.move(start_values_3)
            self.leg_4.move(start_values_4)
            self.leg_5.move(start_values_5)
            self.leg_6.move(start_values_6)

    def tripod_turn(self, steps, direction, speed=0.5):
        if direction == 'right':
            angle = -30
            go = True
        elif direction == 'left':
            angle = 30
            go = True

        else:
            print('what direction is the turn, right or left?')
            go = False
        if go:
            start_values_1 = self.leg_1[2]
            start_values_2 = self.leg_2[2]
            start_values_3 = self.leg_3[2]
            start_values_4 = self.leg_4[2]
            start_values_5 = self.leg_5[2]
            start_values_6 = self.leg_6[2]
            for _ in range(steps):
                # Lift and move legs 0,1, 2 3, 4, 5 forward
                for leg_index in [[0, 2, 4], [1, 3, 5]]:
                    _, _, current_deg_1 = self.legs[leg_index[0]]
                    _, _, current_deg_2 = self.legs[leg_index[1]]
                    _, _, current_deg_3 = self.legs[leg_index[2]]

                    self.move_single_leg([current_deg_1[0], current_deg_1[1] + 30, current_deg_1[2]], leg_index[0])
                    self.move_single_leg([current_deg_2[0], current_deg_2[1] + 30, current_deg_2[2]], leg_index[1])
                    self.move_single_leg([current_deg_3[0], current_deg_3[1] + 30, current_deg_3[2]], leg_index[2])

                    sleep(.1)
                    self.move_single_leg([current_deg_1[0] + angle, current_deg_1[1] + 30, current_deg_1[2]], leg_index[0])
                    self.move_single_leg([current_deg_2[0] + angle, current_deg_2[1] + 30, current_deg_2[2]], leg_index[1])
                    self.move_single_leg([current_deg_3[0] + angle, current_deg_3[1] + 30, current_deg_3[2]], leg_index[2])

                    sleep(.1)
                    self.move_single_leg([current_deg_1[0] + angle, current_deg_1[1], current_deg_1[2]], leg_index[0])
                    self.move_single_leg([current_deg_2[0] + angle, current_deg_2[1], current_deg_2[2]], leg_index[1])
                    self.move_single_leg([current_deg_3[0] + angle, current_deg_3[1], current_deg_3[2]], leg_index[2])

                    time.sleep(speed)

                    # Reset legs to starting position
                    self.move_single_leg(start_values_1, 0)
                    self.move_single_leg(start_values_2, 1)
                    self.move_single_leg(start_values_3, 2)
                    self.move_single_leg(start_values_4, 3)
                    self.move_single_leg(start_values_5, 4)
                    self.move_single_leg(start_values_6, 5)


    def calc_changing_deg(self, leg_index, wanted_degrees, N):
        changing_deg2_1 = wanted_degrees[0] - self.legs[leg_index][2][1]
        changing_deg3_1 = wanted_degrees[1] - self.legs[leg_index][2][2]

        step_deg1 = changing_deg2_1 / N
        step_deg2 = changing_deg3_1 / N

        return step_deg1, step_deg2


    def sit_stand_steps_2(self, N=10, delay=.5, wanted_degrees=[175, 162]):
        run = False
        try:
            run = True
            deg_stand_steps_2_1, deg_stand_steps_3_1 = self.calc_changing_deg(0, wanted_degrees, N)
            deg_stand_steps_2_2, deg_stand_steps_3_2 = self.calc_changing_deg(1, wanted_degrees, N)
            deg_stand_steps_2_3, deg_stand_steps_3_3 = self.calc_changing_deg(2, wanted_degrees, N)
            deg_stand_steps_2_4, deg_stand_steps_3_4 = self.calc_changing_deg(3, wanted_degrees, N)
            deg_stand_steps_2_5, deg_stand_steps_3_5 = self.calc_changing_deg(4, wanted_degrees, N)
            deg_stand_steps_2_6, deg_stand_steps_3_6 = self.calc_changing_deg(5, wanted_degrees, N)
        except:
            print('something went wrong')

        if run:
            for _ in range(N):
                self.move_single_leg(
                    [self.leg_1[2][0], self.leg_1[2][1] + deg_stand_steps_2_1, self.leg_1[2][2] + deg_stand_steps_3_1], 0)
                self.move_single_leg(
                    [self.leg_2[2][0], self.leg_2[2][1] + deg_stand_steps_2_2, self.leg_2[2][2] + deg_stand_steps_3_2], 1)
                self.move_single_leg(
                    [self.leg_3[2][0], self.leg_3[2][1] + deg_stand_steps_2_3, self.leg_3[2][2] + deg_stand_steps_3_3], 2)
                self.move_single_leg(
                    [self.leg_4[2][0], self.leg_4[2][1] + deg_stand_steps_2_4, self.leg_4[2][2] + deg_stand_steps_3_4], 3)
                self.move_single_leg(
                    [self.leg_5[2][0], self.leg_5[2][1] + deg_stand_steps_2_5, self.leg_5[2][2] + deg_stand_steps_3_5], 4)
                self.move_single_leg(
                    [self.leg_6[2][0], self.leg_6[2][1] + deg_stand_steps_2_6, self.leg_6[2][2] + deg_stand_steps_3_6], 5)
                sleep(delay)


    def face_up(self, speed=.5):
        self.move_single_leg([60, 0, 30], 5)
        self.move_single_leg([120, 0, 30], 0)

        self.move_single_leg([60, 90, 60], 2)
        self.move_single_leg([120, 60, 60], 3)

        self.move_single_leg([60, 60, 60], 1)
        self.move_single_leg([120, 60, 60], 4)




