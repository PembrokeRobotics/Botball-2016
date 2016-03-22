import collections
import types
import inspect

class Tasker(object):
    '''
    class to simplify running tasks in order
    '''
    def __init__(self):
        self.task_list = collections.deque()
    def add_single_task(self, new_task):
        '''
        add a task to the task list

        new_task must be a function and that function must take zero argss
        '''
        if type(new_task) == types.FunctionType and \
                             not inspect.getargspec(new_task).args:

            self.task_list.appendleft(new_task)
        else:
            raise TypeError("please make sure that the task is a function \
                             and that that function takes zero args")
    def add_multiple_tasks(self, *new_tasks):
        '''
        adds multiple tasks in order
        '''
        for task in new_tasks:
            if type(task) == types.FunctionType and \
                             not inspect.getargspec(task).args:
                self.task_list.append(task)
    def run_next(self):
        '''
        runs the task at the top of the deque

        if the deque is empty raises IndexError

        will not catch any exceptions the task raises
        '''
        try:
            next_task = self.task_list.pop()
        except IndexError:
            raise IndexError("No more Tasks to run")

        next_task()
    def run_all(self):
        while True:
            try:
                self.run_next()
            except IndexError:
                #expected when task list is spent
                break
