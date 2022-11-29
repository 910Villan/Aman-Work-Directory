# #(q1)
# for i in range(1,6):
#     for j in range(i):
#         print(i,end=" ")
#     print(" ")
# print("\n")

# #(q2)
# col = 5
# for i in range(1,6):
#     for j in range((col-i)+1):
#         print(i,end=" ")
#     print(" ")
# print("\n")

# #(q3)
# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print(" ")
# print("\n")

#(q4)
# col=5
# for i in range(1,6):
#     for j in range(col-i+1):
#         print(col-i+1,end=" ") #5-2+1 =4
#     print("")
# print("\n")

# #(q5)
# num = 5
# for i in range(1,6):
#     for j in range(num-i+1):
#         print(num,end=" ")
#     print("")
# print("\n")


# #(q6)
# for i in range(1,6):
#     num = i
#     for j in range(i):
#         print(num,end=" ")
#         num = num-1
#     print("")
# print("\n")


#(q7)
col = 6
for i in range(1,6):
    num = 1
    for j in range((col-i)+1): #6 - 1 + 1 = 6
        print(num,end=" ")
        num = num+1  # 1 + 1 = 2
    print("")
print("\n")

#(q8)
num=1
for i in range(1,4):
    for j in range((i+i)-1):
        print(num,end=" ")
        num = num+1
    print("")

#(q9)

start = 1
stop = 2
current = stop
for i in range(2,6):
    for j in range(start,stop):
        current = current-1
        print(current,end=" ")
    print("")
    start=stop
    stop = stop+i
    current = stop

#(q10)
for i in range(1,6):
    num=1
    for j in range(i):
        print(num,end=" ")
        num = num+1
    for k in range(i-1,0,-1):
        print(k,end=" ")
    print("")

#(q11)
col=5
for i in range(1,6):
    num=5
    for j in range((col-i)+1):
        print(num,end=" ")
        num = num-1
        no = i
    for k in range((col-i)+1):
        print(no,end=" ")
        no = no+1
    print("")

#(q12)
for i in range(1,6):
    num=10
    for j in range(i):
        print(num,end=" ")
        num = num-2
    print("")

#(q13)
no=1
for i in range(1,8):
    num = 0
    no = i-1
    for j in range(i):
        print(num,end=" ")
        num = num+no
    print("")

#(q14)
num = 1
for i in range(1,6):
    for j in range(i):
        print(num,end=" ")
    print("")
    num = num+2

#(q15)
col = 5
for i in range(1,6):
    num=1
    for s in range(col-i):
        print(" ",end=" ")
    for j in range(i):
        print(num,end=" ")
        num = num+1
    print("")
#q16
n=20
for i in range(1,6):
    for s in range(n):
        print(" ",end="")
    for j in range(i):
        print("*",end=" ")
    print("")
    n = n-1

#q17
n=15
col=7
for i in range(1,7):
    for s in range(n):
        print(" ",end="")
    for j in range(col-i):
        print("*",end=" ")
    print("")
    n = n+1

#q18
for i in range(1,6):
    for j in range(i):
        print("*",end=" ")
    print(" ")
