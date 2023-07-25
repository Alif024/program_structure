num = int(input("Please enter number of factorial : "))
result = 1
for i in range(0, num+1):
    if i == 0:
        pass
    else:
        result = result * i
print(f"Result of {num}! is {result}")