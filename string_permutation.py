# Permutation possible for a given string of unique characters
from itertools import chain


def rev_rotate(string):
    return string[-1:] + string[:-1]


def swap(string, i, j):
    lis = list(string)
    lis[i], lis[j] = lis[j], lis[i]
    return ''.join(lis)


def permutation(stn):
    if stn is None:
        return

    n = len(stn)
    permut = []
    for i in range(n):
        new_str = swap(stn, 0, i)
        permut.append(permutation_help(new_str, rev_rotate(new_str)))

    final_lis = list(chain(*permut))
    final_lis = list(set(final_lis))

    return final_lis

temp_lis = []


def permutation_help(stn, mod_stn):

    temp_lis.append(mod_stn)
    if stn != mod_stn:
        permutation_help(stn, rev_rotate(mod_stn))

    return temp_lis


strn = 'ABC'
print(permutation(strn))
