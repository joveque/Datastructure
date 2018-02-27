# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 21:26:06 2018

@author: joveque
"""

class Node:
    def __init__(self,item):
        self._item = item
        self._next = None   #Node的指针部分默认指向Node
        
    def getitem(self):
        return self._item
    
    def getnext(self):
        return self._next
    
    def setitem(self, newitem):
        self._item = newitem
        
    def setnext(self, newnext):
        self._next = newnext
        
#singlelinkedlist的实现
class Singlelist:
    def __init__(self):
        self._head = None   #初始化链表为空表
        self._size = 0
    
    #检测链表是否为空
    def empty(self):
        if self._head == None:
            print("list is empty!")
            return True
        else:
            return False
    
    #检查链表的长度
    def size(self):
        current = self._head
        count = 0
        if not self.empty():
            while current != None:
                count += 1
                current = current.getnext()
        return count
    
    #遍历链表
    def travel(self):
        current = self._head
        if not self.empty():
            while current != None:
                print (current.getitem())
                current = current.getnext()
    
    #在链表前端添加元素
    def add(self, item):
        temp = Node(item)
        temp.setnext(self._head)
        self._head = temp
        
    #在链表尾部添加元素
    def append(self, item):
        temp = Node(item)
        if self.empty():
            self._head = temp   #若为空表，将添加的元素设为第一个元素
        else:
            current = self._head
            while current.getnext() != None:
                current = current.getnext() #遍历链表
            current.setnext(temp)   #此时current为链表最后的元素
    
    #检查元素是否在链表中
    def search(self, item):
        current = self._head
        founditem = False
        if not self.empty():
            while current !=None and not founditem:
                if current.getitem() == item:
                    founditem = True
                else:
                    current = current.getnext()
            if not founditem:
                print("Not found %s" %item)
        return founditem
    
    #索引元素在链表中的位置
    def index(self, item):
        current = self._head
        count = 0
        found = None
        if not self.empty():
            while current != None and not found:
                count += 1
                if current.getitem() == item:
                    found = True
                else:
                    current = current.getnext()
            if found:
                return count
            else:
                raise ValueError + '%s is not in linkedlist' %item
            
    #删除链表中的某项元素
    def remove(self, item): 
         current = self._head
         pre = None
         if not self.empty():
             if self.search(item):
                 while current != None:
                     if current.getitem() == item:
                         if not pre:    #当只有一个元素时
                             self._head = current.getnext()
                         else:
                             pre.setnext(current.getnext()) #令current的前一个元素的指针指向current.next，相当于删除了current
                         break
                     else:
                         pre = current
                         current = current.getnext()
                 
    #链表中插入元素
    def insert(self, pos, item):
         #首端插入
         if pos <= 1:
             self.add(item)
         #尾端插入
         elif pos >self.size():
             self.append(item)
         else:
             temp = Node(item)  #因为原链表中没有item这个元素
             count = 1
             pre = None
             current = self._head
             while count < pos:
                 count += 1
                 pre = current
                 current = current.getnext()
             pre.setnext(temp)
             temp.setnext(current)


if __name__=='__main__':
  a=Singlelist()
  a.add(1)
  a.add(3)
  a.add(4)
  a.travel()
  a.remove(4)
  a.travel()
  #for i in range(1,10):
    #a.append(i)
  
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        