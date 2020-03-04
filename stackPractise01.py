# 栈抽象数据类型的底层实现采用什么？   list
# 确定列表的哪一端是顶部，然后使用append和pop来实现操作

# 假设列表的尾部是栈的顶部元素，push
# class Stack:
#     def __init__(self):
#         self.items = []

#     def isEmpty(self):
#         return self.items == []
    
#     def push(self,item):
#         self.items.append(item)

#     def pop(self):
#         return self.items.pop()
    
#     def peek(self):
#         return self.items[len(self.items)-1]
    
#     def size(self):
#         return len(self.items)




# from pythonds.basic.stack import Stack

# s = Stack()

# print(s.isEmpty())
# s.push(4)
# s.push('lalla')

# print(s.peek())

# s.push(True)

# print(s.size())

# print(s.isEmpty())

# s.push(10.9)
# print(s.pop())
# print(s.pop())
# print(s.size())




# （）匹配
from pythonds.basic.stack import Stack

#  symbolString  假设 “（（））”
def parChecker(symbolString):
    s = Stack()
    flag = True
    index = 0

    while index < len(symbolString) and flag:
        symbol = symbolString[index]
        if symbol == "(":
            s.push(symbol)
        else:
            if s.isEmpty():
                flag = False
            else:
                s.pop()

        index = index + 1

    if flag and s.isEmpty():
        return True
    else:
        return False


print(parChecker('(())'))
print(parChecker('((())'))
