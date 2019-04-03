"""
Test 3, problem 4.

Authors: Sriram Mohan, Dr. Brackin and 
         PUT YOUR NAME HERE.
         April, 2019
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE. (-1 pt if you do NOT)


import time
import testing_helper


def main():
    """ Calls the   TEST   functions in this module. """
    test_problem4()


###############################################################################
# TODO: 2.  READ the doc-string for the   is_prime   function defined below.
# It is the same as you have seen before.
# After you UNDERSTAND the doc-string (JUST the doc-string, NOT the code),
# ASKING QUESTIONS AS NEEDED, change the above _TODO_ to DONE.
###############################################################################
def is_prime(n):
    """
    What comes in:  An integer n.
    What goes out:
      -- Returns True if the given integer is prime,
                 False if the given integer is NOT prime.
         Treats integers less than 2 as NOT prime.
    Side effects:   None.
    Examples:
      -- is_prime(11) returns  True
      -- is_prime(12) returns  False
      -- is_prime(2)  returns  True
      -- is_prime(1)  returns  False
    Note: The algorithm used here is simple and clear but slow.
    """
    if n < 2:
        return False
    for k in range(2, (n // 2) + 1):
        if n % k == 0:
            return False

    return True
    # ------------------------------------------------------------------
    # Students:
    #   Do NOT touch the above  is_prime  function - it has no TO DO.
    #   Do NOT copy code from this function.
    #
    # Instead, ** CALL ** this function as needed in the problems below.
    # ------------------------------------------------------------------



def test_problem4():
    """ Tests the    problem1    function. """
    # ------------------------------------------------------------------
    # We supplied tests for this function.
    # ------------------------------------------------------------------
    print()
    print('--------------------------------------------------')
    print('Testing the   problem4   function:')
    print('--------------------------------------------------')

    problem4()


def problem4():
    """
    Prompts the user for and inputs:
      -- A string
      -- An integer
      -- Another string
    in that order (via three separate inputs).

    Then prints, in this order, all on separate lines:
      -- If the integer you printed is prime, prints
            'The integer you entered is prime!'
      -- If the integer you entered is NOT prime, prints
            ' I love prime numbers, please enter one next time.'
      -- The SECOND of the two strings
      -- All numbers from zero upto the integer(inclusive) (all on one
          line, with one : between them)
      -- The FIRST of the two strings FOLLOWED by the SECOND of the
           two strings (all on one line, with one space in between them).

    No input validation is required.  Nothing else should be printed.

    Here is a sample run, where the user input is to the right
    of the colons:
        Enter a string: I went skiing!
        Enter a integer: 2
        Enter another string: Mickey Mouse
        The integer you entered is prime!
        Mickey Mouse
        0:1:2
        I went skiing! Mickey Mouse
    Here is another sample run, where the user input is to the right
    of the colons:
        Enter a string: I went hiking!
        Enter a integer: 6
        Enter another string: Jack
        I love prime numbers, please enter one next time
        Jack
        0:1:2:3:4:5:6
        I went hiking! Jack
    """
    # -----------------------------------------------------------------
    # TODO: Implement and test this function.
    #       The testing code is already written for you (above).
    # -----------------------------------------------------------------

# ----------------------------------------------------------------------
# Calls main to start the ball rolling.
#   More precisely, calls main only if this module is running at the
#   top level (as opposed to being imported by another module).
#   This structure helps us automate tests of this module.
# ----------------------------------------------------------------------


if __name__ == '__main__':
    main()
