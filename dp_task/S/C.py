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
	k = readString()
	d = readInt()

	nums = list(map(int, list(k)))
	n = len(nums)
	mod = 10 ** 9 + 7

	dp = [[[0 for _ in range(d)] for _ in range(2)] for _ in range(n+1)]

	dp[0][0][0] = 1

	for i in range(n):
		for sm in range(2):
			for md in range(d):
				up = 9 if sm else nums[i]
				for num in range(up+1):
					nsm = sm or num < up
					if sm == 1 and nsm == 0:
						continue
					cur = dp[i+1][nsm][(md + num) % d]
					cur += dp[i][sm][md]
					if cur > mod:
						cur -= mod
					dp[i+1][nsm][(md + num) % d] = cur

	print((dp[n][0][0] + dp[n][1][0] + mod - 1) % mod)


# tcase()
solve()