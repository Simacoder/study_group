#creates fibinnacous
n = 0
def fab(n):
    num1 = 0
    num2 = 1
    n = int(input("Enter the n term of the fab: "))
    next_number = num2
    count = 0
    while count <= n:
        print(next_number, end=" ")
        count += 1
        num1, num2 = num2, next_number
        next_number = num1 + num2
    print()
fab(n)
