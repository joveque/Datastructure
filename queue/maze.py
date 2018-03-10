# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 22:17:34 2018

@author: joveque
"""

class Stackunderflow(ValueError):   #栈下溢（空栈访问）
    pass

#基于顺序表技术实现的栈类
class SStack():
    def __init__(self):
        self._elems = []
        
    def is_empty(self):
        return self._elems == []
    
    def travel(self):
        if self._elems == []:
            print("list is empty!")
        for i in self._elems:
            print(i)
    
    def top(self):
        if self._elems == []:
            raise Stackunderflow("in SStack.top()")
        return self._elems[-1]
    
    def push(self, elem):
        self._elems.append(elem)
        
    def pop(self):
        if self._elems == []:
            raise Stackunderflow("in SStack.pop()")
        return self._elems.pop()

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

#方向表
dirs = [(0,1), (1,0), (0,-1), (-1,0)]

#标记函数
def mark(maze, pos):        #给迷宫maze的位置pos标2表示“到过了”
    maze[pos[0]][pos[1]] = 2

#位置检查函数
def passable(maze, pos):   #检查迷宫maze的位置pos是否可行
    return maze[pos[0]][pos[1]] == 0

#迷宫的递归求解
def find_path(maze, pos, end):
    mark(maze, pos)
    if pos == end:          #已到达出口
        print(pos, end=" ")  #输出这个位置
        return True         #成功结束
    for i in range(4):      #否则按四个方向顺序探查
        nextp = (pos[0] + dirs[i][0], pos[1] + dirs[i][1])    #dirs[i][0]表示dirs数组中第i个元组的第0个元素，当i为1时，即是元组（0，1）中的0
        #考虑下一个可能方向
        if passable(maze, nextp):             #不可行的相邻位置不管
            if find_path(maze, nextp, end):    #从nextp可达出口
                print(pos, end=" ")             #输出这个点
                return True                     #成功结束
    return False
            
#迷宫的回溯法求解
def maze_solver(maze, start, end):
    if start == end:
        print(start)
        return
    st = SStack()
    mark(maze, start)
    st.push((start, 0))             #入口和方向0的序对入栈
    while not st.is_empty():        #走不通是回退
        pos, nxt = st.pop()         #取栈顶及其探查方向
        for i in range(nxt, 4):     #依次检查未探查的新位置
            nextp = (pos[0] + dirs[i][0], pos[1] + dirs[i][1])      #算出下一位置
            if nextp == end:        #到达出口，打印路径
                print(find_path(end, pos, st))
                return
            if passable(maze, nextp):   #遇到未探查的新位置
                st.push((pos, i+1))     #原位置和下一方向入栈
                mark(maze, nextp)
                st.push((pos, 0))       #新位置入栈
                break                   #退出内层循环，下次迭代将以新栈顶为当前位置继续
    print("No path found.")              #找不到路径
                
#基于队列的迷宫求解算法
def maze_solver_queue(maze, start, end):
    if start == end:                    #特殊情况
        print("Path finds")
        return
    qu = SQueue()
    mark(maze,start)
    qu.enqueue(start)                   #start位置入队
    while not qu.is_empty():            #还有候选位置
        pos = qu.dequeue()              #取出下一个位置
        for i in range(4):             #检查每个方向
            nextp = (pos[0] + dirs[i][0], pos[1] + dirs[i][1])  #列举各位置
            if passable(maze, nextp):   #找到新的探索方向
                if nextp == end:        #是出口
                    print("Path finds")
                    return
                mark(maze, nextp)
                qu.enqueue(nextp)       #新位置入队
    print("No path.")                   #没有路径，失败！





































