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

	dp = [[0 for _ in range(N)] for _ in range(N)]

	for i in range(N):
		dp[i][i] = arr[i]

	for l in range(1, N):
		for i in range(N):
			if i + l >= N:
				break
			dp[i][i+l] = max(-dp[i+1][i+l] + arr[i], -dp[i][i+l-1] + arr[i+l])
	print(dp[0][N-1])
	


# tcase()
solve()