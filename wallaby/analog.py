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

from ctypes import CDLL, c_int, c_short
from decorators import accepts, returns, cast_to

#CDLL assumes that all functions return a c_int
_wallaby = CDLL("libwallaby.so")


'''
BEGIN ANALOG SENSOR FUNCTIONS

int analog(int port);

int analog8(int port);

int analog10(int port);

int analog12(int port);

int analog_et(int port);

void set_analog_pullup(int port, int pullup);

int get_analog_pullup(int port);
'''

@accepts(int)
@cast_to(c_int)
@returns(int)
def analog(port):
    '''gets the reading from the analog sensor at a port'''
    return int(_wallaby.analog(port))

@accepts(int)
@cast_to(c_int)
@returns(int)
def analog8(port):
    '''gets the 8 bit reading from the analog sensor at a port'''
    return int(_wallaby.analog8(port))

@accepts(int)
@cast_to(c_int)
@returns(int)
def analog10(port):
    '''gets the 10 bit reading from the analog sensor at a port'''
    return int(_wallaby.analog10(port))

@accepts(int)
@cast_to(c_int)
@returns(int)
def analog12(port):
    '''gets the 12 bit reading from the analog sensor at a port'''
    return int(_wallaby.analog12(port))

@accepts(int)
@cast_to(c_int)
@returns(int)
def analog_et(port):
    '''gets the reading from the ET sensor at a port'''
    return int(_wallaby.analog_et(port))

@accepts(int, int)
@cast_to(c_int, c_int)
def set_analog_pullup(port, pullup):
    '''sets the pullup for a port'''
    _wallaby.set_analog_pullup(port, pullup)

@accepts(int)
@cast_to(c_int)
@returns(int)
def get_analog_pullup(port):
    '''gets the pullup for a port'''
    return int(_wallaby.get_analog_pullup(port))
