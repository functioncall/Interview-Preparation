import sys
import re

# print ("Script name: %s" % str(sys.argv[1]))
# Get the number of testcases from the command line input

#testc = str(sys.argv[1])
testc = 2

#RPN expression
# rpn = '(a+(b*c))'
rpn = '(a+c)'
# Loop through the testcases
#for i in range(testc):

operator_list = []
output_list = []
for char in rpn:

    if char == '(':
    	# Append the ( symbol into the operator stack
        operator_list.append(char)

    elif char == ')':
		
		# scan and pop elements from the operator stack until left pair ')' is found
		for op in operator_list:
			print op
			if top == '(':
				break
			else:
				print "hello"
				operator_list.remove(op)
				output_list.append(op)


    elif char == '+':
    	top = operator_list[len(operator_list)-1]
    	# check the operator stack 
    	if top == '(' or top == ')':
    		operator_list.append(char)

    	elif top == '*' or top == '/' or top == '+' or top == '-':
    		# Scan the operator stack and pop until an element of lower priority is found
    		scan_stack(top,char)



			




    # elif char == '-':
    # 	# do something
    # elif char == '*':
    # 	# do something
    # elif char == '^':
    # 	# do something
        
    elif bool(re.search('[a-z]', char, re.IGNORECASE)):
    	# print char
        output_list.append(char)


# print operator_list
print output_list
print operator_list

def scan_stack(t, c):
	# Base condition here
	if top == '(' or top == ')' or top == '':
		return 
	# pop the top char 
	operator_list.remove(t)
	# append the char into the operator stack
	operator_list.append(c)
	# and put the top char into output stack
	output_list.append(t)
	top = operator_list[len(operator_list)-1]
	scan_stack(top,c)
