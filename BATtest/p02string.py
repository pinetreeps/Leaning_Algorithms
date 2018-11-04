# _*_ coding:utf-8 _*_
# Filename: p02string.py
# Author: pang song
# python 3.6
# Date: 2018/11/03
"""
# B站课程，BAT算法特训班 p02字符串 https://www.bilibili.com/video/av17664182/?p=2
"""

"""
--------------练习1 字符串循环移位----------------
给定一个字符串S[0...N-1]，要求把S的前k 个字符移动到S的尾部，如把字符串“abcdef” 前面的2个字符‘a’、‘b’移动到字符串的尾 部，得到新字符串“cdefab”:即字符串循环 左移k。
1 循环左移n+k位和k位的效果相同。
2 多说一句:循环左移k位等价于循环右移n-k位。
算法要求: 时间复杂度为 O(n)，空间复杂度为 O(1)。

--------解析--------
在暴力法无法满足实际复杂度的情况下，根据矩阵思想，分别转置再统一转置
(X’Y’)’=YX
如:abcdef
X=ab X’=ba
Y=cdef Y’=fedc
(X’Y’)’=(bafedc)’=cdefab
时间复杂度O(N)，空间复杂度O(1)
"""

# 字符串指定位置翻转算法
def reverse_string(str, start, end):
    str = list(str)
    while start < end:
        c_temp = str[start]
        str[start] = str[end]
        start += 1
        str[end] = c_temp
        end -= 1
    return "".join(str)

# 对n位字符串str，前m位左移到尾部
def left_rotate_string(str, n, m):
    # 对n对m取余数，保证 0 =< m < n
    m %= n
    str = reverse_string(str, 0, m - 1)
    str = reverse_string(str, m, n - 1)
    str = reverse_string(str, 0, n - 1)

    return str

# print(reverse_string('abcdefg',2,5))
# print(left_rotate_string('123456789',9,2))

"""
--------------练习2 LCS---------------
最长公共子序列，即Longest Common Subsequence，
LCS
 一个序列S任意删除若干个字符得到新序列T，则T
叫做S的子序列;
 两个序列X和Y的公共子序列中，长度最长的那个，
定义为X和Y的最长公共子序列。
 字符串13455与245576的最长公共子序列为455  字符串acdfg与adfc的最长公共子序列为adf
 注意区别最长公共子串(Longest Common Substring)  最长公共字串要求连续

--------解析--------
若xm=yn
对于上面的字符串X和Y: 
    x3=y3=‘C’，则:LCS(BDC,ABC)=LCS(BD,AB)+‘C’ 
    x5=y4=‘B’，则:LCS(BDCAB,ABCB)=LCS(BDCA,ABC)+‘B’

若xm!=yn，则:
 要么:LCS(Xm,Yn)=LCS(Xm-1, Yn) 
 要么:LCS(Xm,Yn)=LCS(Xm, Yn-1)

得到状态转移方程

"""



"""
--------------练习3 LIS---------------
最长公共递增子序列，即Longest Increasing Subsequence
"""





"""
--------------练习4 字符串全排列---------------
给定字符串S[0...N-1]，设计算法，枚举S的 全排列。
以字符串1234为例:
 1 – 234
 2 – 134
 3 – 214
 4 – 231
 如何保证不遗漏，保证递归前1234的顺序不变

--------解析--------
除了正常的递归思路，此例还可看做是树（隐视图）的深度搜索遍历DSF，到叶子节点输出

"""

def change_letter(str, num1, num2):
    str_list = list(str)
    str_list[num1], str_list[num2] = str_list[num2], str_list[num1]
    return ''.join(str_list)

# print(change_letter('abcde', 0, 3))

def permutation(str, size, n):
    '''

    :param str: 待排列的字符串
    :param size: 字符长度
    :param n: 字符开始序号
    :return: 排列后的字符串
    '''
    if n == size - 1:
        print(str, size)
        return str

    for i in range(n, size):
        print(i)
        str = change_letter(str, i,  n)
        permutation(str, size, n+1)
        str = change_letter(str, i,  n)

permutation('123', 3, 0)
"""
--------扩展--------
时间复杂度为 O(n!)
广度优先可以看做动态规划
对于有重复字符，可在循环第一步加判断是否出现过，但时间复杂度为变为 O((n+1)!)，
可通过空间换时间的办法降低复杂度，例如增加一个和字符集合一样的数组，记录是否出现过，这样搜索数组为O(1), 整体时间复杂度降低为 O(n!)



"""
