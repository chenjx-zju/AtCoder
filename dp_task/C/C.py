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

	happ = []
	for _ in range(n):
		happ.append(readLine())

	dp = [[0 for _ in range(3)] for _ in range(n)]
	dp[0] = happ[0]

	for i in range(1, n):
		for j in range(3):
			for k in range(3):
				if j != k:
					dp[i][j] = max(dp[i][j], dp[i-1][k] + happ[i][j])

	print(max(dp[-1]))


# tcase()
solve()