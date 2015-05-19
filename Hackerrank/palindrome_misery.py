import sys
# sys.setrecursionlimit(5000)
words = []
t=int(raw_input())
while t:
	words.append(raw_input())
	t=t-1
def do_something(word, n, i, j,op):
	# Base case
	if n==0:
		print op
		return
	if ord(word[j]) > ord(word[i]):
		op = abs(op + (ord(word[j]) - ord(word[i])))
		do_something(word, n-1,i+1,j-1,op)
	elif ord(word[i]) > ord(word[j]):
		op = abs(op + (ord(word[i]) - ord(word[j])))
		do_something(word, n-1,i+1,j-1,op)
	else:
		do_something(word, n-1,i+1,j-1,op)

for word in words:
	word=list(word)
	n,i,j,op=len(word)/2,0,len(word)-1,0
	do_something(word,n,i,j,op)