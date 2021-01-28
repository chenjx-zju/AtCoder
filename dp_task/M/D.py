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

mod = 10 ** 9 + 7

def solve():
	N, K = readLine()
	arr = readLine()
	pre = [0]
	for a in arr:
		pre.append(pre[-1] + a)

	dp = [[0 for _ in range(K+1)] for _ in range(N)]

	for k in range(arr[0]+1):
		dp[0][k] = 1

	temp = [0] * (K + 2)

	for i in range(1, N):
		temp[0] = 0
		for k in range(1, K+2):
			temp[k] = (temp[k-1] + dp[i-1][k-1])

		for k in range(K+1):
			if k > pre[i+1]:
				break
			dp[i][k] = temp[k+1] % mod
			if k > arr[i]:
				dp[i][k] = (dp[i][k] - temp[k-arr[i]]) % mod

	print(dp[N-1][K] % mod)

	


# tcase()
solve()