'''
unittest for tasker.py
'''
import unittest
import tasker
import functools

class TestTaskerSystem(unittest.TestCase):
    '''
    runs unittests on the Tasker class
    '''
    def test_adding_single_function_with_no_args(self):
        '''
        makes sure that you can add a single function that correctly
        has no arguments
        '''
        task_manager = tasker.Tasker()

        def test_function():
            return 1

        task_manager.add_single_task(test_function)
        self.assertEqual(task_manager.run_next(), 1)
    def test_adding_multiple_functions_with_no_args(self):
        '''
        adds multiple functions that have no arguments and makes sure
        that the tasks are run in the correct order
        '''
        task_manager = tasker.Tasker()

        def test_function_1():
            return 1
        def test_function_2():
            return 2

        task_manager.add_multiple_tasks(test_function_1,
                                        test_function_2,
                                        test_function_1,
                                        test_function_1)

        expected_values = [1, 2, 1, 1]
        actual_values   = []

        actual_values.append(task_manager.run_next())
        actual_values.append(task_manager.run_next())
        actual_values.append(task_manager.run_next())
        actual_values.append(task_manager.run_next())

        self.assertEqual(expected_values,
                         actual_values)

    def test_adding_single_function_with_args(self):
        '''
        adds a function that has arguments and makes sure a TypeError is
        raised
        '''

        task_manager = tasker.Tasker()

        def function_with_args(argument):
            return argument

        with self.assertRaises(TypeError):
            task_manager.add_single_task(function_with_args)

    def test_adding_multiple_functions_with_args(self):
        '''
        adds multiple functions, one of which takes arguments,
        and makes sure that a TypeError is raised
        '''
        task_manager = tasker.Tasker()

        def function_without_args():
            return 1

        def function_with_args(argument):
            return argument

        with self.assertRaises(TypeError):
            task_manager.add_multiple_tasks(function_without_args,
                                            function_with_args,
                                            function_without_args)

    def test_adding_single_partial_without_args(self):
        '''
        adds a single partial that correctly has no arguments
        '''

        task_manager = tasker.Tasker()

        def function_with_args(argument):
            return argument

        #this partial should return 1 with no args
        partial_function = functools.partial(function_with_args, 1)


        task_manager.add_single_task(partial_function)
        self.assertEqual(task_manager.run_next(), 1)

    def test_adding_multiple_partials_with_no_args(self):
        '''
        adds multiple partials that have no arguments and makes sure
        that the tasks are run in the correct order
        '''
        task_manager = tasker.Tasker()

        def function_with_args(argument):
            return argument

        test_partial_1 = functools.partial(function_with_args, 1)
        test_partial_2 = functools.partial(function_with_args, 2)

        task_manager.add_multiple_tasks(test_partial_1,
                                        test_partial_2,
                                        test_partial_1,
                                        test_partial_1)

        expected_values = [1, 2, 1, 1]
        actual_values   = []

        actual_values.append(task_manager.run_next())
        actual_values.append(task_manager.run_next())
        actual_values.append(task_manager.run_next())
        actual_values.append(task_manager.run_next())

        self.assertEqual(expected_values,
                         actual_values)

    def test_adding_single_partial_with_args(self):
        '''
        adds a single partial that incorrectly has unfilled arguments
        and makes sure a TypeError is raised
        '''

        task_manager = tasker.Tasker()

        def function_with_two_args(argument_1, argument_2):
            return argument_1 + argument_2

        #this partial should return 1 with no args
        partial_function = functools.partial(function_with_two_args, 1)


        with self.assertRaises(TypeError):
            task_manager.add_single_task(partial_function)

    def test_adding_multiple_partials_with_args(self):
        '''
        adds multiple partials, one of which accepts nonzero args
        and makes sure that the proper TypeError is raised
        '''

        task_manager = tasker.Tasker()

        def function_with_one_arg(argument):
            return argument

        def function_with_two_args(argument_1, argument_2):
            return argument_1 + argument_2

        test_partial_with_one_arg = functools.partial(function_with_one_arg,  1)
        test_partial_with_no_args = functools.partial(function_with_two_args, 1)

        with self.assertRaises(TypeError):
            task_manager.add_multiple_tasks(test_partial_with_no_args,
                                            test_partial_with_no_args,
                                            test_partial_with_one_arg,
                                            test_partial_with_no_args)

    def test_end_of_task_list(self):
        '''
        adds some tasks and runs through them, making sure that afterwords
        the task manager will raise an IndexError if a new task is requested
        '''
        task_manager = tasker.Tasker()

        def test_function_1():
            return 1

        task_manager.add_single_task(test_function_1)
        task_manager.add_single_task(test_function_1)
        task_manager.add_single_task(test_function_1)

        task_manager.run_next()
        task_manager.run_next()
        task_manager.run_next()

        with self.assertRaises(IndexError):
            task_manager.run_next()

    def test_run_all(self):
        '''
        adds some tasks then uses run_all to run them all, then sees if the
        task list is spent
        '''
        task_manager = tasker.Tasker()

        def test_function_1():
            return 1

        task_manager.add_single_task(test_function_1)
        task_manager.add_single_task(test_function_1)
        task_manager.add_single_task(test_function_1)

        task_manager.run_all()

        with self.assertRaises(IndexError):
            task_manager.run_next()
