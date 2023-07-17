import os
os.system('cls')
def home():
    print("="*20, " BMI Calculator ", "="*17)
    print("1. Calculation")
    print("2. Show data")
    print("3. Exit program")
    print("="*55)
home()
mode = input("Please choose 1-3:")
os.system('cls')
list_data = []
while True:
    match mode:
        case "1":
            mode1 = True
            try:
                while mode1:
                    status = []
                    os.system('cls')
                    print("="*20, " Insert Data ", "="*20)
                    name = input("Please input your name : ")
                    height = float(input("Please input Height (cm.) : "))
                    weight = float(input("Please input Weight (kg.) : "))
                    BMI = weight/(height/100)**2
                    if BMI >= 30:
                        detail = "Obesity (2 degree)"
                    elif BMI >= 25:
                        detail = "Obesity (1 degree)"
                    elif BMI >= 23:
                        detail = "Overweight"
                    elif BMI >= 18.5:
                        detail = "Normal"
                    else:
                        detail = "Low body weight"
                    status.append(name)
                    status.append(height)
                    status.append(BMI)
                    status.append(weight)
                    status.append(detail)
                    list_data.append(status)
                    print(f"\nYour BMI is {BMI:.2f} {detail}")
                    print("\n\nทำอีกครั้งกด: y\t\t\t\tกลับหน้าหลัก: [n]")
                    state1 = input("")
                    if state1 == 'y':
                        pass
                    else:
                        mode1 = False
            except KeyboardInterrupt:
                mode1 = False
        case "2":
            mode2 = True
            while mode2:
                os.system('cls')
                print("="*20, " BMI Detail ", "="*21)
                print("No.\tHeight\t\tWeight\t\tBMI\tDetail")
                print("*"*55)
                for i in range(len(list_data)):
                    print(f"{i+1}\t{list_data[i][1]:.2f}\t\t{list_data[i][2]:.2f}\t\t{list_data[i][3]:.2f}\t{list_data[i][4]}")
                print("="*55)
                print("กลับหน้าหลัก Press Enter")
                input("")
                mode2 = False
        case "3":
            os.system('cls')
            confirm = input("Do you want to exit BMI Calculator (y/[n])? ")
            if confirm == "y":
                print("Thank you")
                break
            else:
                pass
        case _:
            pass
    os.system('cls')
    home()
    mode = input("Please choose 1-3:")  