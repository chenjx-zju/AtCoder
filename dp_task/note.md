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

## N - Slimes

## O - Matching

## P - Independent Set

## Q - Flowers

## R - Walk

## S - Digit Sum

## T - Permutation

## U - Grouping

## V - Subtree

## W - Intervals

## X - Tower

## Y - Grid 2

## Z - Frog 3