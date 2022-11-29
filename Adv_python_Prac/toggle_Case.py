string = input("Please Enter your Own String : ")

string1 = ''

for i in range(len(string)):
    if string[i]>='A' & string[i]<='Z':
        string[i] = (char) (string[i] + 'a' - 'A')
        
    else if string[i]>='a' & string[i]<='z':
        string[i] = (char) (string[i] + 'A' - 'a')
        
 
print("\nOriginal String      =  ", string)
print("The Given String After Toggling Case =  ", string1)