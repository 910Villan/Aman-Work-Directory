# String format
age = 44
txt = "My name is Aman, I am " + str(age)
print(txt)

## ---- Combine string and number by using the format() method
age = 52
txt = "My name is raj, and I am {}"
print(txt.format(age))

quantity = 3 
itemNo = 754
price = 75.90
myOrder = "I want {} pieces of item {} for {} dollars."
print(myOrder.format(quantity,itemNo,price))

#to Insert an to end of List,use the listName.insert() method 
thisList = ['apple','banana','cherry']
thisList.insert(4,"orange")
print(thisList)

#to Append an to end of List,use the listName.append() method
thisList = ["Aman","Jay","Ashish","Nil","Brijesh"]
thisList.append("Jayesh")
print(thisList)