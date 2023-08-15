from os import system

def menu():
    print("""กด 1 หาค่าแรงดันไฟฟ้า
กด 2 หาค่ากระแสไฟฟ้า
กด 3 หาค่าความต้านทาน
กด 4 ออกจากโปรแกรม""")

def voltage(I, R):
    return I*R


def resistance(I, V):
    return V/I


def electricCurrent(V, R):
    return V/R


while True:
    system('cls')
    menu()
    while True:
        try:
            choose = int(input("เลือกการทำงานของโปรแกรม >> "))
            if choose >= 1 and choose <= 4:
                break
            else:
                system('cls')
                menu()
                print(" /!\ ใส่ตัวเลข 1-4 เท่านั้น /!\ ")
        except:
            system('cls')
            menu()
            print(" /!\ ใส่ตัวเลข 1-4 เท่านั้น /!\ ")
    if choose == 1:
        try:
            system('cls')
            print("หาค่าแรงดันไฟฟ้า")
            I = float(input("Electric Current >> "))
            R = float(input("Resistance >> "))
            print(f'Voltage = {voltage(I, R):,.3f} V')
            input("กด Enter")
        except:
            input(" /!\ /!\ /!\ ERROR /!\ /!\ /!\ \nกด Enter")
    elif choose == 2:
        try:
            system('cls')
            print("หาค่ากระแสไฟฟ้า")
            V = float(input("Voltage >> "))
            R = float(input("Resistance >> "))
            print(f'Electric Current = {electricCurrent(V, R):,.3f} A')
            input("กด Enter")
        except:
            input(" /!\ /!\ /!\ ERROR /!\ /!\ /!\ \nกด Enter")
    elif choose == 3:
        try:
            system('cls')
            print("หาค่าความต้านทาน")
            I = float(input("Electric Current >> "))
            V = float(input("Voltage >> "))
            print(f'Resistance = {resistance(I, V):,.3f} Ω')
            input("กด Enter")
        except:
            input(" /!\ /!\ /!\ ERROR /!\ /!\ /!\ \nกด Enter")
    elif choose == 4:
        system('cls')
        print("ต้องการออกจากโปรแกรมหรือไม่")
        print("กด y คือ ออกจากโปรแกรม, กด n คือกลับไปที่เมนู")
        YesNo = input(">> ")
        while True:
            if YesNo == 'y' or YesNo == 'n':
                break
            else:
                system('cls')
                print("ต้องการออกจากโปรแกรมหรือไม่")
                print("กด y ออกจากโปรแกรม, กด n กลับไปที่เมนู")
                print(" /!\ ใส่ y หรือ n เท่านั้น /!\ ")
                YesNo = input(">> ")
        if YesNo == 'y':
            print("Thank you")
            break
