def answer(x):
    cur = x
    numSum = 0
    while cur > 0:
        numSum += cur % 10
        cur /= 10
    
    if numSum > 9:
        return answer(numSum)
    else:
        return numSum
        