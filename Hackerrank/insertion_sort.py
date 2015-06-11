#!/bin/python
"""
def insertionSort(ar):
	sort_ar = []
	for i in xrange(1,len(ar)):
		temp = ar[i]
		for j in range(i,0,-1):
			if ar[j] < ar[j-1]:
				t = ar[j]
				ar[j] = ar[j-1]
				ar[j-1] = t
		print i,repr(ar).replace(",", " ").strip('[]').replace("  "," ")
	return ""
m = input()
ar = [int(i) for i in raw_input().strip().split()]
insertionSort(ar)

"""
t=int(raw_input())

def insertion_sort(l):
	for i in xrange(1, len(l)):
		j = i-1 
		key = l[i]
		while (l[j] > key) and (j > 0):
			l[j+1] = l[j]
			j -= 1
		l[j+1] = key
	return l
out = []
while t:
	m = input()
	ar = [int(i) for i in raw_input().strip().split()]
	insertion_sort(ar)
	out.append(ar)
	t=t-1

for item in out:
	print item
	# print " ".join(map(str,item[::-1]))

# print " ".join(map(str,ar[::-1]))