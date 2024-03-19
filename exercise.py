# try an exercise

def is_multiple(m,n):
    # check if is n a factor of n, m
    try:
        i = int(input("Enter your factor as i: "))
        #n = m * i
        if m%n == 0:
            print(f"yes, {i} is a factor of n,m")
        else:
            print(f"No, {i} is not a factor of n,m")
    except Exception as e:
        print("Error", e)
    return

is_multiple(6,3)