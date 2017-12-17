#Given a sorted array with distinct values return index that matches with its value
def magicInd (l):

    if not l:
        return

    return magicIndHelp (l, len(l) - 1)

def magicIndHelp (l, i):

    if (i <= 0):
        return 0
    elif (l[i] == i):
        return i
    else:
        lis =[]
        return magicIndHelp(l, i-1)


print (magicInd([1, 2, 3, 4]))