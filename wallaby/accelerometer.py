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

from ctypes import CDLL, c_short
from decorators import returns

#CDLL assumes that all functions return a c_int
_wallaby = CDLL("libwallaby.so")


'''
BEGIN ACCELEROMETER FUNCTIONS

signed short accel_x();

signed short accel_y();

signed short accel_z();

int accel_calibrate();

'''

_wallaby.accel_x.restype = c_short

@returns(int)
def accel_x():
    '''gets the x value of the accelerometer'''
    return int(_wallaby.accel_x())

_wallaby.accel_y.restype = c_short

@returns(int)
def accel_y():
    '''gets the y value of the accelerometer'''
    return int(_wallaby.accel_y())

_wallaby.accel_z.restype = c_short

@returns(int)
def accel_z():
    '''gets the z value of the accelerometer'''
    return int(_wallaby.accel_z())

@returns(int)
def accel_calibrate():
    '''calibrates the accelerometer'''
    return int(_wallaby.accel_calibrate())
