# -*- coding: utf-8 -*-
"""array.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1JTOkC-g8WXGv0Msu3aViV7v8A63Z_-dd
"""

# Python program to demonstrate
# Creation of Array
 
# importing "array" for array creations
import array as arr
 
# creating an array with integer type
a =arr.array('i', [1, 2, 3])
 
# printing original array
print ("The new created array is : ", end =" ")
for i in range (0, 3):
    print (a[i], end =" ")
print()
 
# creating an array with double type
b = arr.array('d', [2.5, 3.2, 3.3])
 
# printing original array
print ("The new created array is : ", end =" ")
for i in range (0, 2):
    print (b[i], end =" ")

my_array = arr.array('i', [1,2,3,4,5])
print(my_array[1])
# 2
print(my_array[2])
# 3
print(my_array[0])
# 1

#simple example of an array containing 5 integers
my_array = arr.array('i', [1,2,3,4,5])
for i in my_array:
  print(i)
# 1
# 2
# 3
# 4
# 5

my_array = arr.array('i', [1,2,3,4,5])
my_array.append(6)
# array('i', [1, 2, 3, 4, 5, 6])

# Python program to demonstrate
# Adding Elements to a Array
 
# importing "array" for array creations
import array as arr
 
# array with int type
a = arr.array('i', [1, 2, 3])
 
 
print ("Array before insertion : ", end =" ")
for i in range (0, 3):
    print (a[i], end =" ")
print()
 
# inserting array using
# insert() function
a.insert(1, 4)
 
print ("Array after insertion : ", end =" ")
for i in (a):
    print (i, end =" ")
print()
 
# array with float type
b = arr.array('d', [2.5, 3.2, 3.3])
 
print ("Array before insertion : ", end =" ")
for i in range (0, 3):
    print (b[i], end =" ")
print()
 
# adding an element using append()
b.append(4.4)
 
print ("Array after insertion : ", end =" ")
for i in (b):
    print (i, end =" ")
print()

# Python program to demonstrate
# accessing of element from list
 
# importing array module
import array as arr
 
# array with int type
a = arr.array('i', [1, 2, 3, 4, 5, 6])
 
# accessing element of array
print("Access element is: ", a[0])
 
# accessing element of array
print("Access element is: ", a[3])
 
# array with float type
b = arr.array('d', [2.5, 3.2, 3.3])
 
# accessing element of array
print("Access element is: ", b[1])
 
# accessing element of array
print("Access element is: ", b[2])

import array as arr
my_array = arr.array('i', [1,2,3,4,5])
my_extnd_array = arr.array('i', [7,8,9,10])
my_array.extend(my_extnd_array)
for x in my_array:
  print(x) 
# array('i', [1, 2, 3, 4, 5, 7, 8, 9, 10])



my_array = arr.array('i', [1,2,3,4,5])
my_array.insert(0,0)
#array('i', [0, 1, 2, 3, 4, 5])

#Add items from list into array using fromlist() method
my_array = arr.array('i', [1,2,3,4,5])
c=[11,12,13]
my_array.fromlist(c)
# array('i', [1, 2, 3, 4, 5, 11, 12, 13])

my_array = arr.array('i', [1,2,3,4,5])
my_array.remove(4)
# array('i', [1, 2, 3, 5])

#pop removes the last element from the array.
my_array = arr.array('i', [1,2,3,4,5])
my_array.pop()
# array('i', [1, 2, 3, 4])

#Fetch any element through its index using index() method
#index() returns ???rst index of the matching value. Remember that arrays are zero-indexed.

my_array = arr.array('i', [1,2,3,4,5])
print(my_array.index(5))
# 5
my_array = arr.array('i', [1,2,3,3,5])
print(my_array.index(3))
# 3

my_array = arr.array('i', [1,2,3,4,5])
my_array.reverse()
# array('i', [5, 4, 3, 2, 1])

#Check for number of occurrences of an element using count() method
my_array = arr.array('i', [1,2,3,3,5])
my_array.count(3)
# 2

# Python program to demonstrate
# slicing of elements in a Array
 
# importing array module
import array as arr
 
# creating a list
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
 
a = arr.array('i', l)
print("Initial Array: ")
for i in (a):
    print(i, end =" ")
 
# Print elements of a range
# using Slice operation
Sliced_array = a[3:8]
print("\nSlicing elements in a range 3-8: ")
print(Sliced_array)
 
# Print elements from a
# pre-defined point to end
Sliced_array = a[5:]
print("\nElements sliced from 5th "
      "element till the end: ")
print(Sliced_array)
 
# Printing elements from
# beginning till end
Sliced_array = a[:]
print("\nPrinting all elements using slice operation: ")
print(Sliced_array)

#This method provides you the array bu???er start address in memory and number of elements in array. Here is an
my_array = arr.array('i', [1,2,3,4,5])
my_array.buffer_info()

#2d array is as a list of lists.
lst=[[1,2,3],[4,5,6],[7,8,9]]

print (lst[0])
#output: [1, 2, 3]
print (lst[1])
#output: [4, 5, 6]
print (lst[2])
#output: [7, 8, 9]

print (lst[0][0])
#output: 1
print (lst[0][1])
#output: 2

myarray=[[[111,112,113],[121,122,123],[131,132,133]],[[211,212,213],[221,222,223],[231,232,233]],[[311,312,
313],[321,322,323],[331,332,333]]]

print(myarray)
print(myarray[1])
print(myarray[2][1])
print(myarray[1][0][2])