t = int(raw_input())
output = []
def compute(i,set_flag):
	c = 0
	for i in range(i,len(cost)):
		c = c + cost[i]
		if c == x:
			set_flag = 1
			# print 'YES'
			return set_flag
		else:
			continue
	return set_flag


while t:
	n,x = map(int,raw_input().split())
	cost = []
	for i in xrange(n):
		cost.append(int(raw_input()))
	set_flag = 0
	for i in xrange(len(cost)):
		set_flag = compute(i,set_flag)
		if set_flag == 1:
			# print 'YES'
			output.append('YES')
			break
		else:
			continue

	if set_flag == 0:
		# print 'NO'
		output.append('NO')
	t=t-1

for item in output:
	print item