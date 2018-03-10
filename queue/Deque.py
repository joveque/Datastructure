# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 16:21:07 2018

@author: joveque
"""

'''
实现双端队列deque
双端队列（deque，全名double-ended queue）是一种具有队列和栈性质的线性数据结构。
双端队列也拥有两端：队首（front）、队尾（rear），
但与队列不同的是，插入操作在两端（队首和队尾）都可以进行，删除操作也一样。
两种方式的不同主要体现在性能上
操作|实现方式  list  collections.deque（标准库）
-----------------------------------------
addFront    O(n)  O(1)
-----------------------------------------
addRear     O(1)  O(1)
-----------------------------------------
removeFront   O(n)  O(1)
-----------------------------------------
removeRear   O(1)  O(1)
'''

#使用内建类型list
class LDeque():
    def __init__(self):
        self.items = []
    
    #向队首插入项
    def addFront(self, item):
        self.items.insert(0, item)
    
    #向队尾插入项
    def addRear(self, item):
        self.items.append(item)
    
    #返回队首的项，并从双端队列中删除该项
    def removeFront(self):
        return self.items.pop(0)
    
    #返回队尾的项，并从双端队列中删除该项
    def removeRear(self):
        return self.items.pop()
    
    #判断双端队列是否为空
    def empty(self):
        return self.size() == 0
    
    #返回双端队列中项的个数
    def size(self):
        return len(self.items)
    
    
#使用标准库collections.deque
from collections import deque
class CDeque:
    def __init__(self):
        self.items = deque()
        
    def addFront(self, item):
        self.items.appendleft(item)
        
    def addRear(self, item):
        self.items.append(item)
        
    def removeFront(self):
        return self.items.popleft()
    
    def removeRear(self):
        return self.items.pop()
    
    def empty(self):
        return self.size() == 0
    
    def size(self):
        return len(self.items)
    
#使用deque回文验证算法
def palchecker(aString):
    chardeque = LDeque()
    for ch in aString:
        chardeque.addRear(ch)
    while chardeque.size() > 1:
        first = chardeque.removeFront()
        last = chardeque.removeRear()
        if first != last:
            return False
    return True
if __name__ == '__main__':
    str1 = 'able was i ere i saw elba'
    print('"%s" is%s palindrome' % (str1, '' if palchecker(str1) else ' not'))
    str2 = u'人人为我、我为人人'     #u代表是对字符串进行unicode编码
    print(u'"%s"%s是回文' % (str2, u'' if palchecker(str2) else u'不'))
    str3 = u"What's wrong 怎么啦"
    print(u'"%s"%s是回文' % (str3, u'' if palchecker(str3) else u'不'))

    
    






























