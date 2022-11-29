quantity = 3
itemNo = 52
price = 23.44
myorder = "I want {} pieces of items {} for {} dollars\n"
print(myorder.format(quantity,itemNo,price))

quantity = 3
itemNo = 44
price = 23.44
myorder = "I want {2} pieces of items {0} for {1} dollars\n"
print(myorder.format(quantity,itemNo,price))