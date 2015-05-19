import sys
from string import ascii_lowercase as al
sentence  = raw_input()
sentence = sentence.replace(" ", "").lower()

my_dict_rev= {}
for i,j in enumerate(al):
	my_dict_rev[j] = i

alpha = []

for char in sentence:
	if char in alpha:
		pass
	else:
		alpha.append(char)

score = 0
for item in alpha:
	score+=my_dict_rev[item]

if score == 325:
	print 'pangram'
else:
	print 'not pangram'
print alpha, score