from ctypes import CDLL, c_int
from decorators import accepts, returns, cast_to

_wallaby = CDLL("libwallaby.so")

"""
BEGIN CAMERA FUNCTIONS

void camera_open();
void camera_close();
void camera_update();
int get_object_count(int channel);
int get_object_center_x(int channel, int object);
int get_object_center_y(int channel, int object);

"""

def camera_open():
    """opens the connection with the camera"""
    _wallaby.camera_open()

def camera_close():
    """ends the connection with the camera"""
    _wallaby.camera_close()

def camera_update():
    """gets a new image from the camera and performs color tracking"""
    _wallaby.camera_update()

@accepts(int)
@cast_to(c_int)
@returns(int)
def get_object_count(channel):
    """gets the number of objects being tracked on the specified channel"""
    return int(_wallaby.get_object_count(channel))

@accepts(int, int)
@cast_to(c_int, c_int)
@returns(int)
def get_object_center_x(channel, object):
    """gets the center x (column) coordinate value for the object # of the color channel"""
    return int(_wallaby.get_object_center_x(channel, object))

@accepts(int, int)
@cast_to(c_int, c_int)
@returns(int)
def get_object_center_y(channel, object):
    """gets the center y (row) coordinate value for the object # of the color channel"""
    return int(_wallaby.get_object_center_y(channel, object))
