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

def stringmax(a, b):
	return a if len(a) > len(b) else b

def solve():
	s = readString()
	t = readString()
	ls, lt = len(s), len(t)
	dp = [[0 for _ in range(lt+1)] for _ in range(ls+1)]

	for i in range(ls-1, -1, -1):
		for j in range(lt-1, -1, -1):
			dp[i][j] = max(dp[i+1][j], dp[i][j+1])
			if s[i] == t[j]:
				dp[i][j] = max(dp[i][j], dp[i+1][j+1] + 1)
	
	# for row in dp:
	# 	print(row)

	i, j = 0, 0
	while i < ls and j < lt:
		if s[i] == t[j]:
			print(s[i], end='')
			i, j = i+1, j+1
		elif dp[i][j] == dp[i+1][j]:
			i += 1
		else:
			j += 1
	print()


# tcase()
solve()