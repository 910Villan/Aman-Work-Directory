## 1

# str1 = input("Enter Something")
# print("Length of String : ",len(str1))

## 2
#Reverse a String

# my_string=("Aman is Good and Well")
# str2=""
# for i in my_string:
#     str2=i+str2
# print("Reversed string:",str2)

##3
##count the number of characters (character frequency)

# my_string=("google.com")
# userInput = input("What is Input -")

# all_Freq = {}
# for i in userInput:
# 	if i in all_Freq:
# 		all_Freq[i] = all_Freq[i] + 1
# 	else:
# 		all_Freq[i] = 1
# print("count the number of Character\n",all_Freq)	

##4
##5

# a="abc"
# b="xyz"
# new1 = b[2:]
# print(new1)
# new_b = b[:2] + a[2:]
# new_a = a[:2] + b[2:] 
# print(new_a,new_b)


##6
# def word_count(str):
#     counts = {}
#     words = str.split()

#     for word in words:
#         if word in counts:

#             counts[word] = counts[word] + 1
#         else:
#             counts[word] = 1

#     return counts
# print(word_count("the quick brown fox jumps over the lazy dog."))

# ##7
# str1 = input("Enter a value - ")
# def add_string(str1):  
#   length = len(str1)  
  
#   if length > 2:  
#     if str1[-3:] == 'ing':  
#       str1 += 'ly'  
#     else:  
#       str1 += 'ing'  
#   return str1

# print(add_string(str1))  
# print(add_string('abc'))  
# print(add_string('string'))

##8
# for i in range(0,5):
#     if i == 2:
#     	pass
#     print(i)
#9
# str1=input("enter the string:: ")
# if len(str1)==3:
#   if str1[-3:]=='ing':
#     str1+='ly'

# print(str1)

#10
# a = 10
# b = 20
  
# if(b<a):
# 	print("b<a")
# else:
# 	pass
# 	print("a<b")

# Write a Python program to calculate the length of a string.
# string1=input("enter the string ::")
# len1=len(string1)
# print(len1)
# Write a Python program to print the string in reverse order.
# strrev=string1[::-1]
# print(strrev)

# Write a Python program to count the number of characters (character frequency) in a string.
# String : 'google.com'
# Expected Result : {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}

# Python3 code to demonstrate each occurrence frequency using
# collections.Counter()
# from collections import Counter

# initializing string
# test_str = string1

# using collections.Counter() to get
# count of each element in string
# res = Counter(test_str)

# # printing result
# print ("Count of all characters in "+test_str+ "is :\n "
# 										+ str(res))
# all={}
# for i in string1:
# 	if i in all:
# 		all[i]+=1
# 	else:
# 		all[i]=1
# print(all)

def change_char(str1):
  char = str1[0]
  str1 = str1.replace(char, '$')
  str1 = char + str1[1:] 
  return str1
print(change_char('restart'))


# x=input("enter s1")
# y=input("enter s2")
# #abz xyc
# a=x[:2]+y[2:]
# b=y[:2]+x[2:]
# print(a+" "+b)


#9

# test_string = "the quick brown fox jumps over the lazy dog."
 
# # printing original string
# print ("The original string is : " +  test_string)
# res = len(test_string.split())
 
# # printing result
# print ("The number of words in string are : " +  str(res))
