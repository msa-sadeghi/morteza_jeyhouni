# student = {
#     "name": "artin",
#     "age": 20,
#     "gender": "male",
#     "ave": 90
# }
# student["age"] = 18

# copy = student.copy()
# print(copy)
# copy.clear()
# print(copy)
# print(student["name"])
# print(student["age"])
# print(student["gender"])
# print(student["ave"])
# new_dict = dict.fromkeys(student)
# print(new_dict)
# new_dict["name"] = "morteza"
# new_dict["age"] = 17
# new_dict["gender"] = "male"
# new_dict["ave"] = 95
# print(new_dict)


student = {
    "name": "artin",
    "age": 20,
    "gender": "male",
    "ave": 90
}
# print(student["fathername"])
print(student.get("fathername"))

print(student.keys())
print(student.values())
print(student.items())
student2 = {
    "name": "sara",
    "age": 23,
    "gender": "female",
    "ave": 92
}
student.update(student2)
print(student2)