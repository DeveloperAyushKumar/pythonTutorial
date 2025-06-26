import os
# print("Current Working Directory:", os.getcwd())

script_dir = os.path.dirname(os.path.abspath(__file__))
print(script_dir)
# Build full path to the file.txt located in the same folder as the script
file_path = os.path.join(script_dir, "file.txt")
print(file_path)
f =open(file_path,"r")
# data=f.read()
# data=f.read(5)


# print(data)
# print(type(data))
# print(type(f))

# line =f.readline()
# print(line)
# f.close()
file_path2=os.path.join(script_dir,"file2.txt")
f=open(file_path,"a")
f.write("\npython is super crazy. 95")
f.close() 
f=open(file_path2,"a")
f.write('hello new file created')
f.close()

with open(file_path) as f :
     print(f.read())


import os  
os.remove(file_path2)

def check_for_line():
     word="learning"
     data=True
     line_no=1
     with open("practic.txt","r") as f:
          while data :
               data=f.readline()
               if(word in data):
                    break
               line_no+=1

