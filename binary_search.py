#! /usr/bin/env python
#  coding: utf-8 

def binary_search(seq, item):
    low = 0
    high = len(seq) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = seq[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        if guess < item:
            low = mid + 1


if __name__ == '__main__':
    seq = [1, 2, 3, 4, 5, 6, 7, 8]
    print(binary_search(seq, 6))
