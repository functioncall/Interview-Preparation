import sys

def main():
	strings = []
	t=int(raw_input())
	while t:
		strings.append(raw_input())
		t=t-1

	for string in strings:
		string = list(string)
		temp = string[0]
		count = 0
		for i in range(1,len(string)):
			
			if temp == string[i]:
				temp = string[i]
				count+=1
			else:
				temp = string[i]
			
		print count

main()