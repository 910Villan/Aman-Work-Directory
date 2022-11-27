val = 6
print("--- Inverted Pyramid of Descending Numbers ---")
for i in range(1,val+1):
	for j in range(val-i+1):
		print(j + 1,end=' ')
	print(' ')