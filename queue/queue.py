# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 17:05:08 2018

@author: joveque
"""

#定义一个队列
queue = []

#进队列,调用列表的append()函数加到列表的末尾,strip()没有参数是去掉首尾的空格
def appendit():
    queue.append(input('Enter new string:').strip())
    
    
#调用list的列表的pop()函数.pop(0)为列表的第一个元素 
def popit():
    if len(queue) == 0:
        print('shed is empty!')
    else:
        print('remove[',queue.pop(0),']')
        

#编历队列
def viewit():
    print(queue)
    
    
#CMD是字典的使用 
CMD = {'a': appendit, 'p': popit, 'v': viewit} 


#p为提示字符 
def showit(): 
    pr = """ 
    (a)ppend 
    (p)op 
    (v)iew 
    (q)uit
        Enter choice: """
    
    while True:
        while True:
            try:
                #先用strip()去掉空格,再把第一个字符转换成小写的 
                choice = input(pr).strip()[0].lower() 
            except (EOFError, KeyboardInterrupt, IndexError): 
                choice = 'q'
            print('\nYou picked:[%s]' %choice)
            if choice not in 'apvq':
                print('Invalid option, try again')
            else:
                break
            
        #CMD[]根据输入的choice从字典中对应相应的value,比如说输入a,从字典中得到value为appendit,执行appendit()进栈操作 
        if choice == 'q': 
          break
        CMD[choice]() 
            

#判断是否是从本文件进入,而不是被调用 
if __name__ == '__main__': 
    showit() 