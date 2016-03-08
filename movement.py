"""
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

    movement functions for a two wheeled robot
"""

from __future__ import division
from wallaby import motor, off
import time

from config import LEFT_MOTOR_PORT, RIGHT_MOTOR_PORT

def move_forwards(power):
    '''move forwards at the given power'''
    motor(LEFT_MOTOR_PORT, power)
    motor(RIGHT_MOTOR_PORT, power)

def move_backwards(power):
    '''move backwards at the given power'''
    motor(LEFT_MOTOR_PORT, -power)
    motor(RIGHT_MOTOR_PORT, -power)

def turn_left(power):
    '''turns left at the given power'''
    motor(LEFT_MOTOR_PORT, -power)
    motor(RIGHT_MOTOR_PORT, power)

def turn_right(power):
    '''turns right at the given power'''
    motor(LEFT_MOTOR_PORT, power)
    motor(RIGHT_MOTOR_PORT, -power)

def move_forwards_for_time(power, milliseconds):
    '''move forwards at the given power for a given time(ms)'''
    move_forwards(power)
    time.sleep(milliseconds/1000) #sleep takes seconds, / by 1000 for ms
    stop()

def move_backwards_for_time(power, milliseconds):
    '''move backwards at the given power for a given time(ms)'''
    move_backwards(power)
    time.sleep(milliseconds/1000) #sleep takes seconds, / by 1000 for ms
    stop()

def turn_left_for_time(power, milliseconds):
    '''turns left at the given power for a given time(ms)'''
    turn_left(power)
    time.sleep(milliseconds/1000) #sleep takes seconds, / by 1000 for ms
    stop()

def turn_right_for_time(power, milliseconds):
    '''turns right at the given power for a given time(ms)'''
    turn_right(power)
    time.sleep(milliseconds/1000) #sleep takes seconds, / by 1000 for ms
    stop()

def stop():
    '''stops the robot'''
    off(LEFT_MOTOR_PORT)
    off(RIGHT_MOTOR_PORT)
