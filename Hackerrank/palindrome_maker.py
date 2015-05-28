t=int(raw_input())

words = []
while t:
	words.append(raw_input())
	t=t-1

def check_palindrome(string):
	if string == string[::-1]:
		return 1
	else:
		return 0

for word in words:
	string = list(word)
	if check_palindrome(string):
		print '-1'
		continue
	else:
		for i,j in enumerate(range(len(string),0,-1)):
			j=j-1
			if string[i] == string[j]:
				continue
			else:
				index_1, index_2 = string.index(string[i]),string.index(string[j])
				string.pop(index_1)
				if check_palindrome(string):
					print index_1
					break
				else:
					string.insert(index_1,string[i])
					string.pop(index_2)
					if check_palindrome(string):
						print index_2
						break