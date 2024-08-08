#!/usr/bin/python3
"""minimum operation-- interview"""


def minOperations(n):
    """
	  function for the minOperation
	  Gets fewest # of operations needed to result in exactly n H characters
	"""
    op, root = 0, 2
    while root <= n:
        # in n evely divides by root
        if n % root == 0:
            # total even-division by tal operations
            op += root
            # set n to the remainder
            n = n / root
            # reduce root to find remaining smaller values that evenly-div n
            root -= 1
        # increment root until it evely-divides n
        root += 1
	return op
