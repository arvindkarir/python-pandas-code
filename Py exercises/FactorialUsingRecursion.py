#Recursion, calling a function within itself
#return calls for n-1, which calls for n-2 and so on
#till it ends in factorial(0), which is 1
def factorial(n):
    if n == 0:
        return 1
    elif n <0:
        return "no answer"
    else:
        return n * factorial(n-1)
