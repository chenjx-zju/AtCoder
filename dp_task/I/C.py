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
	pro = list(map(float, input().strip().split()))

	dp = [[0 for _ in range(N+1)] for _ in range(N+1)]

	dp[0][0] = 1

	for toss in range(1, N+1):
		for pos in range(toss+1):
			p, n = pos, toss - pos
			if p:
				dp[p][n] += pro[toss-1] * dp[p-1][n]
			if n:
				dp[p][n] += (1 - pro[toss-1]) * dp[p][n-1]
	
	ans = 0
	for pos in range(N+1):
		p, n = pos, N - pos
		if p >= n:
			ans += dp[p][n]
	
	print(ans)


# tcase()
solve()