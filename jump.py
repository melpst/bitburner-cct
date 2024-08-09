# input = [2,1,3,2,4,2,1,1,1,4,1,2,1,2,3,5,5]
# input = [2,2,0,4,7,3,3]
# input = [1,5,1,0,9,4]

def isZero(n):
    return n == 0

assert isZero(0) == True
assert isZero(1) == False
assert isZero(2) == False
assert isZero(-1) == False

def isStartWithZero(r):
    return isZero(r[0])

assert isStartWithZero([0,0]) == True
assert isStartWithZero([0,1]) == True
assert isStartWithZero([1,0]) == False
assert isStartWithZero([1,1]) == False
assert isStartWithZero([2,0]) == False
assert isStartWithZero([2,1]) == False
assert isStartWithZero([-1,0]) == False
assert isStartWithZero([-1,1]) == False

def isAllZero(r):
    if len(r)==0:
        return True
    if len(r)==1:
        return isStartWithZero(r)
    else:
        return isStartWithZero(r) and isAllZero(r[1:])
    
assert isAllZero([0,0]) == True
assert isAllZero([0,1]) == False
assert isAllZero([1,0]) == False
assert isAllZero([1,1]) == False
assert isAllZero([2,0]) == False
assert isAllZero([2,1]) == False
assert isAllZero([-1,0]) == False
assert isAllZero([-1,1]) == False
assert isAllZero([0,0,0]) == True
assert isAllZero([0,0,1]) == False
assert isAllZero([0,1,0]) == False
assert isAllZero([1,0,0]) == False
assert isAllZero([1,0,1]) == False
assert isAllZero([1,1,0]) == False
assert isAllZero([1,1,1]) == False

def maxLeapAtIndex(r):
    index = 0
    max = r[index]
    for i in range(1, len(r)):
        if i+r[i] > max:
            index = i
            max = i+r[i]
    return index

assert maxLeapAtIndex([0, 0, 0, 1]) == 3
assert maxLeapAtIndex([2, 1, 1, 1]) == 3
assert maxLeapAtIndex([2, 1, 3, 1]) == 2
assert maxLeapAtIndex([2, 7, 3, 1]) == 1
assert maxLeapAtIndex([7, 3, 1, 1]) == 0

def maxLeapAtIndexRecur(r):
    if len(r)==1:
        return 0
    else:
        index = maxLeapAtIndexRecur(r[1:])+1
        if r[0]>=r[index]+index:
            return 0
        return index

assert maxLeapAtIndexRecur([0, 0, 0, 1]) == 3
assert maxLeapAtIndexRecur([2, 1, 1, 1]) == 3
assert maxLeapAtIndexRecur([2, 1, 3, 1]) == 2
assert maxLeapAtIndexRecur([2, 7, 3, 1]) == 1
assert maxLeapAtIndexRecur([7, 3, 1, 1]) == 0

def next(r):
    if isAllZero(r) or len(r)<=1:
        return 0
    else:
        return maxLeapAtIndexRecur(r)
    
assert next([0,1,2,3]) == 3
assert next([2,1,0]) == 0
assert next([0,0,0]) == 0
assert next([4,1,7,0,2]) == 2
assert next([4,1,7,7,0,7,2]) == 5
assert next([4,1,7,8,0,8,2]) == 5
assert next([4,1,8,2,0,8,2]) == 5
    
def jump(input, length):
    if length==0:
        return 0
    if isAllZero(input) or len(input)<=length:
        return 1
    else:
        n = next(input[:length])
        return jump(input[n+1:], input[n])+1

assert jump([0],0) == 0
assert jump([0, 0],0) == 0
assert jump([0, 1],0) == 0
assert jump([1],1) == 1
assert jump([1, 1],1) == 2
assert jump([2,0,4,7,3,3], 2) == 3

def minJump(input):
    if isAllZero(input) or isStartWithZero(input):
        return 0
    else:
        time = jump(input[1:], input[0])
        return time if time>0 else 0
    
def possibleToEnd(input):
    return bool(minJump(input))

assert minJump([2,1,3,2,4,2,1,1,1,4,1,2,1,2,3,5,5]) == 7
assert minJump([2,2,0,4,7,3,3]) == 3
assert minJump([10,0,8,0,4,10,3,8,9 ,9,1,8,4,7,5,2,4 ,0,0,1]) == 3
assert minJump([4,3,5,3,5 ,3,2,3,3 ,0,4,8 ,2,2,1,6,2,3,2,1]) == 4
assert minJump([0,4,2,1,4,6,1,3,4,0,3,2,4,1,3,2,3]) == 0
assert minJump([3,5,1,5,4,5,1,4,1,3,2,5,1,2,2,1,5,5,5,4,2]) == 5
assert possibleToEnd([1,5,1,0,9,4]) == 1
assert possibleToEnd([0,4,9,5,3,7,7,9,10,7,10,7,9,0,6,1,0]) == 0
assert possibleToEnd([10,0,8,0,4,10,3,8,9,9,1,8,4,7,5,2,4,0,0,1]) == 1
assert possibleToEnd([0,8,1,0,5,7]) == 0
assert possibleToEnd([3,10,1,8,10,6,7,5,0,5,9,1,1,1,8,3,10,5,0,0,10,7,1]) == 1