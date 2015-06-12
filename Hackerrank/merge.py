def check_merge(j):
	if merge_check_dict[j] == 0:
		merge_check_dict[j] = 1
		for item in xrange(j+1):
			merge_check_dict[item] = 1
		return 1
	else:
		return 0
def merge(line):
	result = [0]*len(line)
	for i in xrange(len(line)):
		merge_check_dict[i] = 0

	for i,item in enumerate(line):
		if item != 0:
			# print 'item',item, i
			if i == 0:
				result[i] = item
				# print result
			else:
				set_flag = 0
				for j in xrange(i,0,-1):
					# print i,j-1
					if result[j-1] == 0:
						# print 'case 1'
						result[j-1] = item
						result[j] = 0
						set_flag=1
						# print result
					elif result[j-1] == item and check_merge(j-1):
						# print 'Before merging',result
						# print 'case 2-merging',i,j-1
						result[j-1] = item + item
						result[j] = 0
						# print 'After merging',result
						break
					elif result[j-1] != item and set_flag == 1:
						# print 'case 3'
						# print result
						break
					elif result[j-1] != item and set_flag == 0:
						# print 'case 4'
						result[i] = item
						# print result
						break
			# merge_check_dict[i] = 1
	return result

# lst1 = map(int,raw_input().split())
lst1 = [8,8]
merge_check_dict = {}
lst2 = merge(lst1)
# print lst1            # You should get [2, 0, 2, 4]
print lst2            # You should get [4, 4, 0, 0]