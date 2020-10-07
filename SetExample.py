# listB = [1,2,3]

# tupleA = (1,2,3,4,5)

# setA = {'test', 1, 2, 3, 4}

# Set? : It is used to remove duplicate values from collection and it's and unordered collection

# setA = {1,2,3,4,5,6,2,2,2,2,2,2,3,3,3,3,3,3,3,3,3,3,4,4,4,4,4,4,5,5,5,5,5,6,6,6,6,7,7,7}

# listA = [1,2,2,2,2,2,2,3,3,3,3,3,3,4,5,6,7,8,8,8]
# listB = []
# for i in listA:
#     if i not in listB:
#         listB.append(i)
# print(listB)

# listA = [1,2,2,2,2,2,2,3,3,3,3,3,3,4,5,6,7,8,8,8]

# setA = set(listA)

# print(setA)

##################

setA = {1,2,3,10}

print("I am doing something")
# setA.add(4)

# setA.update([10,20,30,40,50])
# setA.update((10,20,30,40,50))

# setA.discard(100) # it will not throw error if key doesn't exist
try:
    setA.remove(100) # it will throw error if key doesn't exist    
except Exception as e:
    print("Error")

print("I have removed something")

print(setA)

print("End")


# setA = {1,2,3}
# setB = {3,4,5}
# setC = {3,4,10}
## intersection (To find the common elements from two sets)

# print(setA & setB)
# print(setA.intersection(setB))

# setA.intersection_update(setB, setC) # {3,4} & {1,2,3} => {3}

# print(setA)

## Union (Used to merge two sets)

# print(setA | setB)
# print(setA.union(setB))


# setA = {50,55,60,75}
# setB = {75,25,58,55}
# setC = {75,85,55,95,60}

# setA.intersection_update(setB, setC) 
