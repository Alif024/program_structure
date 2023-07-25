count_div_5 = 0
while True:
    num = int(input("Enter number >> "))
    if num == 0:
        break
    elif num % 5 == 0:
        count_div_5 += 1
print(f"count Div 5 : {count_div_5}")