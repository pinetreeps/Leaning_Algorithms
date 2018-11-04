# _*_ coding:utf-8 _*_
# Filename: Longest Increasing Subsequence.py
# Author: pang song
# python 3.6
# Date: 2018/10/31

# 最长递增子序列算法
"""
题目：
给定一串数组，返回其中的最长递增子序列的长度。
例如：给定数组[10, 9, 2, 5, 3, 7, 101, 18],
则其最长递增子序列为[2, 3, 7, 101],返回长度4.

解题思路：
使用动归。用Dp[i]来保存从0-i的数组的最长递增子序列的长度。
如上数组Dp[0]=1,Dp[1]=1,Dp[2]=1,Dp[3]=2,Dp[4]=2。。。
计算Dp[i]的值可以对Dp[i]之前数值进行遍历，如果nums[i]>nums[j],则Dp[i] = max(Dp[i],Dp[j]+1)。
复杂度为O(n*n)
"""


class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums==[]:
            return 0
        N = len(nums)
        Dp = [1]*N
        print(Dp)
        for i in range(N-1):
            print("i:", i)
            for j in range(0,i+1):
                print("j:", j)
                if nums[i+1]>nums[j]:
                    Dp[i+1] = max(Dp[i+1],Dp[j]+1)
                    print(Dp)
        return max(Dp)

if __name__ == '__main__':
    a = [10, 9, 2, 5, 3, 7, 101, 18]

    ss = Solution()
    print(ss.lengthOfLIS(a))
