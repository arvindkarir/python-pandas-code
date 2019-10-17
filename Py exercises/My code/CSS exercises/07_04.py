# find max list 07_04



def maxSum(l):
    splitPt = len(l)//2
    leftList = l[0:splitPt]
    rightList = l[splitPt:]
    if len(l) == 0:
        return 0
    elif len(l) == 1:
        return max(l[0],0)
    maxLeft = maxSum(leftList)
    maxRight = maxSum(rightList)
    lefthalf = maxSum(leftList)
    righhalf = maxSum(rightList)

    print(maxLeft, maxRight)
    print(lefthalf, righthalf)



l = [-2,1,-3,3,-1,2,1,-5,4]
#l = [-1,2,-5,1]
#l = [1, 2, 3]



maxSum(l)

#https://stackoverflow.com/questions/17542779/generative-recursion-to-find-the-sublist-with-the-maximum-sum
#def sum_max(L, accum=0, max_value=0):
#    if not L:
#        return max_value
#    accum += L[0]
#    return sum_max(L[1:], accum, max(max_value, accum))
#
#def find_max(L):
#    ...
#    left_half = sum_max(L[mid_index-1::-1])
#    right_half = sum_max(L[mid_index:])
#    ...