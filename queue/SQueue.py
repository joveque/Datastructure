# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 17:31:38 2018

@author: joveque
"""
#定义一个可以自动扩充存储的队列类
class Queueunderflow(ValueError):
    pass

class SQueue():
    def __init__(self, init_len=8):
        self._len = init_len        #存储区长度
        self._elems = [0] * init_len    #元素存储
        self._head = 0              #表头元素下标
        self._num = 0               #元素个数
        
    def is_empty(self):
        return self._num == 0
    
    def peek(self):
        if self._num == 0:
            raise Queueunderflow
        return self._elems[self._head]
    
    def dequeue(self):
        if self._num == 0:
            raise Queueunderflow
        e = self._elems[self._head]
        self._head = (self._head+1) % self._len
        self._num -= 1
        return e
    
    def enqueue(self, e):
        if self._num == self._len:
            print("will be extend!")
            self._extend()
        self._elems[(self._head+self._num) % self._len] = e
        self._num += 1
        
    def _extend(self):
        old_len = self._len
        self._len *= 2
        new_elems = [0] * self._len
        for i in range(old_len):
            new_elems[i] = self._elems[(self._head+i) % old_len]
        self._elems, self._head = new_elems, 0
        
    def travel(self):
        if self._num == 0:
           raise Queueunderflow
        else:
            for i in self._elems:
                print(i)
        
a = SQueue()
for i in range(1,12):
    a.enqueue(i)
print(a.travel())        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        