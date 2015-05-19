import sys

def main():

	t = int(raw_input())
	while t:
		n = int(raw_input())
		val = []
		val = raw_input().split()
		# logic here
		for i in range(n):
			print val[i]
		# print val
		t = t-1
	

main()
