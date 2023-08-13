from os import system


def rectangular(width, length):
    return width*length


def square(sideLength):
    return sideLength*sideLength


def circle(radius):
    return (22*radius**2)/7


def equilateralTriangle(sideLength):
    return ((3**(1/2))/4)*sideLength**2  # √3/4 × (side)2


def choose1Task():
    try:
        print("คำนวณหาพื้นที่สี่เหลี่ยมจัตุรัส")
        sideLength = int(input("ใส่ความยาวด้าน >> "))
        print(f"พื้นที่สี่เหลี่ยมจัตุรัส = {square(sideLength)}")
        input("กด Enter")
    except:
        input(" /!\ /!\ /!\ ERROR /!\ /!\ /!\ \nกด Enter")


def choose2Task():
    try:
        print("คำนวณหาพื้นที่สี่เหลี่ยมพื้นผ้า")
        width = int(input("ใส่ความกว้าง >> "))
        length = int(input("ใส้ความยาว >> "))
        print(f"พื้นที่สี่เหลี่ยมพื้นผ้า = {rectangular(width, length)}")
        input("กด Enter")
    except:
        input(" /!\ /!\ /!\ ERROR /!\ /!\ /!\ \nกด Enter")


def choose3Task():
    try:
        print("คำนวณหาพื้นที่วงกลม")
        radius = int(input("ใส้ความยาวรัศมี >> "))
        print(f"พื้นที่วงกลม = {circle(radius)}")
        input("กด Enter")
    except:
        input(" /!\ /!\ /!\ ERROR /!\ /!\ /!\ \nกด Enter")


def choose4Task():
    try:
        print("คำนวณหาพื้นที่สามเหลี่ยมด้านเท่า")
        sideLength = int(input("ใส่ความยาวด้าน >> "))
        print(f"พื้นที่สามเหลี่ยมด้านเท่า = {equilateralTriangle(sideLength)}")
        input("กด Enter")
    except:
        input(" /!\ /!\ /!\ ERROR /!\ /!\ /!\ \nกด Enter")


while True:
    system('cls')
    print("""กด 1 คำนวณหาพื้นที่สี่เหลี่ยมจัตุรัส
กด 2 คำนวณหาพื้นที่สี่เหลี่ยมพื้นผ้า
กด 3 คำนวณหาพื้นที่วงกลม
กด 4 คำนวณหาพื้นที่สามเหลี่ยมด้านเท่า
กด 5 ออกจากโปรแกรม
""")
    while True:
        try:
            choose = int(input("เลือกการทำงานของโปรแกรม >> "))
            if choose >= 1 and choose <= 5:
                break
            else:
                system('cls')
                print("""กด 1 คำนวณหาพื้นที่สี่เหลี่ยมจัตุรัส
กด 2 คำนวณหาพื้นที่สี่เหลี่ยมพื้นผ้า
กด 3 คำนวณหาพื้นที่วงกลม
กด 4 คำนวณหาพื้นที่สามเหลี่ยมด้านเท่า
กด 5 ออกจากโปรแกรม
""")
                print(" /!\ ใส่ตัวเลข 1-5 เท่านั้น /!\ ")
        except:
            system('cls')
            print("""กด 1 คำนวณหาพื้นที่สี่เหลี่ยมจัตุรัส
กด 2 คำนวณหาพื้นที่สี่เหลี่ยมพื้นผ้า
กด 3 คำนวณหาพื้นที่วงกลม
กด 4 คำนวณหาพื้นที่สามเหลี่ยมด้านเท่า
กด 5 ออกจากโปรแกรม
""")
            print(" /!\ ใส่ตัวเลข 1-5 เท่านั้น /!\ ")
    system('cls')
    if choose == 1:
        choose1Task()
    elif choose == 2:
        choose2Task()
    elif choose == 3:
        choose3Task()
    elif choose == 4:
        choose4Task()
    elif choose == 5:
        print("ต้องการออกจากโปรแกรมหรือไม่")
        print(f"{'กด y ตกลง'} {'กด n ยกเลิก':>20}")
        confirm_exit = input(">> ")
        while True:
            if confirm_exit == 'y' or confirm_exit == 'n':
                break
            else:
                system('cls')
                print("ต้องการออกจากโปรแกรมหรือไม่")
                print(f"{'กด y ตกลง'} {'กด n ยกเลิก':>20}")
                confirm_exit = input("ใส่ y หรือ n เท่านั้น >> ")
        if confirm_exit == 'y':
            print("thank you")
            break
    else:
        print()
