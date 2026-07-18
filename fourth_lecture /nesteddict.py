student = {
    "name" : "granth soni",
    "subjects" : {
        "physics" : 65,
        "chemistry" : 71,
        "biology" : 88
    }
}


print(list(student.keys()))
print(list(student.values()))
print(student.items())





new_dict = {"city" : "delhi"}
# '''print(student.get("name2")) #error create kr deti h ye 
# print(student.get["name2"]) #error create kr deti h ye'''
 

new_dict = {"name": "rohit kumar ", "age": "17"}
student.update(new_dict)
print(student)