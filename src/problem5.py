"""
Exam 3, problem 5.

Authors: All CSSE Faculty,Dr. Brackin, and 
         PUT_YOUR_NAME_HERE.  
         April, 2019.

"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE. (-1 pt if you do NOT)
####################################################################
# TODO: 2. Commit and push this file- NOW.
#          You will be penalized severely if you do NOT follow instructions
# 1 Points
####################################################################

import time
import testing_helper


def main():
    """ Calls the   TEST   functions in this module. """
    run_test_problem5()


def run_test_problem5():
    """ Tests the  problem5   function. """
    ####################################################################
    # THESE TESTS ARE ALREADY DONE.  DO NOT CHANGE THEM.
    ####################################################################
    print()
    print('--------------------------------------------------')
    print('Testing the   problem5   function:')
    print('--------------------------------------------------')

    format_string = '    problem5( {} )'
    test_results = [0, 0]  # Number of tests passed, failed.

    # Test 1:
    sequence = [['a','b','c'], ['z', 'd'], []]
    expected = ['c', 'z']
    print_expected_result_of_test([sequence], expected,
                                  test_results, format_string)
    actual = problem5(sequence)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 2:
    sequence = [['w', 'y'], ('z', 'a')]
    expected = ['y', 'z']
    print_expected_result_of_test([sequence], expected,
                                  test_results, format_string)
    actual = problem5(sequence)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 3:
    sequence = [('d', 'p'),
                ('g', 'j', 'b', 'k', 'l'),
                ('f', 'm', 'z', 'o'),
                ('e', 'a'),
                (),
                ('r', 'r', 'c')
                ]
    expected = ['p', 'l', 'z', 'e', 'r']
    print_expected_result_of_test([sequence], expected,
                                  test_results, format_string)
    actual = problem5(sequence)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 4:
    sequence = (['a'], [], ['b', 'h'])
    expected = ['a', 'h']
    print_expected_result_of_test([sequence], expected,
                                  test_results, format_string)
    actual = problem5(sequence)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 5:
    sequence = ([], [], [])
    expected = []
    print_expected_result_of_test([sequence], expected,
                                  test_results, format_string)
    actual = problem5(sequence)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # SUMMARY of the test results:
    print_summary_of_test_results(test_results)


def problem5(seq_of_seq):
    """
    What comes in:
      -- A sequence of sub-sequences of characters.
    What goes out:
      -- Returns a NEW list containing largest character of each sequence.
      If one of the original sub-sequences were empty, it has no largest character,
      so contributes characters to the returned list.  For our purposes, only
      lower case characters will be used.
      Characters are ordered such that a < b < c <....<z
    Side effects:  None.
    Examples:
    sequence = [('d', 'p'),
                ('g', 'j', 'b', 'k', 'l'),
                ('f', 'm', 'z', 'o'),
                ('e', 'a'),
                (),
                ('r', 'r', 'c')
                ]
                returns ['p', 'l', 'z', 'e', 'r']

      sequence =( ['a'], [], ['b', 'h'] ) returns ['a', 'h']
      sequence =( ['a','b','c'], ['z', 'd'], []) returns ['c', 'z']
      problem5( [[], [], [] )          returns []


    Type hints:
      :type seq_of_seq: list of list of str
      :rtype: (list of characters) | str
    """
    # -------------------------------------------------------------------------
    # TODO: 3. Implement and test this function.
    #          Tests have been written for you (above).
    #
    # 14 Points
    # -------------------------------------------------------------------------


###############################################################################
# Our tests use the following to print error messages in red.
# Do NOT change it.  You do NOT have to do anything with it.
###############################################################################

def print_expected_result_of_test(arguments, expected,
                                  test_results, format_string):
    testing_helper.print_expected_result_of_test(arguments, expected,
                                                 test_results,
                                                 format_string)


def print_actual_result_of_test(expected, actual, test_results):
    testing_helper.print_actual_result_of_test(expected, actual,
                                               test_results)


def print_summary_of_test_results(test_results):
    testing_helper.print_summary_of_test_results(test_results)


# To allow color-coding the output to the console:
USE_COLORING = True  # Change to False to revert to OLD style coloring

testing_helper.USE_COLORING = USE_COLORING
if USE_COLORING:
    # noinspection PyShadowingBuiltins
    print = testing_helper.print_colored
else:
    # noinspection PyShadowingBuiltins
    print = testing_helper.print_uncolored

# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# The   try .. except   prevents error messages on the console from being
# intermingled with ordinary output to the console.
# -----------------------------------------------------------------------------
try:
    main()
except Exception:
    print('ERROR - While running this test,', color='red')
    print('your code raised the following exception:', color='red')
    print()
    time.sleep(1)
    raise