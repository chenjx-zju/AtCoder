# Educational DP Contest

> https://atcoder.jp/contests/dp

## A - Frog 1

## B - Frog 2

## C - Vacation

## D - Knapsack 1

1 ≤ W ≤ 10^5

01背包

## E - Knapsack 2

观察到总value不大，对value 01背包

## F - LCS

倒序统计dp，顺序遍历输出子序列

[7, 6, 6, 5, 5, 4, 4, 4, 3, 2, 2, 1, 0]
[6, 6, 6, 5, 5, 4, 4, 4, 3, 2, 2, 1, 0]
[6, 6, 6, 5, 5, 4, 4, 4, 3, 2, 2, 1, 0]
[6, 6, 6, 5, 5, 4, 4, 4, 3, 2, 2, 1, 0]
[5, 5, 5, 5, 5, 4, 4, 4, 3, 2, 2, 1, 0]
[5, 5, 5, 5, 5, 4, 4, 4, 3, 2, 2, 1, 0]
[4, 4, 4, 4, 4, 4, 4, 4, 3, 2, 2, 1, 0]
[3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 1, 0]
[2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 0]
[2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 0]
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0]
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

## G - Longest Path

拓扑排序，更新dp

## H - Grid 1

## I - Coins

二维dp，注意迭代顺序。

## J - Sushi

考虑到堆数量相同堆等价，统计数量为1 2 3的堆的数量记录状态。

三维dp，递归TLE。注意根据状态转移公式决定迭代的顺序。

## K - Stones

一维dp，dp[k]代表剩余k个，先手胜。如果有一个dp[k-a]为False，dp[k]为True。

## L - Deque

二维dp，第一维按照区间长度遍历。

## M - Candies

dp(n, k)  = dp(n-1, k) + dp(n-1, k) + ... + dp(n-1, k-arr[n])，等式右边可以有前缀和省时间，时间复杂度O(NK)

## N - Slimes

二维dp，dp(i, j) = min(dp(i, k) + dp(k+1, j)) for k in range(i, j)

## O - Matching

状态压缩dp，状态中1的个数可以表明第几行，顺序遍历状态。dp[i] = (dp[i] + dp[i ^ (1 << j)]) % mod

## P - Independent Set

dfs遍历树，倒序bottom up dp染色

## Q - Flowers

dp[h] = max(dp[0...h-1]) + val[h]。线段树维护即可（不会写抄的BIT模板）

## R - Walk

倍增法生成路径长度为1 << n的矩阵，位运算把各矩阵相乘。（单位矩阵是主对角线为1的矩阵

## S - Digit Sum

数位dp，dp(index, smaller, modD)，根据smaller遍历index位的num，状态转移

## T - Permutation

考虑定义dp(i, j)是使用0 ~ i的排列满足了前 i - 1 个符号的要求，且最后一个为j的方案数。

然后以 j - 1 为分界线，把 j - 1之后的数都加一，不破坏整体关系的前提下消除了 j，再把 j 放到最后一位。

dp(i+1, j) = dp(i, j...i) or dp(i, 0...j-1)。前缀和维护结果。

## U - Grouping

首先计算子集对应的分数，状压dp，遍历子集 dp[state] = max(dp[state], memo[sub] + dp[state ^ sub])

## V - Subtree

## W - Intervals

## X - Tower

考虑相邻 i j 砖块交换位置推导出 s + w 越小应该在越高的位置。排序后 01 背包

## Y - Grid 2

## Z - Frog 3