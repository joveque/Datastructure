# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 16:08:15 2018

@author: joveque
"""

class Node:
    def __init__(self,item):
        self._item = item
        self._next = None   #尾指针
        self._pre = None    #头指针
        
    def getitem(self):
        return self._item
    
    def getnext(self):
        return self._next
    
    def getpre(self):
        return self._pre
    
    def setitem(self, newitem):
        self._item = newitem
        
    def setnext(self, newnext):
        self._next = newnext
        
    def setpre(self, newpre):
        self._pre = newpre
        
class twowaylist(Node):
    def __init__(self, head, tail):
        self._head = Node(head)   
        self._tail = Node(tail)
        self._head.setnext(self._tail)
        self._tail.setpre(self._head)
        
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
        length = 0
        if not self.empty():
            while current != None:
                length += 1
                current = current.getnext()
        return length
    
    #追加节点
    def append(self, item):
        node = Node(item)
        current = self._head
        while current.getnext().getnext() != None:
            current = current.getnext() #遍历链表
        current.setnext(node)   #此时current为链表倒数第二的元素
        node.setpre(current)
        node.setnext(self._tail)
        self._tail.setpre(node)
        
    
    #获取节点
    def get(self, index):
        #获取第index个值，若index>0正向获取else 反向获取
        length = self.size()
        index = index if index >= 0 else length +index  #注意
        if index >= length or index < 0:
            print("%s is beyond" %index)
        node = self._head
        while index:
            node = node.getnext()
            index -= 1
        print(node.getitem())
        return node
    
    #设置节点
    def set(self, index, data):
        node = self.get(index)
        if node:
            node.data = data
        return node
    
    #插入节点
    def insert(self, index, data):  #有问题
        length = self.size()
        if abs(index + 1) > length:
            return False
        index = index if index >= 0 else index + 1 + length
        
        node = self.get(index)
        if node:
            add_node = Node(data)
            node.getnext().setpre(add_node)
            add_node.setnext(node)
            node.setnext(add_node)
            add_node.setpre(node)
            return add_node
        
    #删除节点
    def delete(self, index):
        node = self.get(index)
        if node:
            node.getpre().setnext(node.getnext())
            node.getnext().setpre(node.getpre())
            return True
        return False
    
    #反转链表
    def __reversed__(self):
        pre_head = self._head
        tail = self._tail
        
        def reverse(pre_node, node):
            if node:
                node.getnext().setnext(node)
                node.setnext(pre_node)
                pre_node.setpre(node)
                if pre_node is self._head:
                    pre_node.setnext(None)
                if node is self._tail:
                    node.setpre(None)
                return reverse(node, node.getnext())
            else:
                self._head = tail
                self._tail = pre_head
        return reverse(self._head, self._head.getnext())
    
    #清空链表
    def clear(self):
        self._head.setnext(self._tail)
        self._tail.setnext(self._head)
        
    #遍历链表
    def travel(self):
        current = self._head
        if not self.empty():
            while current != None:
                print (current.getitem())
                current = current.getnext()
        
if __name__=='__main__':
    a=twowaylist(1,100) 
    a.append(2)
    a.append(3)
    a.append(4)
    a.get(3)
    a.insert(1, 2)
    a.travel()
         
                
                
    
    
            
        
    
            
            
            
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        