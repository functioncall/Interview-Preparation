# Enter your code here. Read input from STDIN. Print output to STDOUT
from string import ascii_lowercase as al

t=int(raw_input())
# Create dict here
mydict_vk,mydict_kv = {i:j for i,j in enumerate(al)},{j:i for i,j in enumerate(al)}

words = []
while t:
    words.append(raw_input())
    t=t-1

for word in words:
    #print word
    if word == word[::-1]:
        print 'no answer'
        continue
    # Append the char values into a new list
    num_word = []
    for char in word:
        if char in mydict_kv.keys():
            num_word.append(mydict_kv[char])
    num_map = {}
    num_map_rev = {}
    i=1
    # Create a mapping
    for item in sorted(num_word):
        num_map[item] = i
        num_map_rev[i] = item
        i=i+1
    #print num_map_rev.items()
    # Create the new number representation of the word
    new_num_word = []
    for char in word:
        new_num_word.append(num_map[mydict_kv[char]])
    #print new_num_word

    # Generating lexicographically higher order terms
    for i in range(len(new_num_word),0,-1):
        if (i-1)==0:
            #print 'Breaking here'
            break
        i=i-1
        j=i-1
        if j == 0:
            temp = new_num_word[j]
            for n,i in enumerate(new_num_word):
                if i == (temp+1):
                    new_num_word[n] = temp
            new_num_word[j] = new_num_word[j]+1
            new_num_word[i:len(new_num_word)] = sorted(new_num_word[i:len(new_num_word)])
            #print i,j,new_num_word,new_num_word[i], new_num_word[j],temp
            break
            
        #print i,j,new_num_word,new_num_word[i], new_num_word[j],new_num_word[j:i+1]
        if new_num_word[i] > new_num_word[j]:
            #print 'here'
            new_num_word[j:i+1] = new_num_word[j:i+1][::-1]
            break
    #print new_num_word
    
    #Convert it into characters
    num_word = []
    for item in new_num_word:
        num_word.append(mydict_vk[num_map_rev[item]])
        
    print ''.join(num_word)
    #print