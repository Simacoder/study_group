# list comprehesion 

n = int(input("enter your n: "))
squares = []
for k in range(1, n+1):
    squares.append(k*k)
print(squares)

print("list comprehesion")

squares2 = [k*k for k in range(1, n+1)]
print(squares2)
