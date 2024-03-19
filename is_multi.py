# ritng a function 

def is_multiple(n, m):
    
    try:
        i = int(input("enter the i value: "))
        n = m*i
        if n % m == 0:
            print(f"yes, the {i} is the factor of n and m")
        else:
            print(f"No, the {i} is not the factor of n and m")

    except Exception as e:
        print("Error;", e)
    return 
is_multiple(15,3)



