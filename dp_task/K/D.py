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
	N, K = readLine()
	arr = readLine()

	dp = [False] * (K + 1)

	# dp[0] = False

	for i in range(1, K+1):
		# choice = False
		if i < arr[0]:
			dp[i] = False
		for a in arr:
			if i < a:
				continue
			if not dp[i-a]:
				dp[i] = True

	print("First" if dp[-1] else "Second")
	


# tcase()
solve()