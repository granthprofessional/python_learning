#python can be used to perform operators on a file. (read & write data)
'''types of file
1. text files: .text, .docx, .log, etc
2. binary files: .jpg, .png, .mp3, .mp4, etc'''



# f = open("/Users/granthsoni/Documents/python/third_lecture/list.py", "r")
# data = f.read()
# print(data)
# print(type(data))
# f.close()

''' 
"r " - read only mode(default)
"w " - open for writting, truncating the file first
"x" - create file and open for it writting
"a" - open a wirriting appending to the end of the file if it exists
"b" - binary mode
"t" - text mode(default)
"+" - open a disk file for updating (reading and writing)'''



#second method to read a line from a file
f = open("/Users/granthsoni/Documents/python/third_lecture/list.py", "r" )
line1 = f.readline()
print(line1,2,3,4,5)

f.close()

#append to a file
f = open("demo.txt", "w")
f.write("Hello everyone\n")
f.write("This will overwrite old data")
f.close()

#with statement(auto close file)
with open("demo.txt", "r") as f:
    data = f.read()
    print(data)


#delete a file
import os
os.remove("demo.txt")
