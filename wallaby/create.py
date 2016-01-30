from ctypes import CDLL, c_int, c_char
from decorators import accepts, returns, cast_to

_create = CDLL("libwallaby.so")

'''

BEGIN CREATE FUNCTIONS
 int create_connect();
 int create_connect_once();
 void create_disconnect();
 void create_start();
 void create_passive();
 void create_safe();
 void create_full();
 void create_spot();
 void create_cover();
 void create_demo(int d);
 void create_cover_dock();
 int get_create_mode();
 int get_create_lbump();
 int get_create_rbump();
 int get_create_lwdrop();
 int get_create_cwdrop();
 int get_create_rwdrop();
 int get_create_wall();
 int get_create_lcliff();
 int get_create_lfcliff();
 int get_create_rfcliff();
 int get_create_rcliff();
 int get_create_llightbump();
 int get_create_lflightbump();
 int get_create_lclightbump();
 int get_create_rclightbump();
 int get_create_rflightbump();
 int get_create_rlightbump();
 int get_create_llightbump_amt();
 int get_create_rlightbump_amt();
 int get_create_lflightbump_amt();
 int get_create_lclightbump_amt();
 int get_create_rclightbump_amt();
 int get_create_rflightbump_amt();
 int get_create_vwall();
 int get_create_overcurrents();
 int get_create_infrared();
 int get_create_advance_button();
 int get_create_play_button();
 int get_create_normalized_angle();
 void set_create_normalized_angle(int angle);
 int get_create_total_angle();
 void set_create_total_angle(int angle);
 int get_create_distance();
 void set_create_distance(int dist);
 int get_create_battery_charging_state();
 int get_create_battery_voltage();
 int get_create_battery_current();
 int get_create_battery_temp();
 int get_create_battery_charge();
 int get_create_battery_capacity();
 int get_create_wall_amt();
 int get_create_lcliff_amt();
 int get_create_lfcliff_amt();
 int get_create_rfcliff_amt();
 int get_create_rcliff_amt();
 int get_create_bay_DI();
 int get_create_bay_AI();
 int get_create_song_number();
 int get_create_song_playing();
 int get_create_number_of_stream_packets();
 int get_create_requested_velocity();
 int get_create_requested_radius();
 int get_create_requested_right_velocity();
 int get_create_requested_left_velocity();
 void create_stop();
 void create_drive(int speed, int radius);
 void create_drive_straight(int speed);
 void create_spin_CW(int speed);
 void create_spin_CCW(int speed);
 void create_drive_direct(int l_speed, int r_speed);
 void create_spin_block(int speed, int angle);
 void create_advance_led(int on);
 void create_play_led(int on) ;
 void create_power_led(int color, int brightness);
 void create_digital_output(int bits);
 void create_pwm_low_side_drivers(int pwm2, int pwm1, int pwm0);
 void create_low_side_drivers(int pwm2, int pwm1, int pwm0);
 void create_load_song(int num);
 void create_play_song(int num);
 int create_read_block(char *data, int count);
 void create_write_byte(char byte);
 void create_clear_serial_buffer();

'''
def create_disconnect():
    '"disconnects the create"'
    _create.create_disconnect()

def create_start():
    "starts the create"
    _create.create_start()

def create_passive():
    _create.create_passive()

def create_safe():
    _create.create_safe()

def create_full():
    _create.create_full()

def create_spot():
    _create.create_spot()

def create_cover():
    _create.create_cover()

@accepts(int)
@cast_to(c_int)
def create_demo(d):
    _create.create_demo(d)

def create_cover_dock():
    _create.create_cover_dock()

@returns(int)
def get_create_mode():
    return int(_create.get_create_mode())

@returns(int)
def get_create_lbump():
    return int(_create.get_create_lbump())

@returns(int)
def get_create_rbump():
    return int(_create.get_create_rbump())

@returns(int)
def get_create_lwdrop():
    return int(_create.get_create_lwdrop())

@returns(int)
def get_create_cwdrop():
    return int(_create.get_create_cwdrop())

@returns(int)
def get_create_rwdrop():
    return int(_create.get_create_rwdrop())

@returns(int)
def get_create_wall():
    return int(_create.get_create_wall())

@returns(int)
def get_create_lfcliff():
    return int(_create.get_create_lfcliff())

@returns(int)
def get_create_rfcliff():
    return int(_create.get_create_rfcliff())

@returns(int)
def get_create_rcliff():
    return int(_create.get_create_rcliff())

@returns(int)
def get_create_lcliff():
    return int(_create.get_create_lcliff())

@returns(int)
def get_create_llightbump():
    return int(_create.get_create_llightbump())

@returns(int)
def get_create_lflightbump():
    return int(_create.get_create_lflightbump())

@returns(int)
def get_create_lclightbump():
    return int(_create.get_create_lclightbump())

@returns(int)
def get_create_rclightbump():
    return int(_create.get_create_rclightbump())

@returns(int)
def get_create_rflightbump():
    return int(_create.get_create_rflightbump())

@returns(int)
def get_create_rlightbump():
    return int(_create.get_create_rlightbump())

@returns(int)
def get_create_llightbump_amt():
    return int(_create.get_create_llightbump_amt())

@returns(int)
def get_create_lflightbump_amt():
    return int(_create.get_create_lflightbump_amt())

@returns(int)
def get_create_lclightbump_amt():
    return int(_create.get_create_lclightbump_amt())

@returns(int)
def get_create_rclightbump_amt():
    return int(_create.get_create_rclightbump_amt())

@returns(int)
def get_create_rflightbump_amt():
    return int(_create.get_create_rflightbump_amt())

@returns(int)
def get_create_rlightbump_amt():
    return int(_create.get_create_rlightbump_amt())

@returns(int)
def get_create_vwall():
    return int(_create.get_create_vwall())

@returns(int)
def get_create_overcurrents():
    return int(_create.get_create_overcurrents())

@returns(int)
def get_create_infrared():
    return int(_create.get_create_infrared())

@returns(int)
def get_create_advance_button():
    return int(_create.get_create_advance_button())

@returns(int)
def get_create_play_button():
    return int(_create.get_create_play_button())

@returns(int)
def get_create_normalized_angle():
    return int(_create.get_create_normalized_angle())

@accepts(int)
@cast_to(c_int)
def set_create_normalized_angle(angle):
    _create.set_create_normalized_angle(angle)

@returns(int)
def get_create_total_angle():
    return int(_create.get_create_total_angle())

@accepts(int)
@cast_to(c_int)
def set_create_total_angle(angle):
    _create.set_create_total_angle(angle)

@returns(int)
def get_create_distance():
    return int(_create.get_create_distance())

@accepts(int)
@cast_to(c_int)
def set_create_distance(dist):
    _create.set_create_distance(dist)

@returns(int)
def get_create_battery_charging_state():
    return int(_create.get_create_battery_charging_state())

@returns(int)
def get_create_battery_voltage():
    return int(_create.get_create_battery_voltage())

@returns(int)
def get_create_battery_current():
    return int(_create.get_create_battery_current())

@returns(int)
def get_create_battery_temp():
    return int(_create.get_create_battery_temp())

@returns(int)
def get_create_battery_charge():
    return int(_create.get_create_battery_charge())

@returns(int)
def get_create_battery_capacity():
    return int(_create.get_create_battery_capacity())


@returns(int)
def get_create_wall_amt():
    return int(_create.get_create_wall_amt())

@returns(int)
def get_create_lfcliff_amt():
    return int(_create.get_create_lfcliff_amt())

@returns(int)
def get_create_rfcliff_amt():
    return int(_create.get_create_rfcliff_amt())

@returns(int)
def get_create_rcliff_amt():
    return int(_create.get_create_rcliff_amt())

@returns(int)
def get_create_lcliff_amt():
    return int(_create.get_create_lcliff_amt())

@returns(int)
def get_create_bay_DI():
    return int(_create.get_create_bay_DI())

@returns(int)
def get_create_bay_AI():
    return int(_create.get_create_bay_AI())

@returns(int)
def get_create_song_number():
    return int(_create.get_create_song_number())

@returns(int)
def get_create_song_playing():
    return int(_create.get_create_song_playing())

@returns(int)
def get_create_number_of_stream_packets():
    return int(_create.get_create_number_of_stream_packets())

@returns(int)
def get_create_requested_velocity():
    return int(_create.get_create_requested_velocity())

@returns(int)
def get_create_requested_radius():
    return int(_create.get_create_requested_radius())

@returns(int)
def get_create_requested_right_velocity():
    return int(_create.get_create_requested_right_velocity())

@returns(int)
def get_create_requested_left_velocity():
    return int(_create.get_create_requested_left_velocity())

def create_stop():
    _create.create_stop()

@accepts(int, int)
@cast_to(c_int, c_int)
def create_drive(speed, radius):
    _create.create_drive(speed, radius)

@accepts(int)
@cast_to(c_int)
def create_drive_straight(speed):
    _create.create_drive_straight(speed)

@accepts(int)
@cast_to(c_int)
def create_spin_CW(speed):
    _create.create_spin_CW(speed)

@accepts(int)
@cast_to(c_int)
def create_spin_CCW(speed):
    _create.create_spin_CCW(speed)

@accepts(int, int)
@cast_to(c_int, c_int)
def create_drive_direct(l_speed, r_speed):
    _create.create_drive_direct(l_speed, r_speed)

@accepts(int, int)
@cast_to(c_int, c_int)
def create_spin_block(speed, angle):
    _create.create_spin_block(speed, angle)

@accepts(int)
@cast_to(c_int)
def create_advance_led(on):
    _create.create_advance_led(on)

@accepts(int)
@cast_to(c_int)
def create_play_led(on):
    _create.create_play_led(on)

@accepts(int, int)
@cast_to(c_int, c_int)
def create_power_led(color, brightness):
    _create.create_power_led(color, brightness)

@accepts(int)
@cast_to(c_int)
def create_digital_output(bits):
    _create.create_digital_output(bits)

@accepts(int, int, int)
@cast_to(c_int, c_int, c_int)
def create_pwm_low_side_drivers(pwm2, pwm1, pwm0):
    _create.create_pwm_low_side_drivers(pwm2, pwm1, pwm0)

@accepts(int, int, int)
@cast_to(c_int, c_int, c_int)
def create_low_side_drivers(pwm2, pwm1, pwm0):
    _create.create_low_side_drivers(pwm2, pwm1, pwm0)

@accepts(int)
@cast_to(c_int)
def create_load_song(num):
    _create.create_load_song(num)

@accepts(int)
@cast_to(c_int)
def create_play_song(num):
    _create.create_play_song(num)

@accepts(str, int)
@cast_to(c_char, c_int)
@returns(int)
def create_read_block(data, count):
    return int(_create.create_read_block(data, count))

@accepts(str)
@cast_to(c_char)
def create_write_byte(byte):
    _create.create_write_byte(byte)

def create_clear_serial_buffer():
    _create.create_clear_serial_buffer()
