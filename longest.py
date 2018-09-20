def find_longest(intvect):
    max_so_far = 0
    curr_count = 1
    max_pos = -1
    #iterate through all integers in the vector
    for counter1, integer in enumerate(intvect):
        #case where we just started. No comparison needed yet. 
        if counter1 == 0:
            pass
        #case where we have an increase
        elif intvect[counter1] >= intvect[counter1-1]:
            curr_count += 1
        #case where we dont have an increase
        else:
            if curr_count > max_so_far:
                max_pos = counter1-curr_count
                max_so_far = curr_count
            curr_count = 1
    #final case after exiting loop
    if curr_count > max_so_far:
        max_pos = len(intvect)-curr_count
        max_so_far = curr_count
    return intvect[max_pos:max_pos+max_so_far]

x = [8, 42, 40, 45, 46, 44, 43, 50, 49]

def check_ascending(lst):
	for i in range(len(lst) - 1):
		if (lst[i] > lst[i+1]):
			return False
	return True

def longest_left(lst):
	if (len(lst) == 0) or (len(lst) == 1): 
		return lst
	index = 0
	while (index < (len(lst) - 1)) and (lst[index] <= lst[index+1]):
		index+=1
	return lst[:index+1]

def longest_right(lst):
	if len(lst) == 0 or len(lst) == 1: return lst
	index = len(lst) - 1
	while (index > 0) and (lst[index - 1] <= lst[index]): 
		index -= 1
	return lst[index:]

def merge(x, y):
	l1 = x[1]
	lr1 = x[2]
	ll1 = x[3]
	l2 = y[1]
	lr2 = y[2]
	ll2 = y[3]

	c = x[0] + y[0]
	test = lr1 + ll2 # middle ascending list
	test = find_longest(test)
	if len(l1) > len(l2):
		longest = l1
	else:
		longest = l2
	if check_ascending(test) and len(test) > len(longest): # if middle list is asscending and longer than longest, update longest
		longest = test
	new_lr = longest_right(c)
	new_ll = longest_left(c)
	return(c, longest, new_lr, new_ll)

def sort(lst):
	if len(lst) == 0 or len(lst) == 1:
		return (lst,lst,lst,lst)
	middle = len(lst) // 2
	if len(lst) == 2:
		first_half = (lst[:middle], lst[:middle], lst[:middle], lst[:middle])
		second_half = (lst[middle:], lst[middle:], lst[middle:], lst[middle:])
		return merge(first_half, second_half)
	else:
		first_half = sort(lst[:middle])
		second_half = sort(lst[middle:])
		return merge(first_half, second_half)

def mergesort(lst):
	return sort(lst)[1]
	

