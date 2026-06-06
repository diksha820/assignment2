#Python Dictionaries 

#1.	Create a dictionary to store a student's name, age, and city, and print the dictionary. 

student={"name":"diksha","age":23,"city":"pune"}
print(student)


#2.	Write a program to print all the keys of a dictionary. 
student={"name":"diksha","age":23,"city":"pune"}
print(student.keys())


#3.	Write a program to print all the values of a dictionary. 
student={"name":"diksha","age":23,"city":"pune"}
print(student.values())


#4.	Write a program to add a new key-value pair to an existing dictionary. 
student={"name":"diksha","age":23,"city":"pune"}
student["id"]=123
print(student)


#5.	Write a program to update the value of an existing key in a dictionary. 
student={"name":"diksha","age":23,"city":"pune"}
student["age"]=21
print(student)


#6.	Write a program to check whether a given key exists in a dictionary. 
student={"name":"diksha","age":23,"city":"pune"}
if "age" in student:
    print("key exists")
else:
    print("key does not exist")


#7.	Write a program to remove a key-value pair from a dictionary. 
student={"name":"diksha","age":23,"city":"pune"}
student.pop("city")
print(student)


#8.	Write a program to count the total number of key-value pairs in a dictionary. 
student={"name":"diksha","age":23,"city":"pune"}
print("total key",len(student))

#9.	Write a program to iterate through a dictionary and print all keys and their corresponding values. 
student={"name":"diksha","age":23,"city":"pune"}
for key,value in student.items():
    print(key,":",value)


#10.Create a dictionary of student names and marks, then find the student with the highest marks.
marks={"diksa":92,"aanu":95,"isha":93}
higest_student =max(marks,key=marks.get)
print("higest marks student:",higest_student)
print("marks",marks[higest_student])


