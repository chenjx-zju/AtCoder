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
	arr = [readLine() for _ in range(n)]
	arr.sort(key=lambda x: (x[0] + x[1], x[0]))

	dp = [[0 for _ in range(20050)] for _ in range(n+1)]

	for i in range(1, n+1):
		cw, cs, cv = arr[i-1]
		for w in range(20050):
			dp[i][w] = dp[i-1][w]
			if w >= cw and w <= cs + cw:
				dp[i][w] = max(dp[i][w], dp[i-1][w - cw] + cv)

	print(max(dp[-1]))

	


# tcase()
solve()