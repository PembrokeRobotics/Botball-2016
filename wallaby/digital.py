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
BEGIN DIGITAL FUNCTIONS

int digital(int port);

void set_digital_value(int port, int value);

int get_digital_value(int port);

void set_digital_output(int port, int out);

int get_digital_output(int port);

int get_digital_pullup(int port);

void set_digital_pullup(int port, int pullup);
'''

@accepts(int)
@cast_to(c_int)
@returns(int)
def digital(port):
    '''returns the value of the digital port, either zero or one'''
    return int(_wallaby.digital(port))

@accepts(int, int)
@cast_to(c_int, c_int)
def set_digital_value(port, value):
    '''sets the digital value of a port'''
    _wallaby.set_digital_value(port, value)

@accepts(int)
@cast_to(c_int)
@returns(int)
def get_digital_value(port):
    '''gets the digital value at a port'''
    return int(_wallaby.get_digital_value(port))

@accepts(int, int)
@cast_to(c_int, c_int)
def set_digital_output(port, out):
    '''sets digital output'''
    _wallaby.set_digital_output(port, out)

@accepts(int)
@cast_to(c_int)
@returns(int)
def get_digital_output(port):
    '''gets digital output at a port'''
    return int(_wallaby.get_digital_output(port))

@accepts(int)
@cast_to(c_int)
@returns(int)
def get_digital_pullup(port):
    '''gets digital pullup'''
    return int(_wallaby.get_digital_pullup(port))

@accepts(int, int)
@cast_to(c_int, c_int)
def set_digital_pullup(port, pullup):
    '''sets digital pullup'''
    _wallaby.set_digital_pullup(port, pullup)
