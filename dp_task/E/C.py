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

def update(d, k, v):
	if k in d:
		d[k] = max(d[k], v)
	else:
		d[k] = v

def solve():
	N, W = readLine()
	w, v = [], []
	for _ in range(N):
		tw, tv = readLine()
		w.append(tw)
		v.append(tv)
	maxV = 10 ** 5

	dp = [[float('inf') for _ in range(maxV+1)] for _ in range(N+1)]

	for i in range(N+1):
		dp[i][0] = 0

	for i in range(1, N+1):
		for j in range(maxV, -1, -1):
			dp[i][j] = dp[i-1][j]
			if j >= v[i-1]:
				dp[i][j] = min(dp[i][j], dp[i-1][j-v[i-1]] + w[i-1])

	ans = 0
	for j in range(maxV+1):
		if dp[-1][j] <= W:
			ans = j
	print(ans)
	


# tcase()
solve()