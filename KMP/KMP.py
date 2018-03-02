# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 21:24:18 2018

@author: joveque
"""
#主函数
def matching_KMP(t, p, pnext):
    j, i = 0, 0
    n, m = len(t), len(p)
    while j < n and i < m:      #i=m说明找到了匹配
        if i == -1 or t[j] == p[i]:  #考虑p中下一字符
            j, i = j+1, i+1         
        else:                   #失败，考虑pnext决定的下一字符
            i = pnext[i]
    if i == m:                  #找到匹配
        return j-i
    return -1                   #无匹配，返回特殊值

#pnext表构造算法
def gen_pnext(p):
    """生成针对p中各位置i的下一检查位置表，用于KMP算法"""
    i, k, m = 0, -1, len(p)
    pnext = [-1] * m        #初始数组元素全为-1
    while i < m - 1:        #生成下一个pnext元素值
        if k == -1 or p[i] == p[k]:     #循环中一个一个比较是否相同，相同则k不断加1
            i, k = i+1, k+1
            pnext[i] = k    #设置pnext元素
        else:
            k = pnext[k]    #找不到相同时，将k值变为pnext表中未遍历的值，即-1，使其下一轮p[i]和前面的比较
    print(pnext)
    return pnext

#改进版pnext,改进后可以使模式串右移更远，因为出现第一个相同最长前后缀的元素对应pnext值为-1，而下标不能为-1
def gen_pnext1(p):
    """生成针对p中各位置i的下一检查位置表，用于KMP算法"""
    i, k, m = 0, -1, len(p)
    pnext = [-1] * m        #初始数组元素全为-1
    while i < m - 1:        #生成下一个pnext元素值
        if k == -1 or p[i] == p[k]:
            i, k = i+1, k+1
            if p[i] == p[k]:
                pnext[i] = pnext[k]
            else:
                pnext[i] = k    #设置pnext元素
        else:
            k = pnext[k]    #找不到相同时，将k值变为pnext表中未遍历的值，即-1，使其下一轮p[i]和前面的比较
    print(pnext)
    return pnext

gen_pnext("abbcabcaabbcaa")
gen_pnext1("abbcabcaabbcaa")




























            
        
    