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
	n, k = readLine()
	h = readLine()

	dp = [float('inf')] * n
	dp[0] = 0

	for i in range(n):
		for j in range(1, k+1):
			if i - j >= 0:
				dp[i] = min(dp[i], dp[i-j] + abs(h[i] - h[i-j]))

	print(dp[-1])


# tcase()
solve()