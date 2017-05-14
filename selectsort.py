#! /usr/bin/env python
#  coding: utf-8 

def find(seq):
    find_min = seq[0]
    find_index = 0

    for i in range(1, len(seq)):
        if find_min > seq[i]:
            find_min = seq[i]
            find_index = i
    return find_index


def selectsort(seq):
    select_seq = []
    for j in range(len(seq)):
        select_seq.append(seq.pop(find(seq)))

    return select_seq


if __name__ == '__main__':
    test_seq = [2, 0, 1, 7, 5, 1, 6]
    print(selectsort(test_seq))
