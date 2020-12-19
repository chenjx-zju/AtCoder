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
	N, W = readLine()
	w, v = [], []
	for _ in range(N):
		a, b = readLine()
		w.append(a)
		v.append(b)

	dp = [[0 for _ in range(W+1)] for _ in range(N)]

	for j in range(W+1):
		if j >= w[0]:
			dp[0][j] = v[0]

	for i in range(1,N):
		for j in range(W+1):
			dp[i][j] = dp[i-1][j]
			if j - w[i] >= 0:
				dp[i][j] = max(dp[i][j], dp[i-1][j-w[i]] + v[i])

	# print(dp)
	print(max(dp[-1]))


# tcase()
solve()