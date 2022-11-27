val =5

print("--- Inverted Half Pyramid Number Pattern ---")
for i in range(0,val):
	for j in range(0,val-i+1):
		print(j,end='.')
	print(' ')