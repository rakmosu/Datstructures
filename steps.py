#Possible ways of Climbing the stairs when you can take only 1 or 2 or 3 steps at a time
def totSteps (n):

    if (n <= 0 or not n):
        return 0

    if (n == 1):
        return 1
    elif (n == 2):
        return 2
    elif (n == 3):
        return 4
    else:
         return totSteps(n - 1) + totSteps(n - 2) + totSteps(n - 3)


print (totSteps(5))
