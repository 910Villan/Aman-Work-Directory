#1
arr_Num = [1,2,3,4,5,6,7]
print(arr_Num)

#2
arr_Char = ["one","two","three","four","five","six","seven"]
print(arr_Char)

#3
arr1 = ["one","two","three","four","five","six","seven"]
arr2 = arr1
print(arr1)

#4
x= arr1.index("three")
print(x)

y = arr1[4]
print(y)

#5
arr_Retrive = ["one","two","three","four","five","six","seven"]
new_List = 0
x = len(arr_Retrive)
print("--- Printing New List ---------\n")
while new_List < x:
	print(arr_Retrive[new_List])
	new_List += 1

#6.1
arr_Slicing =  ["one","two","three","four","five","six","seven","eight","nine","ten"]
y = arr_Slicing[0:3]
print(y)

#6.2
y1 = arr_Slicing[-4:]
print(y1)

#6.3
y2 = arr_Slicing[0:]
print(y2)

#7.1
arr_Num1 = [10,20,30,40,50,60,70]
print(arr_Num1)

#7.2
y7 = arr_Num1[2:5]
print(y7)

#8
#Calculating the Total and Percentage.
print("Enter the Marks of Three Subjects")
sub_1 = float(input("Enter the Marks of Subject One :-"))
sub_2 = float(input("Enter the Marks of Subject Two :-"))
sub_3 = float(input("Enter the Marks of Subject Three :-"))

total,percentage,average,grade = None,None,None,None

total = sub_1 + sub_2 + sub_3
average = total/3.0
percentage = (total/300.0)*100


if average > 90:
	grade = 'A'
elif average >= 80 and average < 90:
	grade = 'B'
elif average >= 70 and average < 80:
	grade = 'C'
elif average >= 60 and average < 70:
	grade = 'D'
elif average >= 50 and average < 60:
	grade = 'E'
else:
	grade = 'F'

print("\n The Total Marks is :\t",total,"/300.00")
print("\nThe Average Marks is :\t",average)
print("\nThe Percentage Marks is :\t",percentage,"%")
print("\nThe Grade is :\t",grade)

#9.1
import array as arr
arr_Method = [1,2,3,4,5,6,7,8,9,10]
print(arr_Method)

#9.2
arr_Method.append(30)
print(arr_Method)

#9.3
arr_Method.insert(1,99)
print(arr_Method)

#9.4
arr_Method.remove(9)
print(arr_Method)

#9.5
arr_Method.pop()
print(arr_Method)

#9.6
print(arr_Method.index(2))

#9.7
x = arr.array('i',[1,2,3,4,5,6,7,8,9,10])
convert_List = x.tolist()
print(convert_List)

#10
