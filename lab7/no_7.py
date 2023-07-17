def fac(num):
    if num >= 0:
        fac = 1
        for i in range(num, 0, -1):
            fac = fac * i
    else:
        fac = "Undefined"
    return fac
num = int(input("Please enter number of factorial : "))
print(f"Result of {num}! is {fac(num)}.")