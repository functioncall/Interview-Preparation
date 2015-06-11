t=int(raw_input())
def solve(l):
	out = []
	for i in xrange(len(l)):
		count,flag = 0,0
		for j in xrange(i,len(l)):
			if l[i] > l[j]:
				count+=1
				flag = 1
				out.append(count)
				break
		if flag == 0:
			out.append(count)
	return out
while t:
	n=int(raw_input())
	ar = []
	for i in xrange(n):
		ar.append(raw_input())
	print ' '.join(map(str,solve(ar)))
	t=t-1