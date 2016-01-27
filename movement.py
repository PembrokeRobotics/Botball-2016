'''movement functions for a two wheeled robot'''
from __future__ import division
from wallaby import motor, off
from decorators import accepts
import time

from config import LEFT_MOTOR_PORT, RIGHT_MOTOR_PORT

@accepts(int)
def move_forwards(power):
    '''move forwards at the given power'''
    motor(LEFT_MOTOR_PORT, power)
    motor(RIGHT_MOTOR_PORT, power)

@accepts(int)
def move_backwards(power):
    '''move backwards at the given power'''
    motor(LEFT_MOTOR_PORT, -power)
    motor(RIGHT_MOTOR_PORT, -power)

@accepts(int)
def turn_left(power):
    '''turns left at the given power'''
    motor(LEFT_MOTOR_PORT, -power)
    motor(RIGHT_MOTOR_PORT, power)

@accepts(int)
def turn_right(power):
    '''turns right at the given power'''
    motor(LEFT_MOTOR_PORT, power)
    motor(RIGHT_MOTOR_PORT, -power)

@accepts(int, (int, float))
def move_forwards_for_time(power, milliseconds):
    '''move forwards at the given power for a given time(ms)'''
    move_forwards(power)
    time.sleep(milliseconds/1000) #sleep takes seconds, / by 1000 for ms
    stop()

@accepts(int, (int, float))
def move_backwards_for_time(power, milliseconds):
    '''move backwards at the given power for a given time(ms)'''
    move_backwards(power)
    time.sleep(milliseconds/1000) #sleep takes seconds, / by 1000 for ms
    stop()

@accepts(int, (int, float))
def turn_left_for_time(power, milliseconds):
    '''turns left at the given power for a given time(ms)'''
    turn_left(power)
    time.sleep(milliseconds/1000) #sleep takes seconds, / by 1000 for ms
    stop()

@accepts(int, (int, float))
def turn_right_for_time(power, milliseconds):
    '''turns right at the given power for a given time(ms)'''
    turn_right(power)
    time.sleep(milliseconds/1000) #sleep takes seconds, / by 1000 for ms
    stop()

def stop():
    '''stops the robot'''
    off(LEFT_MOTOR_PORT)
    off(RIGHT_MOTOR_PORT)
