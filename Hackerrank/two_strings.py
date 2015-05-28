t=int(raw_input())
temp = t
first_line_string,second_line_string = [],[]

while t:
	first_line_string.append(raw_input())
	second_line_string.append(raw_input())
	t=t-1

for i in range(temp):
	set_flag = 0
	for char in first_line_string[i]:
		if char in second_line_string[i]:
			print 'YES'
			set_flag = 1
			break
	if set_flag == 0:
		print 'NO'