# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 17:14:30 2018

@author: joveque
"""

#用list实现队列
class Queue():
    def __init__(self):
        self.items = []
    def enqueue(self, item):
        self.items.append(item)
    def dequeue(self):
        if  len(self.items) == 0:
            print("queue is empty")
        else:
            return self.items.pop(0)
    def empty(self):
        return self.size() == 0
    def size(self):
        return len(self.items)
    
'''
实现约瑟夫斯问题
约瑟夫斯问题（Josephus Problem）是应用队列（确切地说，是循环队列）的典型案例。
在约瑟夫斯问题中，参与者围成一个圆圈，从某个人（队首）开始报数，
报数到n+1的人退出圆圈，然后从退出人的下一位重新开始报数；
重复以上动作，直到只剩下一个人为止。
'''
def josephus(namelist, num):
    simqueue = Queue()
    for name in namelist:
        simqueue.enqueue(name)
    while simqueue.size() > 1:
        for i in range(num):
            simqueue.enqueue(simqueue.dequeue())
        simqueue.dequeue()
    #print(simqueue.dequeue())
    return simqueue.dequeue()
if __name__ == '__main__':
    print(josephus(["Bill", "David", "Kent", "Jane", "Susan", "Brad"], 3))
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        