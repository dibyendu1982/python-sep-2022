arr = [11, 23, 36] #! It's a list not an array 

print(id(arr))

print(arr)
print(type(arr))

print(arr[0])
print(arr[1])

for element in arr:
    print(element * 2)

print("-"* 20, "List Operation", "-"* 20)
list = [5, 7, 1]
list.append(9)
print(list)
list.insert(1, 22)
print(list)
list.pop(1) # ~ Remove by position 
print(list)
list.remove(1) # ~ Remove by value
print(list)
list.extend([2,3,4])

print("-"* 20, "List Slicing ", "-"* 20)
print("list[1:]", list[1:])
print("list[1:3]", list[1:3])
print("list[2:5:2]", list[2:5:2])
print(list)
print("list[::-1]", list[::-1])
print("list[:-4:-1]", list[:-4:-1])
print(list)
print("list[::-2]", list[::-2])
print("list[:-6:-2]", list[:-6:-2]) # TODO : Need to check on the -2 on how this one works
