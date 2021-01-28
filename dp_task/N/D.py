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
	N = readInt()
	arr = readLine()

	pre = [0]
	for a in arr:
		pre.append(pre[-1] + a)

	dp = [[0 for _ in range(N)] for _ in range(N)]

	for l in range(1, N):
		for i in range(0, N):
			if i + l >= N:
				break
			j = i + l
			cost = pre[j+1] - pre[i]
			merge = float('inf')
			for k in range(i, j):
				merge = min(merge, dp[i][k] + dp[k+1][j])
			dp[i][j] = cost + merge

	print(dp[0][N-1])
	


# tcase()
solve()