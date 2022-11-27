val = 5
print("---  Inverted Pyramid of the Same Digit ---")
for i in range(val):
	for j in range(val-i + 1):
		print(val,end = " ")
	print(" ")
