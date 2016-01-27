'''
module for function decorators. you can use some, or none of this

This is here for you java people, mostly
'''
from __future__ import print_function
import time
import warnings
import signal
import functools

class TimeoutError(Exception):
    '''Exception used by the timeout decorator'''
    pass
class cast_to(object):
    """Converts function arguments to specified types."""
    def __init__(self, *args, **kw):
        self.args = args
        self.kw = kw
    def __call__(self, f):
        @functools.wraps(f)
        def func(*args, **kw):
            nargs = [x[0](x[1]) for x in zip(self.args, args)]
            invalidkw = [x for x in kw if x not in self.kw]
            if len(invalidkw) > 0:
                raise TypeError, f.func_name + \
                    "() got an unexpected keyword argument '%s'" % invalidkw[0]
            kw = dict([(x, self.kw[x](kw[x])) for x in kw])
            v = f(*nargs, **kw)
            return v
        return func

def timeout(seconds, error_message='Function call timed out'):
    '''gives a method for having functions timeout'''
    def decorated(func):
        '''annotated function'''
        def _handle_timeout(signum, frame):
            '''times the function out'''
            del signum
            del frame
            raise TimeoutError(error_message)

        def wrapper(*args, **kwargs):
            '''does the wrapping'''
            signal.signal(signal.SIGALRM, _handle_timeout)
            signal.alarm(seconds)
            try:
                result = func(*args, **kwargs)
            finally:
                signal.alarm(0)
            return result

        return functools.wraps(func)(wrapper)

    return decorated

def deprecated(func):
    """This is a decorator which can be used to mark functions
    as deprecated. It will result in a warning being emmitted
    when the function is used."""

    def new_func(*args, **kwargs):
        '''internals'''
        warnings.simplefilter('always', DeprecationWarning)  # turn off filter
        warnings.warn(
            "Call to deprecated function {}.".format(
                func.__name__),
            category=DeprecationWarning,
            stacklevel=2)
        warnings.simplefilter('default', DeprecationWarning)  # reset filter
        return func(*args, **kwargs)

    new_func.__name__ = func.__name__
    new_func.__doc__ = func.__doc__
    new_func.__dict__.update(func.__dict__)
    return new_func

def timeit(method):
    '''times a function'''
    def timed(*args, **kw):
        '''the timed version of the function'''
        before = time.time()
        result = method(*args, **kw)
        after = time.time()

        print('%r (%r, %r) %2.2f sec' % \
              (method.__name__, args, kw, after-before))
        return result

    return timed

def accepts(*argstypes, **kwargstypes):
    '''checks arguments and makes sure they are of the correct type'''
    def wrapper(func):
        '''wraps a function'''
        @functools.wraps(func)
        def wrapped(*args, **kwargs):
            '''defines a wrapped function'''
            if len(args) > len(argstypes):
                raise TypeError(
                    "%s() takes at most %s non-keyword arguments (%s given)" %
                    (func.__name__, len(argstypes), len(args)))
            argspairs = zip(args, argstypes)
            for k, k_2 in kwargs.items():
                if k not in kwargstypes:
                    raise TypeError(
                        "Unexpected keyword argument '%s' for %s()" %
                        (k, func.__name__))
                argspairs.append((k_2, kwargstypes[k]))
            for param, expected in argspairs:
                if param is not None and not isinstance(param, expected):
                    raise TypeError(
                        "Parameter '%s' is not %s" %
                        (param, expected.__name__))
            return func(*args, **kwargs)
        return wrapped
    return wrapper


def returns(rtype):
    '''makes sure a function returns a result of a certain type'''
    def wrapper(function):
        '''wraps a function'''
        @functools.wraps(function)
        def wrapped(*args, **kwargs):
            '''defines a wrapped function'''
            result = function(*args, **kwargs)
            if not isinstance(result, rtype):
                raise TypeError(
                    "return value %r does not match %s" %
                    (result, rtype))
            return result
        return wrapped
    return wrapper
