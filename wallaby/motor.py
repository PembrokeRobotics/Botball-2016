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

    module for wrapping all necessary wallaby functions
"""

from ctypes import CDLL, c_int
from decorators import accepts, returns, cast_to

#CDLL assumes that all functions return a c_int
_wallaby = CDLL("libwallaby.so")


'''
BEGIN MOTOR FUNCTIONS

int get_motor_position_counter(int motor);

int gmpc(int motor);

void clear_motor_position_counter(int motor);

void cmpc(int motor);

int move_at_velocity(int motor, int velocity);

int mav(int motor, int velocity);

int move_to_position(int motor, int speed, int goal_pos);

int mtp(int motor, int speed, int goal_pos);

int move_relative_position(int motor, int speed, int delta_pos);

int mrp(int motor, int speed, int delta_pos);

int freeze(int motor);

int get_motor_done(int motor);

void block_motor_done(int motor);

void bmd(int motor);

int setpwm(int motor, int pwm);

int getpwm(int motor);

void fd(int motor);

void bk(int motor);

void motor(int motor, int percent);

void off(int motor);

void alloff();

void ao();

'''

@accepts(int)
@returns(int)
@cast_to(c_int)
def get_motor_position_counter(motor_num):
    '''gets motor position counter
    fill in section once we know what that means
    '''

    status = _wallaby.get_motor_position_counter(motor_num)
    return int(status)

@accepts(int)
@returns(int)
def gmpc(motor_num):
    '''
    shortened alias for get_motor_position_counter
    '''

    return get_motor_position_counter(motor_num)

@accepts(int)
@cast_to(c_int)
def clear_motor_position_counter(motor_num):
    '''
    clears the motor position counter
    '''

    _wallaby.clear_motor_position_counter(motor_num)

@accepts(int)
def cmpc(motor_num):
    '''
    shortened alias for clear_motor_position_counter
    '''
    clear_motor_position_counter(motor_num)

@accepts(int, int)
@cast_to(c_int, c_int)
def move_at_velocity(motor_num, velocity):
    '''
    moves the designated motor at velocity

    velocity is given in [TBD]
    '''

    _wallaby.move_at_velocity(motor_num, velocity)


@accepts(int, int)
def mav(motor_num, velocity):
    '''
    shortened alias for move_at_velocity
    '''
    move_at_velocity(motor_num, velocity)

@accepts(int, int, int)
@cast_to(c_int, c_int, c_int)
def move_to_position(motor_num, speed, goal_pos):
    '''
    moves the motor to a given position
    '''
    _wallaby.move_to_position(motor_num,
                              speed,
                              goal_pos)

@accepts(int, int, int)
@cast_to(c_int, c_int, c_int)
def mtp(motor_num, speed, goal_pos):
    '''
    shortened alias for move_to_position
    '''

    move_to_position(motor_num, speed, goal_pos)

@accepts(int, int, int)
@cast_to(c_int, c_int, c_int)
def move_relative_position(motor_num, speed, delta_pos):
    '''move motor to a relative position'''

    _wallaby.move_relative_position(motor_num, speed, delta_pos)

def mrp(motor_num, speed, delta_pos):
    '''shortened alias for move_relative_position'''
    move_relative_position(motor_num, speed, delta_pos)

@accepts(int)
@cast_to(c_int)
def freeze(motor_num):
    '''freezes the motor'''
    _wallaby.freeze(motor_num)

@accepts(int)
@returns(bool)
@cast_to(c_int)
def get_motor_done(motor_num):
    '''gets if the motor is done'''
    result = _wallaby.get_motor_done(motor_num)
    return bool(int(result))

@accepts(int)
@cast_to(c_int)
def block_motor_done(motor_num):
    '''block motor done'''
    _wallaby.block_motor_done(motor_num)

@accepts(int)
def bmd(motor_num):
    '''alias for block motor done'''
    block_motor_done(motor_num)

@accepts(int)
@cast_to(c_int)
def setpwm(motor_num, pwm):
    '''sets the pwm'''
    _wallaby.setpwm(motor_num, pwm)

@accepts(int)
@cast_to(c_int)
def getpwm(motor_num):
    '''gets the pwm'''
    _wallaby.getpwm(motor_num)

@accepts(int)
@cast_to(c_int)
def fd(motor_num):
    '''runs the motor forwards'''
    _wallaby.fd(motor_num)

@accepts(int)
@cast_to(c_int)
def bk(motor_num):
    '''runs the motor backwards'''
    _wallaby.bk(motor_num)

#insert more here

@accepts(int, int)
@cast_to(c_int, c_int)
def motor(motor_num, power_level):
    '''puts the specified motor to the specified power'''

    _wallaby.motor(motor_num, power_level)

@accepts(int)
@cast_to(c_int)
def off(motor_num):
    '''turns the specified motor off'''

    _wallaby.off(motor_num)

def ao():
    '''turns all motors off'''
    _wallaby.ao()

def all_off():
    '''turns all motors off'''
    ao()
