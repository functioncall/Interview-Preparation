import sys

def reverse(x,y):
	a[x:y+1] = reversed(a[x:y+1])

i = int(raw_input())
n = int(raw_input())
a = raw_input().split()

reverse(0,i-1)
reverse(i,n-1)
reverse(0,n-1)
print ' '.join(a)