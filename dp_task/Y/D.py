import collections
import math

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
	h, w, n = readLine()
	wall = []
	mod = 10 ** 9 + 7
	for _ in range(n):
		r, c = readLine()
		wall.append([r, c])
	wall.append([h, w])
	n += 1

	f = [0] * (h + w + 1)
	invf = [0] * (h + w + 1)

	f[0] = f[1] = 1
	for i in range(2, h + w + 1):
		f[i] = (f[i-1] * i) % mod

	def pow_mod(x, n):
		ans = 1
		while n:
			if n & 1:
				ans = (ans * x) % mod
			n >>= 1
			x = (x * x) % mod
		return ans

	invf[0] = invf[1] = 1
	for i in range(2, h + w + 1):
		invf[i] = pow_mod(f[i], mod - 2)

	# print(f, invf)

	def comb(x, y):
		return (f[x+y] * invf[x] * invf[y]) % mod

	wall.sort(key=lambda x:(x[0]+x[1]))

	dp = [0] * n

	for i in range(n):
		x, y = wall[i]
		dp[i] = comb(x-1, y-1)
		for j in range(i):
			jx, jy = wall[j]
			if jx <= x and jy <= y:
				dp[i] = (dp[i] - dp[j] * comb(x-jx, y-jy)) % mod
	print(dp[-1])

	


# tcase()
solve()