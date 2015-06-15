"""
This is a docstring for the module:

This module demonstrates the merge functionality
in the 2048 game.
"""
def check_merge(iterator):
    """
    Check whether the merge has happen at a particular
    index or not, and returns the appropriate boolean value
    for the same.
    """
    if Dictionary[iterator] == 0:
        Dictionary[iterator] = 1
        for item in xrange(iterator+1):
            Dictionary[item] = 1
        return 1
    else:
        return 0
def merge(line):
    """
    Return a new merge list for the given input list.
    """
    # Start with a result list that contains the same number of 0's as the length of the line argument. 
    result = [0]*len(line)
    # Initialize the dictionary with default value 0
    for index in xrange(len(line)):
        Dictionary[index] = 0
    
    # Iterate over every value in the list
    for index,item in enumerate(line):
    	# Iterate over the line input looking for non-zero entries
        if item != 0:
        	# Put the first index element directly in the result list
            if index == 0:
                result[index] = item
                # For the rest of the elements, iterate towards the front of the list and start merging
            else:
                set_flag = 0
                for iterator in xrange(index,0,-1):
               	    # For 0 elements
                    if result[iterator-1] == 0:
                        result[iterator-1] = item
                        result[iterator] = 0
                        set_flag=1
                    # For elements which are same and merge can be applied
                    elif result[iterator-1] == item and check_merge(iterator-1):
                        result[iterator-1] = item + item
                        result[iterator] = 0
                        break
                    elif result[iterator-1] != item and set_flag == 1:
                        break
                    elif result[iterator-1] != item and set_flag == 0:
                        result[index] = item
                        break

    return result

list_1 = map(int,raw_input().split())
# list_1 = [8,8]
# Initialize an empty dictionary
Dictionary = {}
# Printing the result
print merge(list_1)