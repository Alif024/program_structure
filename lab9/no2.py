def rectangular(width, length):
    return width*length

def square(sideLength):
    return sideLength*sideLength

def circle(radius):
    return (22*radius**2)/7

choose = input("เลือกสูตรการหาพื้นที่ >> ")
print("""กด 1 คำนวณหาพื้นที่สี่เหลี่ยมจัตุรัส
      กด 2 คำนวณหาพื้นที่สี่เหลี่ยมพื้นผ้า
      กด 3 คำนวณหาพื้นที่วงกลม
      กด 4 คำนวณหาพื้นที่สามเหลี่ยมด้านเท่า
      กด 5 ออกจากโปรแกรมและการถามว่าต้องการออกจากโปรแกรมหรือไม่ ถ้ากด y คือ ออกจากโปรแกรม ถ้ากด n คือกลับไปที่เมนู
""")
if choose == 1:
    sideLength = int(input("ใส่ความยาวด้าน >> "))
    print(f"{square(sideLength)}")
elif choose == 2:
    width = int(input("ใส่ความกว้าง >> "))
    length = int(input("ใส้ความยาว >> "))
    print(f"{rectangular(width, length)}")
elif choose == 3:
    radius = int(input("ใส้ความยาวรัศมี >> "))
    print(f"{circle(radius)}")