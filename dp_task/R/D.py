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

mod = 10 ** 9 + 7

def matmul(a, b, n):
	new = [[0 for _ in range(n)] for _ in range(n)]
	for i in range(n):
		for j in range(n):
			temp = 0
			for k in range(n):
				temp = (temp + a[i][k] * b[k][j]) % mod
			new[i][j] = temp
	return new

def solve():
	n, k = readLine()
	arr = [readLine() for _ in range(n)]

	digit = int(math.log2(k))

	check = [[] for _ in range(digit+1)]
	check[0] = arr

	for i in range(1, digit+1):
		ref = check[i-1]
		new = matmul(ref, ref, n)
		check[i] = new
	# print(check)

	base = [[0 for _ in range(n)] for _ in range(n)]
	for i in range(n):
		base[i][i] = 1

	for i in range(digit + 1):
		if k & (1 << i):
			base = matmul(check[i], base, n)

	ans = 0
	for i in range(n):
		for j in range(n):
			ans = (ans + base[i][j]) % mod
	print(ans)

	


# tcase()
solve()