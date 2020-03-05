'''
使用"除2"算法，将输入的十进制数字转换成8位2进制数字
'''
# from pythonds.basic.stack import Stack

# def divide2(desNumber):
#     s = Stack()

#     while desNumber > 0:
#         rem = desNumber % 2
#         s.push(rem)
#         desNumber = desNumber//2
    
#     binString = ""
#     while not s.isEmpty():
#         binString = binString + str(s.pop())
    
#     return binString

# print(divide2(233))


'''
八进制，十六进制
'''
from pythonds.basic.stack import Stack

def divideBase(desNumber,base):
    digits = '0123456789ABCDEF'
    s = Stack()

    while desNumber > 0:
        rem = desNumber % base
        s.push(rem)
        desNumber = desNumber // base
    
    binString = ""
    while not s.isEmpty():
        binString = binString + digits[s.pop()]
    
    return binString

print(divideBase(233,2))
print(divideBase(233,8))
print(divideBase(233,16))