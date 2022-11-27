def count(s1, s2):
    c=0 #counter variable
    j=0
    for i in s1:
        if s2.find(i)>-1 and j==s1.find(i):
            c=c+1
        j=j+1
    print("Matching char: ",c)
    

s1="abcdef"
s2="a b c d 1"
count(s1,s2)