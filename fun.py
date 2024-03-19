# search using function and for loop 

data = [1, 2, 3, 4, 5]
target = 5
item = int(input("enter your number: "))

def contains(data, target):
    if item in data:
        if item == target:
            print(f"the item {item} is found as the target is {target}")
            return True
        else:
            print(f"The item {item} is not found as the target is {target}")
    return False

contains(data, target)
