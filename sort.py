t=int(raw_input())
out = []
def sort(l,m):
	out = []
	for item in l:
		out.append(item)
	for item in m:
		out.append(item)
	return sorted(out)[::-1]

while t:
	n,m = raw_input().split()
	ar1 = [int(i) for i in raw_input().strip().split()]
	ar2 = [int(i) for i in raw_input().strip().split()]
	print n,m
	out.append(sort(ar1, ar2))
	t=t-1

for item in out:
	print " ".join(map(str,item))


