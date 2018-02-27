# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 12:08:03 2018

@author: joveque
"""

class Node:
    def __init__(self, initdata):
        self.__data = initdata
        self.__next = None
    
    def getdata(self):
        return self.__data
    
    def getnext(self):
        return self.__next
    
    def setdata(self, newdata):
        self.__data = newdata
        
    def setnext(self, newnext):
        self.__next = newnext
        
class Sincyclelist:
    def __init__(self):
        self._head = Node(None)
        self._head.setnext(self._head)
        
    # 向链表中插入数据项
    def add(self, item):
        temp = Node(item)
        temp.setnext(self._head.getnext())  #因为开始head是循环的
        self._head.setnext(temp)
        
    #删除链表中的数据项
    def remove(self, item):
        pre = self._head
        while pre.getnext() != self._head:
            cur = pre.getnext()
            #先判断每一个阶段pre的下一个（即cur）是否为item
            if cur.getdata() == item:
                pre.setnext(cur.getnext())
            #然后再不断令pre向前进
            pre = pre.getnext()
            
    #在链表中查找数据项是否存在
    def search(self, item):
        cur = self._head.getnext()  #与单链表的不同之处
        while cur != self._head:
            #每一循环先判断
            if cur.getdata() == item:
                return True
            #然后再前进
            cur = cur.getnext()
        return False
    
    #判断链表是否为空
    def empty(self):
        return self._head.getnext() == self._head
    
    #返回链表中数据项的个数
    def size(self):
        count = 0
        cur = self._head.getnext()
        while cur != self._head:
            count += 1
            cur = cur.getnext()
        return count
    
if __name__ == '__main__':
  s = Sincyclelist()
  print('s.empty() == %s, s.size() == %s' % (s.empty(), s.size()))
  s.add(19)
  s.add(86)
  print('s.empty() == %s, s.size() == %s' % (s.empty(), s.size()))
  print('86 is%s in s' % ('' if s.search(86) else ' not',))
  print('4 is%s in s' % ('' if s.search(4) else ' not',))
  print('s.empty() == %s, s.size() == %s' % (s.empty(), s.size()))
  s.remove(19)
  print('s.empty() == %s, s.size() == %s' % (s.empty(), s.size()))
            
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    