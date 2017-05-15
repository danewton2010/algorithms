#! /usr/bin/env python
#  coding: utf-8 


def quicksort(seq):
    if len(seq) < 2:
        return seq
    else:
        first = seq[0]
        left = [i for i in seq[1:] if i <= first]
        right = [i for i in seq[1:] if i > first]
        return quicksort(left) + [first] + quicksort(right)


if __name__ == '__main__':
    seq = [4, 3, 2, 1, 7, 6, 8, 9]
    res = quicksort(seq)
    print(res)
