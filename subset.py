# subset within a list(incorrect understanding of solution
def subset(l):

    if not l:
        return

    n = len(l)
    final = []
    samp = list(l)

    for i in range(n):
        final.append(subset_help(samp, l[i]))
        #print(final)
        del samp[0]

    return final


def subset_help(lis, elem):

    #print(lis)
    newlist = list(lis)
    n = len(lis) - 1
    if newlist[n] == elem and n == 0:
        return newlist
    else:
        temp = []
        temp.append(newlist)
        temp.append(subset_help(newlist[0:n], elem))

        return temp


print(subset([1, 2, 3, 4]))
