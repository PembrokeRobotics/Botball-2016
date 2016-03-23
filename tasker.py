import collections
import types
import inspect
import functools

class Tasker(object):
    '''
    class to simplify running tasks in order
    '''

    def __init__(self):
        self.task_list = collections.deque()

    def add_single_task(self, new_task):
        '''
        add a task to the task list

        new_task must be either a function or a partial
        and that function or partial must take zero args
        '''

        #check that runs if it is a partial
        if isinstance(new_task, functools.partial):
            len_original_func_arguments    = len(inspect.getargspec(new_task.func).args)
            number_of_partialed_arguments  = len(new_task.args)

            if (len_original_func_arguments - number_of_partialed_arguments) == 0:
                self.task_list.appendleft(new_task)
            else:
                raise TypeError("Make sure that the passed partial takes no arguments")

        #check that runs if it is a pure function
        elif isinstance(new_task, types.FunctionType):
            if not inspect.getargspec(new_task).args:
                self.task_list.appendleft(new_task)
            else:
                raise TypeError("Make sure that the passed function takes no arguments")

        else:
            raise TypeError("Make sure that the passed task is a functon or partial")


    def add_multiple_tasks(self, *new_tasks):
        '''
        adds multiple tasks in order
        '''
        for task in new_tasks:
            self.add_single_task(task)
    def run_next(self):
        '''
        runs the task at the top of the deque

        if the deque is empty raises IndexError

        will not catch any exceptions the task raises

        will also return any return value of the function
        '''
        try:
            next_task = self.task_list.pop()
        except IndexError:
            raise IndexError("No more Tasks to run")

        return next_task()
    def run_all(self):
        while True:
            try:
                self.run_next()
            except IndexError:
                #expected when task list is spent
                break
