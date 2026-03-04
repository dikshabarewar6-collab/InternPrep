# Dictionary

student = {
    "name": "Diksha",
    "age": 20,
    "course": "AIML",
}

print(student["name"])
print(student["course"])

#change value
student["age"] = 21
print(student)


#New data add
student["college"] = "TIT Bhopal"


#Delete
del student["age"]
print(student)

#Loop

student = {
    "name": "Diksha",
    "age": 20,
    "course": "AIML"
}

for key in student:
    print(key, ":", student[key])


#Dictionary function

print(student.keys())
print(student.values())
print(student.items())

#Robot sensor data

sensor = {
    "temperature": 35,
    "humidity": 60,
    "gas_level": 120
}

if sensor["gas_level"] > 100:
    print("Gas Alert!")
else:
    print("Safe")