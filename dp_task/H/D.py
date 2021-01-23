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
	H, W = readLine()
	grid = []
	for _ in range(H):
		grid.append(readString())
	dp = [[0 for _ in range(W+1)] for _ in range(H+1)]
	mod = 10 ** 9 + 7

	dp[1][1] = 1

	for i in range(H):
		for j in range(W):
			if i == 0 and j == 0:
				dp[1][1] = 1
			elif grid[i][j] == '.':
				dp[i+1][j+1] = dp[i+1][j] + dp[i][j+1]
				if dp[i+1][j+1] >= mod:
					dp[i+1][j+1] -= mod
	print(dp[-1][-1])


# tcase()
solve()