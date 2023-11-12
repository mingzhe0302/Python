#A slicing expression select a range of elements from a sequence.
#Format: list_name[start : end]
#The expression returns a list containing a copy of the elements form start up to(but not including)end.

numbers = [1, 2, 3, 4, 5, 6]
midNum = numbers[2 : 4]
print(midNum)  #result is [3, 4]

#If you leave out the start index, uses 0 as the starting index
print(numbers[:3])  #[1, 2, 3]

#If you leave out the end index in a slicing expression, Python use the length of the list as the end index
print(numbers[2:])  #[3, 4, 5, 6]

#If you leave both, you get a copy of the entire list.
print(numbers[:])   #[1, 2, 3, 4, 5, 6]





