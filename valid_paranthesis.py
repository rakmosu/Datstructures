from itertools import chain


def swap(string, i, j):
    lis = list(string)
    lis[i], lis[j] = lis[j], lis[i]
    return ''.join(lis)


def valid_par(n):

    if n == 0 or n is None:
        return

    strn = ''
    strn2 = ''
    final = []

    for i in range(2*n):
        if i < n:
           strn = strn + '('
           strn2 = strn2 + '()'
        else:
            strn = strn + ')'

    final.append(valid_par_help(strn, n))

    if n % 2 != 0:

        final.append(valid_par_help_rev_odd(strn2, n))
    else:
        final.append(valid_par_help_rev_even(strn2, n))

    final1 = list(chain(*final))
    final1 = list(set(final1))

    return final1

temp =[]


def valid_par_help(strn, n):

    if strn[0:2] == '()':
        return strn[0:2]
    else:
        m = n - 1
        k = (2 * n) - 2
        temp.append(strn)
        strn = swap(strn, m, k)
        temp.append(strn)
        valid_par_help(strn, m)

        return list(set(temp))


def valid_par_help_rev_odd(strn, n):

    if strn[0:2] == '((':
        return strn[0:2]
    else:

        m = n + 1
        strn = swap(strn, n, m)
        temp.append(strn)
        n = n - 1
        valid_par_help_rev_odd(strn, n)

        return list(set(temp))

def valid_par_help_rev_even(strn, n):

    if strn[0:2] == '((':
        return strn[0:2]
    else:
        m = n - 1
        strn = swap(strn, m, n)
        temp.append(strn)
        n = n - 1
        valid_par_help_rev_even(strn, n)
        return list(set(temp))

print(valid_par(4))
