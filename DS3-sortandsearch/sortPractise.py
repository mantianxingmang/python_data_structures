'''
           [54,26,93,17,77,31,44,55,20]   长度为9
    第1趟： [26,54,93,17,77,31,44,55,20]  54和26交换
    第2趟： [26,54,93,17,77,31,44,55,20]  未交换
    第3趟： [26,54,17,93,77,31,44,55,20]  93和17交换
    第4趟： [26,54,17,77,93,31,44,55,20]  93和77交换
    第5趟： [26,54,17,77,31,93,44,55,20]  93和31交换
    第6趟： [26,54,17,77,31,44,93,55,20]  93和44交换
    第7趟： [26,54,17,77,31,44,55,93,20]  93和55交换
    第8趟： [26,54,17,77,31,44,55,20,93]  93和20交换
    
    列表中有n项，那第一遍比对需要n-1次，第二遍n-2...
    8遍 n-1遍
    
'''
# a和b交换
# a = 10
# b = 20
# temp = a
# a = b
# b = temp
# print(a)
# print(b)

# def bubbleSort(alist):
#     for passnum in range(len(alist)-1,0,-1):
#         for i in range(passnum):
#             if alist[i] < alist[i+1]:
#                 temp = alist[i]
#                 alist[i] = alist[i+1]
#                 alist[i+1] = temp

# alist = [54,26,93,17,77,31,44,55,20]
# bubbleSort(alist)
# print(alist)

'''短冒泡排序'''
# def bubbleSort(alist):
#     flag = True
#     passnum = len(alist) - 1
    
#     while passnum>0 and flag:
#         flag = False
#         for i in range(passnum):
#             if alist[i] > alist[i+1]:
#                 flag = True
#                 temp = alist[i]
#                 alist[i] = alist[i+1]
#                 alist[i+1] = temp
        
#         passnum = passnum - 1

# alist = [54,26,93,17,77,31,44,55,20]
# bubbleSort(alist)
# print(alist)

'''
    选择排序
'''
# def selectionSort(alist):
#     for fillsort in range(len(alist)-1,0,-1):
#         maxPos = 0
#         for location in range(1,fillsort+1):
#             if alist[location] > alist[maxPos]:
#                 maxPos = location
        
#         temp = alist[fillsort]
#         alist[fillsort] = alist[maxPos]
#         alist[maxPos] = temp

# alist = [54,26,93,17,77,31,44,55,20]
# selectionSort(alist)
# print(alist)


'''
    插入排序
'''
# def insertionSort(alist):
#     for i in range(1,len(alist)):
#         currentValue = alist[i]
#         pos = i
#         while pos > 0 and alist[pos -1]>currentValue:
#             alist[pos] = alist[pos -1]
#             pos = pos -1
        
#         alist[pos] = currentValue

# alist = [54,26,93,17,77,31,44,55,20]
# insertionSort(alist)
# print(alist)


'''
    希尔排序
'''
def shellSort(alist):
    sublistcount = len(alist)//2

    while sublistcount > 0:
        for startposition in range(sublistcount):
            gapInsertionSort(alist,startposition,sublistcount)
    
        print('alist：',alist)

        sublistcount = sublistcount//2

def gapInsertionSort(alist,start,gap):
    for i in range(start+gap,len(alist),gap):
        currentValue = alist[i]
        
        pos = i
        while pos >= gap and alist[pos-gap]>currentValue:
            alist[pos] = alist[pos -gap]
            pos = pos - gap
        
        alist[pos] = currentValue

alist = [54,26,93,17,77,31,44,55,20]
shellSort(alist)
print(alist)