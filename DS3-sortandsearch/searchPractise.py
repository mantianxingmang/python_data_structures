'''
**练习**：
写一个函数，该函数需要一个列表和我们正在搜索的项作为参数，
并返回一个是否存在的布尔值。found = False
'''
# def sequentialSearch(alist,item):
#     found = False
#     pos = 0

#     while pos<len(alist) and not found:
#         if alist[pos] == item:
#             found = True
#         else:
#             pos = pos + 1

#     return found

# testList = [1,2,300,7,23,42,90]
# print(sequentialSearch(testList,90))
# print(sequentialSearch(testList,100))

# 在   最好的情况？1   最差的情况是什么？n       O(n)
# 不在  n  n


'''
    升序 [17,20,26,30,44,54,55,65,77,93]
    假设寻找的项在列表中，
    假设寻找的项不在列表中，50
'''
# def orderedSequentialSearch(alist,item):
#     pos = 0
#     found = False
#     stop = False

#     while pos<len(alist) and not found and not stop:
#         if alist[pos] == item:
#             found = True
#         else:
#             if alist[pos] > item:
#                 stop = True
#             else:
#                 pos = pos + 1
    
#     return found

# testList = [17,20,26,30,44,54,55,65,77,93]
# print(orderedSequentialSearch(testList,50))

# 在    1   n      O(n)
# 不在  1   n

'''
    有序列表
    二分查找：每次都从剩余项中的中间元素进行比对
'''
# def binarySearch(alist,item):
#     found = False
#     first = 0
#     last = len(alist) - 1

#     while first<=last and not found:
#         # 中间
#         midpoint = (first+last)//2
#         if alist[midpoint] == item:
#             found = True
#         else:
#             if item < alist[midpoint]:
#                 last = midpoint - 1
#             else:
#                 first = midpoint + 1
    
#     return found

# testList = [0,1,2,8,13,17,19,32,42]
# print(binarySearch(testList,3))


#  递归实现二分查找
def binarySearch(alist,item):
    if len(alist) == 0:
        return False
    midpoint = len(alist)//2
    if alist[midpoint] == item:
        return True
    else:
        if alist[midpoint] > item:
            return binarySearch(alist[:midpoint],item)
        else:
            return binarySearch(alist[midpoint+1:],item)


testList = [0,1,2,8,13,17,19,32,42]
print(binarySearch(testList,13))


# n/2   n/4   n/8 ....   n/2^i   O(logn)