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
	arr = []
	for _ in range(N):
		arr.append(readLine())
	
	mod = 10 ** 9 + 7

	dp = [0 for _ in range(1 << N)]
	
	dp[0] = 1

	for i in range(1 << N):
		count = 0
		for j in range(N):
			if i & (1 << j):
				count += 1
		for j in range(N):
			if not arr[count - 1][j]:
				continue
			if not (i & (1 << j)):
				continue
			dp[i] = (dp[i] + dp[i ^ (1 << j)]) % mod
	print(dp[-1])

# tcase()
solve()