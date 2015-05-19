import sys
from string import ascii_lowercase as al

myDict = {}
anagramDict = {}

def enumdict(alpha):
	for i, x in enumerate(alpha):
		myDict[x] = i
	return myDict

def sort_insertion(my_list):
    for i in range(1,len(my_list)):
        val_current = my_list[i]
        pos = i 
        
        # check backwards through sorted list for proper pos of val_current
        while((pos > 0) and (my_list[pos-1] > val_current)):
            my_list[pos] = my_list[pos-1]
            pos = pos-1
             
        if pos != i:
            my_list[pos] = val_current 
    
    return my_list

def create_Signature(word):
	word_num_list = []
	for char in word:
		if char in al:
			word_num_list.append(myDict[char])
		else:
			pass # skip for special characters

	# Sort this new list
	sort_insertion(word_num_list)
	# print word_num_list

	# Creating the signature from the sorted list
	word_sig = []
	for char, value in myDict.items():
		for num in word_num_list:
			if value == num:
				word_sig.append(char)
	# print ''.join(word_sig)
	n_word = ''.join(word_sig)

	if bool(anagramDict):
		for key in anagramDict.items():
			# print key
			if key == n_word:
				# Append the anagram to the same signature
				anagramDict[key].append(word)
				break
			else:
				n_word_list = []
				# Create a new entry
				anagramDict.setdefault(n_word, []).append(word)
				break
	else:
		# First entry
		# anagramDict.setdefault(n_word, {})[word] = 1
		anagramDict.setdefault(n_word, []).append(word)

def main():
	enumdict(list(al))
	# words = open('/usr/share/dict/american-english','r')
	words = open('/home/zerobyte/Desktop/Files/words.txt','r')
	for word in words:
		word = word.replace("'", "").lower()
		create_Signature(word)
		print 'Signature created :',word

	print anagramDict



main()
