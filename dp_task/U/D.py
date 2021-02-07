import collections

def readLine():
	return list(map(int, input().strip().split()))

def readInt():
	return int(input())

def readString():
	return input()

def tcase():
	t = readInt()
	for _ in range(t):
		solve()

def solve():
	n = readInt()
	arr = [readLine() for _ in range(n)]

	allstate = 1 << n
	memo = [0] * allstate
	for state in range(allstate):
		cur = []
		for j in range(n):
			if state & (1 << j):
				cur.append(j)
		score = 0
		for i in range(len(cur)):
			for j in range(i):
				score += arr[cur[i]][cur[j]]
		memo[state] = score

	dp = [-float('inf')] * allstate

	dp[0] = 0

	for state in range(1, allstate):
		res = -float('inf')
		sub = state
		while sub:
			res = max(res, memo[sub] + dp[state ^ sub])
			sub = (sub - 1) & state
		dp[state] = res

	print(dp[allstate - 1])

	


# tcase()
solve()