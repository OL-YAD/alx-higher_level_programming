#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    nums = [0, 0]
    for i in range(len(tuple_a)):
        if i > 1:
            break
        nums[i] += tuple_a[i]

    for i in range(len(tuple_b)):
        if i > 1:
            break
        nums[i] += tuple_b[i]

    return (nums[0], nums[1])
