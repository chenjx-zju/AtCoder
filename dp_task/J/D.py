import collections
import functools

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

	a, b, c = 0, 0, 0
	for item in arr:
		a += item == 1
		b += item == 2
		c += item == 3
	dp = [[[0 for _ in range(c+1)] for _ in range(b+c+1)] for _ in range(a+b+c+1)]

	for three in range(c+1):
		for two in range(b+c+1):
			if two + three > b + c:
				continue
			for one in range(a+b+c+1):
				if one + two + three > a + b + c:
					continue
				if one + two + three == 0:
					dp[one][two][three] = 0
					continue
				temp = 1
				if one:
					temp += (one / N) * dp[one-1][two][three]
				if two:
					temp += (two / N) * dp[one+1][two-1][three]
				if three:
					temp += (three / N) * dp[one][two+1][three-1]
				
				temps = one + two + three
				if temps > 0:
					temp = N * temp / temps
				
				dp[one][two][three] = temp

	print(dp[a][b][c])

# tcase()
solve()