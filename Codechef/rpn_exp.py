import sys
import re

# print ("Script name: %s" % str(sys.argv[1]))
# Get the number of testcases from the command line input
#testc = str(sys.argv[1])
testc = raw_input()

# Get the number of rpn expressions
operator_list = []
input_exp = []

for i in range(int(testc)):
	input_exp.append(raw_input())

for rpn in input_exp:
    output_list = []
    operator_list = []
    for char in rpn:
        if char == '(':
          operator_list.append(char)
          
    # Closing braces
        elif (char == ')'):
    	    for item in operator_list[::-1]:
    		    if (item != '('):
    			    output_list.append(item)
    			    operator_list.remove(item)
    		    elif (item == '('):
    		        # Remove the opening brace
    		        operator_list.remove(item)
    		        break
    		    
        # Aphabets character 
        elif bool(re.search('[a-z]', char, re.IGNORECASE)):
            output_list.append(char)

        # Operators go here
        else:
            # print char
    	    operator_list.append(char)
    	    
    # If operator stack is not empty
    for op in operator_list[::-1]:
        output_list.append(op)
    
    print ''.join(output_list)