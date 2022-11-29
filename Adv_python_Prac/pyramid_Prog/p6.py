val = 5 
print("--- Reverse Pyramid of Number ---")
for i in range(1,val+1):
	for j in range(1,i+1):
		print(i-j,end = " ")
	print(" ")