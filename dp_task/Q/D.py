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

class BIT:
    def __init__(self, n):
        self.n = n + 1
        self.ms = [0] * self.n
    def update(self, i, val):
        while i < self.n:
            self.ms[i] = max(self.ms[i], val)
            i += i & (-i)
    def get(self, i):
        res = 0
        while i > 0:
            res = max(res, self.ms[i])
            i -= i & (-i)
        return res

def solve():
	n = readInt()
	h = readLine()
	a = readLine()

	bit = BIT(n)

	for i in range(n):
		res = bit.get(h[i]-1) + a[i]
		bit.update(h[i], res)

	print(bit.get(n))
	


# tcase()
solve()