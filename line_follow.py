'''
function for following a black line for a given amount of time

assumes that we start on the black line when function is called
'''

BLACK_THRESHOLD = 3000;

from movement import *
from decorators import timeout,TimeoutError
from wallaby import analog
IR_SENSOR_PORT = 0;

def line_follow():
    while True:

        if (analog(IR_SENSOR_PORT) >= BLACK_THRESHOLD):
            move_forwards_for_time(100,100)
            turn_left_for_time(100,100)

        if (analog(IR_SENSOR_PORT) < BLACK_THRESHOLD):
            turn_right_for_time(100,100)





def line_follow_time(time):
    try:
        timeout(time)(line_follow)()
    except TimeoutError:
        pass #intended behaviour
