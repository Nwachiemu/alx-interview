#!/usr/bin/python3
'''The minimum operations coding challenge'''


def minOperations(n):
    '''Computes the fewest number of operations needed to result
    in exactly n H characters'''
    if not isinstance(n, int):
        return 0
    copy = 0
    clipboard = 0
    paste = 1

    while paste < n:
        if clipboard == 0:

            clipboard = paste
            paste += clipboard
            copy += 2

        elif n - paste > 0 and (n - paste) % paste == 0:

            clipboard = paste
            paste += clipboard
            copy += 2

        elif clipboard > 0:

            paste += clipboard
            copy += 1

    return copy
