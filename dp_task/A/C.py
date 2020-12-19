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

	h = readLine()

	dp = [float('inf')] * n

	dp[0] = 0

	for i in range(n):
		if i >= 1:
			dp[i] = min(dp[i], dp[i-1] + abs(h[i] - h[i-1]))
		if i >= 2:
			dp[i] = min(dp[i], dp[i-2] + abs(h[i] - h[i-2]))

	print(dp[-1])

# tcase()
solve()