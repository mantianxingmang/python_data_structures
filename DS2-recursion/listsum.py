'''
[1,3,5,7,9]
'''
def listSum(numList):
    sum = 0
    for i in numList:
        sum = sum + i
    
    return sum

print(listSum([1,3,5,7,9]))


#不能使用while或者for
#使用小学的内容：连加
#（1+3） = （4+5）= （9+7）= 16+9 = 25
#（1+（3+（5+（7+9））））
#     （1+（3+（5+16）））
#           （1+（3+21））
#                 （1+24）
#                      25

'''
    listSum2([1,3,5,7,9])
= 1 + listSum2([5,7,9])
= 3 + listSum2([5,7,9])
= 5 + listSum2([7,9])
= 7 + listSum2([9])
'''
def listSum2(numList):
    if len(numList) == 1:
        return numList[0]
    else:
        return numList[0] + listSum2(numList[1:])

print(listSum2([1,3,5,7,9]))






def toStr(n,base):
    str1 = '0123456789ABCDEF'

    if n < base:
        return str1[n]
    else:
        return toStr(n//base,base) + str1[n%base]


print(toStr(100,10)) 

'''
toStr(10,10) + '0'
toStr(1,10) + '0'
'1'
'''

#栈 实现递归
from pythonds.basic.stack import Stack

rStack = Stack()

def toStr(n,base):
    convertString = "0123456789ABCDEF"

    while n > 0:
        if n < base:
            rStack.push(convertString[n])
        else:
            rStack.push(convertString[n % base])

        n = n // base
    res = ""

    while not rStack.isEmpty():
        res = res + str(rStack.pop())
    return res

print(toStr(1453,16))


