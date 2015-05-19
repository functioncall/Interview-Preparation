import sys

def anti_vowel(text):
	textnew = list(text)
	vovels = "aeiouAEIOU"

	for char in text:
		if char in vovels:
			textnew.pop(textnew.index(char))
	print ''.join(textnew)

anti_vowel("Hey look Words!")