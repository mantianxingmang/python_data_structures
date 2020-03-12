'''
    列表表示
'''
# myTree = ['a',['b',['d',[],[]],['e',[],[]]],['c',['f',[],[]],[]]]

# print('左树：',myTree[1])
# print('根节点：',myTree[0])
# print("右树：",myTree[2])


'''
    抽象数据类型  ADT或者节点表示方式
'''
# class BinaryTree:
#     def __init__(self,rootObj):
#         self.key = rootObj
#         # 新树的根节点
#         self.leftChild = None
#         self.rightChild = None
    
#     # 插入左树
#     def insertLeft(self,newMode):
#         if self.leftChild == None:
#             self.leftChild = BinaryTree(newMode)
#         else:
#             temp = BinaryTree(newMode)
#             temp.leftChild = self.leftChild
#             self.leftChild = temp 

#     # 插入右树
#     def insertRight(self,newMode):
#         if self.rightChild == None:
#             self.rightChild = BinaryTree(newMode)
#         else:
#             temp = BinaryTree(newMode)
#             temp.rightChild = self.rightChild
#             self.rightChild = temp 


#     def setRootVal(self,obj):
#         self.key = obj
#     def getRootVal(self):
#         return self.key
#     def getLeftChild(self):
#         return self.leftChild
#     def getRightChild(self):
#         return self.rightChild


# r = BinaryTree('a')
# print(r.getRootVal())
# print(r.getLeftChild())
# r.insertLeft('b')
# print(r.getLeftChild())
# print(r.getLeftChild().getRootVal())
# r.insertRight('c')
# print(r.getRightChild())
# print(r.getRightChild().getRootVal())
# r.getRightChild().setRootVal('hello')
# print(r.getRightChild().getRootVal())

'''
    分析树 ( 3 + （ 4 * 5 ）） => ['(','3','+','(','4','*','5',')',')']
'''
# from pythonds.basic.stack import Stack
# from pythonds.trees.binaryTree import BinaryTree
# import operator

# def buildParseTree(fpexp):
#     fplist = fpexp.split()
#     pStack = Stack()
#     eTree = BinaryTree('')
#     pStack.push(eTree)
#     currentTree = eTree

#     for i in fplist:
#         if i == '(':
#             currentTree.insertLeft('')
#             pStack.push(currentTree)
#             currentTree = currentTree.getLeftChild()
#         elif i not in ['+','-','*','/',')']:
#             currentTree.setRootVal(int(i))
#             parent = pStack.pop()
#             currentTree = parent
#         elif i in ['+','-','*',"/"]:
#             currentTree.setRootVal(i)
#             currentTree.insertRight('')
#             pStack.push(currentTree)
#             currentTree = currentTree.getRightChild()
#         elif i == ')':
#             currentTree = pStack.pop()
#         else:
#             raise ValueError
#     return eTree

# def evaluate(parseTree):
#     opers = {
#         '+':operator.add,
#         '-':operator.sub,
#         '*':operator.mul,
#         '/':operator.truediv
#     }
#     leftC = parseTree.getLeftChild()
#     rightC = parseTree.getRightChild()

#     if leftC and rightC:
#         fn = opers[parseTree.getRootVal()]
#         return fn(evaluate(leftC),evaluate(rightC))
#     else:
#         return parseTree.getRootVal()


# pt = buildParseTree('( 3 + ( 4 * 5 ) )')
# # pt.postorder()

# print(evaluate(pt))


'''
    树的遍历
'''
# def preOrder(tree):
#     if tree:
#         print(tree.getRootVal())
#         print(tree.getLeftChild())
#         print(tree.getRightChild())

# 前序
def preOrder(self):
    print(self.key)
    if self.leftChild:
        self.leftChild.preOrder()
    if self.rightChild:
        self.rightChild.preOrder()

# 后序
def postorder(tree):
    if tree != None:
        postorder(tree.getLeftChild())
        postorder(tree.getRightChild())
        print(tree.getRootVal())

from pythonds.trees.binaryTree import BinaryTree
# 中序
def inorder(tree):
    if tree != None:
        inorder(tree.getLeftChild())
        print(tree.getRootVal())
        inorder(tree.getRightChild())



def printExp(tree):
    sVal = ""
    if tree:
        sVal = '('+printExp(tree.getLeftChild())
        sVal = sVal + str(tree.getRootVal())
        sVal = sVal + printExp(tree.getRightChild())+')'
    return sVal

print(printExp(pt))
