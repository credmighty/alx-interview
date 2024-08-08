#!/usr/bin/python3
"""minimum operation-- interview"""


def minOperations(n):
    """
      function for the minOperation
      Gets fewest # of operations needed to result in exactly n H characters
    """
    ops, root = 0, 2
    if type(n) != int or n <= 1:
        return 0
    while n != 1:
        if n % root == 0:
            # set n to the remainder
            n = n / root
            ops = ops + root
        else:
            root = root + 1
        # increment root until it evely-divides n
        root += 1
    return ops
