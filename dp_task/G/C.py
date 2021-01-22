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
	N, M = readLine()
	d = collections.defaultdict(list)
	ind = [0] * N
	for _ in range(M):
		x, y = readLine()
		x, y = x-1, y-1
		ind[y] += 1
		d[x].append(y)

	dp = [0] * N
	q = collections.deque()
	for i in range(N):
		if ind[i] == 0:
			q.append(i)
	while q:
		cur = q.popleft()
		for nei in d[cur]:
			dp[nei] = max(dp[nei], dp[cur] + 1)
			if ind[nei]:
				ind[nei] -= 1
				if not ind[nei]:
					q.append(nei)
	print(max(dp))


# tcase()
solve()