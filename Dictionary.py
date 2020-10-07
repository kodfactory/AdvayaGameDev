# 

# listA = ["Jayesh", "Dhandha", "Vadodara", "InfoDesk", 500, 26]

# listA = ["Jayesh", "Dhandha", "InfoDesk", "Vadodara", 500, 26]

# print(listA[3])

dictA = {
    "nextCompany": "InfoDesk", "firstName": "Jayesh", "lastName": "Dhandha", 
    "currentCity": "Vadodara", 
    "Salary": 500, "age": 26
}

# print(dictA["age"])

# Dictionary is a group of key value pair
# Key should be unique in each dictionary
# Syntax: {<KEY> : <VALUE>}
# We can access the value by passing key in []

# for i in dictA:
#     print(i, dictA[i])

# for i,j in dictA.items():
#     print(i, j)

for i in dictA.values():
    print(i)

