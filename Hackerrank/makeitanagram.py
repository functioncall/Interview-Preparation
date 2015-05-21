# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
anagram_dict1 = {}
anagram_dict2 = {}
flag = 0

def compute(string1,string2,count,flag):
	anagram = []
	for char in string1:
		if char in string2:
			anagram.append(char)
		else:
			count+=1
	# print anagram
	c = Counter(anagram)
	if flag == 0:
		for item in c:
			anagram_dict1[item] = c[item]
	else:
		for item in c:
			anagram_dict2[item] = c[item]

	return count

	


string1 = raw_input().lower()
string2 = raw_input().lower()

count = compute(string1,string2,0,0)+compute(string2,string1,0,1)

for item in anagram_dict1.keys():
	count += abs(anagram_dict1[item]-anagram_dict2[item])
print count