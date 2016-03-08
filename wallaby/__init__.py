'''
Module containing all libwallaby functions
'''
def import_funcs(name):
    '''
    cheap hack to import all functions from submodules to global namespace
    '''
    modu = __import__(name, globals(), locals())
    attributes = dir(modu)
    for i in attributes:
        possible_function = getattr(modu,i)
        if hasattr(possible_function, '__call__'):
            globals()[i] = possible_function

import_funcs("accelerometer")
import_funcs("analog")
import_funcs("camera")
import_funcs("digital")
import_funcs("graphics")
import_funcs("motor")
import_funcs("create")
