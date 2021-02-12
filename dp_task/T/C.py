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
	s = readString()
	mod = 10 ** 9 + 7

	dp = [[0 for _ in range(n+1)] for _ in range(n+1)]

	dp[1][1] = 1

	def get(pre, i, j):
		return (pre[j+1] - pre[i]) % mod

	for i in range(2, n+1):
		pre = [0]
		for j in range(n+1):
			pre.append((pre[-1] + dp[i-1][j]) % mod)

		if s[i-2] == '<':
			for j in range(2, i+1):
				dp[i][j] = get(pre, 0, j-1)
		else:
			for j in range(i-1, 0,-1):
				dp[i][j] = get(pre, j, i)
	
	ans = 0
	for j in range(n+1):
		ans = (ans + dp[-1][j]) % mod

	print(ans)
	


# tcase()
solve()