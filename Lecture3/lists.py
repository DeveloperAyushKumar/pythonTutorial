age =[3,4 ,4,5]
print(age)
print(len(age))
contact=[33,"delhi",3984]
# lists are mutable 
# strings are not mutable 
sliced=contact[2:3]
print(contact)
print(sliced)

contact=["hello","hey","no integer allowed in sort"]
contact.append("ak")
contact.sort()
contact.sort(reverse=True)
contact.reverse()
contact.insert(3,"pp")
print(contact)
contact.remove("pp") #element
contact.pop(3) #index