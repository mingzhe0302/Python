#1. Creating a set
myset = set()   #empty set

#can pass list, tuple, or string
myset1 = set(['a', 'b', 'c'])

myset2 = set('abc')

#set cannot contain duplicate elements
myset3 = set('aaabc')

#we have to pass a list containing the string
myset4 = set(['one', 'two', 'three'])

#
#
#


#2. Getting the number of elements in a set
print(len(myset4))   #3

#
#
#

#3. Adding and Removing elements
numSet = set()
numSet.add(1)
numSet.add(2)
numSet.add(3)

print(numSet)

set1 = set([1, 2, 3])
set2 = set([8, 9, 10])
set1.update(set2)
print(set1)

set1.update('abc')
print(set1)


set1.remove(1)
print(set1)
set1.discard(2)
print(set1)



#4. Using the for loop to iterate over a set
x = set(["a", "b", "c", 1, 2, 3])
for val in x:
    print(val)

y = set([1, 2, 3])
if 1 in y:
    print("The value 1 is in the set.")


#5. Find the Union of Sets
set3 = x.union(y)
print(set3)

#OR

set3 = x | y
print(set3)

#6. Find the intersection of Sets
set3 = x.intersection(y)
print(set3)

#OR
set3 = x & y
print(set3)

#7. Find the difference of sets
set3 = x.difference(y)
print(set3)

#OR
set3 = x - y
print(set3)


