num = int(input("Please enter number of factorial : "))
while True:
    if num < 10 and num > 0:
        result = 1
        for i in range(0, num+1):
            if i == 0:
                pass
            else:
                result *= i
        print(f"Result of {num}! is {result:,}")
        break
    else:
        print("ใส่แค่ 1-9")
        num = int(input("Please enter number of factorial : "))