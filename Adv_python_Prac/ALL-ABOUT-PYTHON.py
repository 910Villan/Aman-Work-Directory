# #(q1)
# name = "brijesh"
# #1st method
# print("length of a string is: "+str(len(name)))
# #2nd method
# count=0
# for i in name:
#     count = count+1
# print("length of a string is: "+str(count))

# #(q2)
# revstr = ""
# count = len(name)
# while(count>0):
#     revstr = revstr + name[count-1]
#     count = count-1
# print("the reversed string is: "+revstr)


# #(q3)
# names = "google.com"
# dict = {}
# for i in names:
#     if i in dict:
#         dict[i] = dict[i]+1
#     else:
#         dict[i] = 1
# print(dict)


# #(q4)

# str1 = "restart"
# char1 = str1[0]
# newstr = str1.replace(char1,'$')
# newstr = char1 + newstr[1:]
# print("output is: "+newstr)

# #(q5)

# stra = "abc"
# strb = "xyz"
# new_a = strb[:2] + stra[2:]
# new_b = stra[:2] + strb[2:]
# print("output is: "+ new_a + " " + new_b)


# #(q6)

# str = "abc"
# length = len(str)
# if length>=3:
#     if str[-3:] == "ing":
#         str = str + "ly"
#     else:
#         str = str + "ing"

# print(str)

# #(q7)
# #def word_count(str1):
#  #   counts= dict()
#   #  words = str1.split()
#    # for word in words:
#     #    if word in counts:
#      #       counts[word] = counts[word] + 1
#       #  else:
#        #     counts[word] = 1
#    # return counts

# #print(word_count("the quick brown fox jumps over the lazy dog"))

# #(q8)

# user_input = input("what is your name")
# print("lowercase: "+user_input.lower())
# print("uppercase: "+user_input.upper())

# #(q9)
# words = input("enter a comma separated syntax").split(',')
# words.sort()
# words = set(words)
# print(",".join(words))

# #(q10)

# str1 = "my name is brijesh"
# words = str1.split(" ")
# reverse_string = ' '.join(reversed(words))
# print(reverse_string)

# #(q11)

# str = "BRIJESH"
# string = str.lower()
# vowel = [string.count('a'), string.count('e'), string.count(
#         'i'), string.count('o'), string.count('u')]
# if vowel.count(0)>0:
#     print("not accepted")
# else:
#     print("accepted")

# #q12

# str1= "brijesh"
# str2= "bhavesh"
# set_str1 = set(str1)
# set_str2 = set(str2)
# matching_char = set_str1 & set_str2
# print(matching_char)
# print("number of matching character is: "+str(len(matching_char)))
# print("matching character are")
# print(','.join(matching_char))


#(q13)
#patters starts
#(q1)
# for i in range(1,6):
#     for j in range(i):
#         print(i,end="")
#     print(" ")

# #(q2)
# col = 5
# for i in range(1,6):
#     for j in range((col-i)+1):
#         print(i,end=" ")
#     print(" ")

# #(q3)
# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print(" ")

# #(q4)
# col=5
# for i in range(1,6):
#     for j in range((col-i)+1):
#         print(col-i+1,end=" ")
#     print("")
    
# #(q5)

# num = 5
# for i in range(1,6):
#     for j in range((num-i)+1):
#         print(num,end=" ")
#     print("")

# #(q6)
# for i in range(1,6):
#     num = i
#     for j in range(i):
#         print(num,end=" ")
#         num = num-1
#     print("")

# #(q7)
# col = 6
# for i in range(1,6):
#     num = 0
#     for j in range((col-i)+1):
#         print(num,end=" ")
#         num = num+1
#     print("")

# #(q8)
# num=1
# for i in range(1,4):
#     for j in range((i+i)-1):
#         print(num,end=" ")
#         num = num+1
#     print("")

# #(q9)

# start = 1
# stop = 2
# current = stop
# for i in range(2,6):
#     for j in range(start,stop):
#         current = current-1
#         print(current,end=" ")
#     print("")
#     start=stop
#     stop = stop+i
#     current = stop

# #(q10)
# for i in range(1,6):
#     num=1
#     for j in range(i):
#         print(num,end=" ")
#         num = num+1
#     for k in range(i-1,0,-1):
#         print(k,end=" ")
#     print("")

# #(q11)
# col=5
# for i in range(1,6):
#     num=5
#     for j in range((col-i)+1):
#         print(num,end=" ")
#         num = num-1
#         no = i
#     for k in range((col-i)+1):
#         print(no,end=" ")
#         no = no+1
#     print("")

# #(q12)
# for i in range(1,6):
#     num=10
#     for j in range(i):
#         print(num,end=" ")
#         num = num-2
#     print("")

# #(q13)
# no=1
# for i in range(1,8):
#     num = 0
#     no = i-1
#     for j in range(i):
#         print(num,end=" ")
#         num = num+no
#     print("")

# #(q14)
# num = 1
# for i in range(1,6):
#     for j in range(i):
#         print(num,end=" ")
#     print("")
#     num = num+2

# #(q15)
# col = 5
# for i in range(1,6):
#     num=1
#     for s in range(col-i):
#         print(" ",end=" ")
#     for j in range(i):
#         print(num,end=" ")
#         num = num+1
#     print("")
# #q16
# n=20
# for i in range(1,6):
#     for s in range(n):
#         print(" ",end="")
#     for j in range(i):
#         print("*",end=" ")
#     print("")
#     n = n-1

# #q17
# n=15
# col=7
# for i in range(1,7):
#     for s in range(n):
#         print(" ",end="")
#     for j in range(col-i):
#         print("*",end=" ")
#     print("")
#     n = n+1

# #q18
# for i in range(1,6):
#     for j in range(i):
#         print("*",end=" ")
#     print(" ")

#pattern ends


#-----Sequence------
# - input value : 7
# Sequence 1,4,9,16,25,36,49...

# n=int(input("Enter Your Choice Number-->"))
# l1=[]
# for i in range(1,n+1):
#     l1.append(i*i)
# print("Sequence--> ",l1)

# - input value : 7
# sequence 1,8,15,22,29,36,43

# n = int(input("Enter Your Choice Number-->"))
# ans = 1
# print("Sequence -->",end=" ")
# for i in range(1,n+1):
#     print(ans,end=" ")
#     ans+=7

# - input value : 7
# sequence 50,35,26,15,10,3,2

# n = int(input("Enter Your Choice Number-->"))
# ans = 1
# l1=[]
# for i in range(n,0,-1):
#     if(i % 2 !=0):
#         l1.append((i*i)+1)
#     else:
#         l1.append((i*i)-1)
# print("Sequence--> ",l1)

# - input value : 5
# sequence 5,10,30,120,600

# n = int(input("Enter Your Choice Number-->"))
# cal = 5
# l1=[]
# for i in range(1,n+1):
#     cal*=i
#     l1.append(cal)
# # print("Sequence-->",l1)

# create UDF to do following:
# - factorial
# def factorial(n):
#     fact=1
#     while(n>=1):
#         fact*=n
#         n-=1
#     return fact
# n = int(input("Enter your choice number-->"))
# print(f"factorial of {n} is ",factorial(n))

# - whether given no. is prime or not
# def prime_or_not(n):
#     count=0
#     for i in range(1,n+1):
#         if n%i==0:
#            count+=1
#     if (count==2):
#         return f"{n} is prime number."
#     else:
#         return f"{n} is not prime number."
# n=int(input("Enter your choice number-->"))
# print(prime_or_not(n))

# - find divisiors of the no
# def divisior(n):
#     lst=[]
#     for i in range(1,n+1):
#         if(n%i==0):
#             lst.append(i)
#         return lst
# n=int(input("Enter Any Number-->"))
# print(f"Divisior of{n} is == ",divisior(n))


# - fibonacci series (1 1 2 3 5 8 ...)
# def fibonacci(n):
#     if(n==0):
#         return 0
#     elif(n==1):
#         return 1
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)
# n=int(input("Enter Number Till You Print Febonacci Series -->"))
# print(f"Fibonacci of 0-{n} -> ",end="")
# for i in range(n):
#     print(fibonacci(i),end=" ")
    


# String 
# - take sentence from user and print it in toggle case
# str = input("Enter String -->")
# toogle_str=str.swapcase()
# print("Toogle Case String --> ",toogle_str)

# - take password from user and check it for below rules:
# - must be of length 8
# - it should contain minimum 1 special symbol
# - it should contain minimum 1 upper case
# - it should contain minimum 1 digit

# p = input("Enter Your Password -> ")
# spc = 0
# lc = 0
# d = 0
# uc = 0
# if(len(p) >= 8):
#     for i in p:
#         if(i.isupper()):
#             uc += 1
#         elif(i.islower()):
#             lc += 1
#         elif(i.isnumeric()):
#             d += 1
#         else:
#             spc += 1
            
#     if(spc >= 1):
#         if(lc >= 1):
#             if(d >= 1):
#                 if(uc >= 1):
#                     print("Password is Valid.")
#                 else:
#                     print("Uppercase character is not present in your password Please enter password that have atleast one Uppercase charactor.")
#             else:
#                 print("Digit is not present in your password Please enter password that have atleast one digit.")
#         else:
#             print("Lowercase character is not present in your password Please enter password that have atleast one Lowercase charactor.")
#     else:
#         print("Special Symbol is not present in password Please enter password that have atleast one special symbol.")
    
# else:
#     print("Please Enter Password which is more then 8 character.")
        

    

# list, tuple,set
# - take list of products from user ask user to provide name of product they want to search 
# and print the message if it's available in a list or not.
# pro_name = [i for i in input("Enter Product Name -> ").split(",")]
# print("product List -> ",pro_name)

# search = input("Enter Product Name which you can search -> ")
# if search in pro_name:
#     print(f"{search} is present in List.")
# else:
#     print(f"{search} is not present in List.")

# - create dictionary with productname as key and price as value ask user what they want to 
# purchase and in which quantity, then generate the bill.....
# {"Pen":10,"Pencil":5,"Eraser":3,"Laptop":25000}
# Pen : 10
# Pencil : 5
# What you want to purchase? : pen
# in what quantity? : 10
# What you want to purchase? : mouse
# mouse is not availabel sorry.

# product_dict = {
#     "pen":10,
#     "pencil":5,
#     "eraser":3,
#     "laptop":25000
# }


# print("|--------------PRODUCT DETAILS------------|")
# for iname,iprice in product_dict.items():
#     print(f"Product Name = {iname}  Product Price = {iprice}")
# print("|-----------------------------------------|")
    
# total_price = 0
# product_lst = set()
# while(True):
#     purchase_item = input("What you want to Purchase? -> ").lower()
#     if purchase_item in product_dict.keys():
        
#         product_lst.add(purchase_item)
        
#         qty = int(input("In what quantity you purchase -> "))
#         product_prc = product_dict[purchase_item]
#         total_price += product_prc * qty
#         bill = input("You Genrate Bill Now(yes/no)? -> ")
        
#         if(bill == "yes" or bill=="Yes"):
#             print("\n\n")
#             print("--------------BILL--------------")
#             print("Purchase Product -> ",product_lst)
#             print("Total Bill       -> ",total_price)
#             print("--------------------------------")
#             break
#         elif(bill == "no" or bill=="No"):
#             continue
#         else:
#             print("Invalid Choice...")
#             continue
        
#     else:
#         print(f"{purchase_item} is not availble now sorry.")


#  Python program to print "Hello Python"
# print("Hello Pyhton")

#  Python program to do arithmetical operations
# n1 = int(input("Enter First Number            -> "))
# n2 = int(input("Enter Second Number           -> "))
# op = input("Enter Which Operation you perform -> ")
# if(op=='+'):
#     print(f"\n Addition of {n1} + {n2} = {n1 + n2}")
# elif(op == '-'):
#      print(f"\n Subtraction of {n1} - {n2} = {n1 - n2}")
# elif(op == '*'):
#      print(f"\n Multiplication of {n1} * {n2} = {n1 * n2}")
# elif(op == '/'):
#      print(f"\n Division of {n1} / {n2} = {round(n1 / n2,2)}")
# else:
#     print("\n Invelid Operator..")
#     exit()

#  Python program to find the area of a triangle
# h=float(input("Enter Hight of Tringle ->"))
# b=float(input("Enter Base of Tringle ->"))
# area=round(b*h/2,2)
# print("Area of Tringle Is-->",area)

#  Python program to solve quadratic equation


#  Python program to swap two variables
# n1 = int(input("Enter Value of N1 -> "))
# n2 = int(input("Enter Value of N2 -> "))

# print("-------Number Before Swap-------")
# print("N1 -> ",n1)
# print("N2 -> ",n2)

# n1,n2 = n2,n1

# print("-------Number After Swap-------")
# print("N1 -> ",n1)
# print("N2 -> ",n2)

#  Python program to generate a random number
# import random
# n=random.random()
# n=random.randint(0,10)
# n=random.sample(range(10,20),5)
# print("Enter Random Number is=",n)

#  Python program to convert kilometers to miles
# k = float(input("Enter Kilometer -> "))
# mile = k * (0.621371)
# print(f"{k} Kilometer = {round(mile,3)} Mile")

#  Python program to convert Celsius to Fahrenheit
# Celsius to Fehrenheit
# f = c*(9/5)+32

# c = float(input("Enter Celsius -> "))
# f = round(c*(9/5)+32,3)
# print(f"{c} Celsius = {f} Fehrenheit")

#  Python program to display calendar
# import calendar
# yy = int(input("Enter Which Year Calender You print -> "))
# mm = int(input("Enter Which Month Calender You Print -> "))
# print(calendar.month(yy,mm))

# yy = int(input("Enter Which Year Calender You print -> "))
# print(calendar.calendar(yy))

#  Python Program to Check if a Number is Positive, Negative or Zero
# n=int(input("Enter Number:"))
# if(n>0):
#     print("Number is Positive")
# elif(n<0):
#     print("Number is Negetive")
# else:
#     print("Number is Zero")

#  Python Program to Check if a Number is Odd or Even
# n = int(input("Enter Number -> "))
# if(n % 2 == 0):
#     print(f"{n} is Even Number...")
# else:
#     print(f"{n} is Odd Number...")
    
#  Python Program to Check Leap Year
# y = int(input("Enter Year -> "))
# if(y % 4 == 0 and y % 100 == 0 or y % 400 == 0):
#     print(f"{y} is Leap Year....")
# else:
#     print(f"{y} is not a Leap Year....")
    

#  Python Program to Check Prime Number
# n = int(input("Enter Your Choice Number -> "))
# count = 0 
# for i in range(1,n+1):
#     if(n % i == 0):
#         count += 1
# if(count == 2):
#     print(f"{n} is Prime Number.")
# else:
#     print(f"{n} is not a Prime Number.")
    
        
#  Python Program to Print all Prime Numbers in an Interval
# n = int(input("Enter Range -> "))
# l1 = []
# for i in range(1,n+1):
#     count = 0
#     for j in range(1,i+1):
#         if(i % j == 0):
#             count += 1
#     if(count == 2):
#         l1.append(j)
#     else:
#         pass
# print(f"Prime Numbers Between 1 To {n} => ",l1)


# Python Program to Find the Factorial of a Number
# n = int(input("Enter Number -> "))
# fact = 1
# for i in range(1,n+1):
#     fact *= i
# print(f"Factorial of {n} is {fact}")

#  Python Program to Display the multiplication Table
# n = int(input("Enter Your Choice Number Which Multiplication table You Needed -> "))
# for i in range(1,11):
#     print(f"{n} X {i} = {n*i}")

#  Python Program to Print the Fibonacci sequence
# def fibonacii(n):
#     if(n==0):
#         return 0
#     elif(n==1):
#         return 1
#     else:
#         return fibonacii(n-1) + fibonacii(n-2)
    
    
# n = int(input("Enter Range -> "))
# print(f"Fibonacci Between 0 To {n} => ",end=" ")
# for i in range(n):
#     print(fibonacii(i),end=" ")
    

#  Python Program to Check Armstrong Number
# n = int(input("Enter Your Choice Number -> "))
# n_str = str(n)
# len = len(n_str)
# sum = 0
# for i in n_str:
#     d_cube = 1
#     for j in range(len):
#         i = int(i)
#         d_cube *= i 
#     sum += d_cube


# if(sum == n):
#     print(f"{n} is Armstrong Number.")
# else:
#     print(f"{n} is not a Armstrong Number.")


#  Python Program to Find Armstrong Number in an Interval
# r = int(input("Enter Range -> "))

# arm = []
# arm_not = []
# for i in range(0,r):
#     str_i = str(i)
#     length = len(str_i)
#     sum = 0
#     for j in str_i:  
#         d_calc = 1
#         for k in range(1,length+1):
#             j = int(j)
#             d_calc *= j
#         sum += d_calc

#     if(i == sum):
#         arm.append(i)
#     else:
#         arm_not.append(i)    


# print(f"Armstrong Number Between 1-{r} => ",arm)




#  Python Program to Find the Sum of Natural Numbers
# n = int(input("Enter Range -> "))
# sum = 0
# for i in range(1,n+1):
#     sum += i
    
# print(f"Sum of 1-{n} = {sum}")

#  Write the program to remove the duplicate element of the list.
# o_list = input("Enter List Element -> ").split(",")
# print("Orignal List -> ",o_list)

# s1 = set(o_list)
# r_list = list(s1)

# print("Required List -> ",r_list)


#  Write a program to find the sum of the element in the list.


#  Write the program to find the lists consist of at least one common element.
# l1 = [[1,2,3],[1,2,1],[2,3,4],[6,6,6],[8,9,10],[12,13,12]]
# l2 = []
# for i in l1:
#     for j in i:
#         c = i.count(j)
#     if(c > 1):
#         l2.append(i)
# print("Required List -> ",l2)


#  Write the Python program to show that Python tuples are immutable objects.
# tp1 = (1,2,3,4,5)
# print("Tuple = ",tp1,type(tp1))
# tp1[1] = 786
# print("Tuple After Change -> ", tp1)