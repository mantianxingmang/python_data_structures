class Deque:

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addFront(self, item):
        self.items.append(item)

    def addRear(self, item):
        self.items.insert(0,item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)


#from collections import deque
from pythonds.basic.deque import Deque

def palChecker(aString):
    chardeque = Deque()
    for ch in aString:
        chardeque.addRear(ch)
    flag = True

    while chardeque.size() > 1 and flag:
        first = chardeque.removeFront()
        last = chardeque.removeRear()

        if first != last:
            flag = False
    
    return flag

print(palChecker("山西运煤车煤运山西"))
