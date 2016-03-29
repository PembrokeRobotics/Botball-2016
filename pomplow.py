import wallaby
import time
from config import GREEN_POM_CHANNEL, RED_POM_CHANNEL

POMPLOW_PORT = 2 #The port to which the pomplow's motor is attached
POMPLOW_SPEED = 100 #The speed at which we want the pomplow's motor to run

def turn_on_pom_plow():
    '''
    turns on the pom plow
    '''
    wallaby.motor(POMPLOW_PORT)

def turn_off_pom_plow():
    '''
    turns off the pom plow
    '''
    wallaby.off(POMPLOW_PORT)

def run_pom_plow_for_time(time):
    '''
    turns on the pom plow and turns it off after a given numver of seconds
    '''
    turn_on_pom_plow()
    time.sleep(time)
    turn_off_pom_plow()

def run_plow_while_poms():
    '''
    turns on the pom plow and keeps it running while there are poms in sight
    '''

    #very light wrapper on the channel int that lets me less clunkily get count
    class Channel(int):
        @property
        def count(self):
            wallaby.camera_update()
            return wallaby.get_object_count(self)

    green_channel = Channel(GREEN_POM_CHANNEL)
    red_channel   = Channel(RED_POM_CHANNEL)

    #whiles are technically a while True with an if clause
    #therefore, for whatever reason we can put an else
    #and that else will only be executed if we entered then exited the loop
    while(red_channel.count > 0 or green_channel.count > 0):
        turn_on_pom_plow()
        time.sleep(50)
    else:
        turn_off_pom_plow()
