# ใส่เงินทั้งหมดที่จะให้ไปคำนวณเป็นธนบัตรกับเหรียญ
money = float(input("Enter money:"))

# ใส่ประเภทของเหรียญกับธนบัตรเก็บไว้ในตัวแปรประเภท List
type_money = [100, 50, 20, 10, 5, 2, 1, 0.0165, 0.0082, 0.0033, 0.0016, 0.00033]

print("เงินทั้งหมด : {} ดอลลาร์".format(money))

# ใช้ For loop เข้าเงื่อนไขตรวจสอบจำนวนเหรียญกับธนบัตร
for i in type_money:
    if money >= 1:
        if money // i != 0:
            print("แบงค์ {} ดอลลาร์ = {} ใบ".format(i, int(money//i)))
        money = money % i 
    else:
        if money // i != 0:
            print("เหรียญ {:.0f} เซนต์ = {} เหรียญ".format(i*3030.30303, int(money//i)))
        money = money % i

print("เหลือเศษ {} ดอลลาร์".format(money))