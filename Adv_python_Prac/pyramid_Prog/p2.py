val = 5
count =1
print("--- Inverted Pyramid of Numbers ---")
for i in range(1,val+1):
	for j in range(1,i+1):
		print(count+j-1,end = " ")
	print(" ")