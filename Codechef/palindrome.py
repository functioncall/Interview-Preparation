import sys
from string import ascii_lowercase as al

t=int(raw_input())

# Build the dictionary
my_dict = {}
for i,j in enumerate(al):
	my_dict[i] = j

my_dict_rev= {}
for i,j in enumerate(al):
	my_dict_rev[j] = i


def palindrome_check(string):
	if string == string[::-1]:
		return True

def char_computation(string,char,index,i):

	
	n_char = my_dict[my_dict_rev[char]-1]
	string = list(string)
	# string[len(string)-i:index+1] = n_char
	string[index] = n_char
	string = ''.join(string)
	print string
	if n_char == 'a':
		index = index-1
		i=i+1
		n_char = string[len(string)-i:index+1]

	if palindrome_check(string):
		print 'Is Panlindrome', string
		return string
	else:
		char_computation(string,n_char,index,i)
	


while t:
	string = raw_input()
	for char in string[::-1]:
		index = string.index(char)
		i=1
		char_computation(string,char,index,i)

		break

	t=t-1


"""
abcd
abcc
abcb
abca
abba

"""