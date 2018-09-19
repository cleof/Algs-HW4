
# def find_longest(lst):
# 	print("list: " + str(lst))
# 	if (len(lst)) == 0 or (len(lst)) == 1: return lst
# 	start = 0
# 	end = 1
# 	max_val = 1
# 	max_values = []
# 	for i in range(len(lst) - 1):
# 		print("max vals in loop: " + str(max_values))
# 		print(lst[i])
# 		if lst[i] <= lst[i+1]:
# 			print(str(lst[i]) + " vs. " + str(lst[i+1]))
# 			max_val+=1
# 			end+=1
# 			print("end: " + str(end))
# 			if (i+1) == len(lst):
# 				max_values.append((max_val, start, end))
# 				start = i+1
# 				end = i+2
# 		else:
# 			max_values.append((max_val, start, end))
# 			max_val = 0
# 			start = i+1
# 			end = i+2
# 	val = 0
# 	s = 0
# 	e = 0
# 	print("max vals: " + str(max_values))
# 	for m, begin, terminate in max_values:
# 		if (m > val):
# 			val = m
# 			s = begin
# 			e = terminate
# 	print("longest: " + str(lst[s:e]))
# 	return lst[s:e]
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
        elif intvect[counter1] > intvect[counter1-1]:
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
	end = 1
	for i in range(len(lst)-1):
		if lst[i] < lst[i+1]:
			end+=1
		else:
			return lst[0:end]

def longest_right(lst):
	start = len(lst) - 1
	while start > 0: 
		if (lst[start] > lst[start-1]):
			start = start - 1
		else:
			return lst[start:]

# def merge((a, l1, lr1, ll1),(b, l2, lr2, ll2)): # what happens when there is only 1 list (1 leave)
def merge(x, y):
	if x == [] and y == []: 
		return print("yikes")
	if x == []: 
		return (y, y, y, y)
	elif y == []: 
		return (x, x, x, x)
	# print(x)
	# print(y)
	a = x
	l1 = find_longest(a)
	lr1 = longest_right(a)
	ll1 = longest_left(a)
	b = y
	l2 = find_longest(b)
	lr2 = longest_right(b)
	ll2 = longest_left(b)
	print("a: " + str(a))
	print("b: " + str(b))
	# print("x: " + str(x) + ", y: " + str(y))
	c = a + b
	test = lr1 + ll2 # middle ascending list
	test = find_longest(test)
	if len(l1) > len(l2):
		longest = l1
	else:
		longest = l2
	# print("l1: " + str(l1))
	# print("l2: " + str(l2))
	# print("l1 or l2: " + str(longest))
	# print("test: " + str(test))
	if check_ascending(test) and len(test) > len(longest): # if middle list is asscending and longer than longest, update longest
		longest = test
	# print("longest after test: " + str(longest))
	new_lr = longest_right(c)
	new_ll = longest_left(c)

	return(c, longest, new_lr, new_ll)

g = (x[0:5])
y = (x[5:8])
# print("merge g and y: " + str(merge(g,y)))
# find_longest(x[0:5])

def mergesort(x):
# # """ Function to sort an array using merge sort algorithm """
    if (len(x) == 0):
        print("base case list: " + str(x))
        return x
    else:
        middle = len(x)//2
        if middle >= 2:
	        print("middle: " + str(middle))
	        x = mergesort(x[:middle])
	        y = mergesort(x[middle:])
	        print("merge x and y: " + str(merge(x,y)))
	        answer = merge(x,y)
	        # longest = answer[1]
	        # return longest
mergesort(x)
	

