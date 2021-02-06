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
	
	eds = []
	for _ in range(n-1):
		eds.append(readLine())

	mod = 10 ** 9 + 7

	nei = collections.defaultdict(list)
	for e in eds:
		x, y = e[0] - 1, e[1] - 1
		nei[x].append(y)
		nei[y].append(x)
	
	q = collections.deque([0])
	seen = set({0})
	
	df = []
	while q:
		cur = q.popleft()
		df.append(cur)
		for x in nei[cur]:
			if x not in seen:
				q.append(x)
				seen.add(x)

	index = [0] * n
	for i in range(n):
		index[df[i]] = i

	dp = [[1 for _ in range(2)] for _ in range(n)]
	# 0 black, 1 white

	for i in range(n-1,-1,-1):
		cur = df[i]
		for x in nei[cur]:
			if index[x] > index[cur]:
				dp[cur][0] = (dp[cur][0] * dp[x][1]) % mod
				dp[cur][1] = (dp[cur][1] * (dp[x][0] + dp[x][1])) % mod

	print((dp[0][0] + dp[0][1]) % mod)

	


# tcase()
solve()