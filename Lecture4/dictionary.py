info ={
    "name ":"Ayush",
    "cgpa":9.06
}
# key can be int , float , string, tuple, as they are immutable 
print(info)
#dict are unordered
# no duplicate key
info["branch"]="Coe"
print(info)
nestedDict={
    "subject":{
        1:"physics",
        2:"math"
    }
}
print(nestedDict)
print(nestedDict.keys())
print(len((nestedDict)))
print(nestedDict.items())
print(nestedDict.get("subject")) # will return none if not present , no error 
newDict={"name":"ayush"}
nestedDict.update(newDict) #adds newDict to nestedDict






