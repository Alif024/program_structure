from random import randint
from os import system


def deposit(balance):
    money = int(input("จำนวนเงิน ===> "))
    balance += money
    print(f"ยอดเงินคงเหลือ : {balance:,} บาท")
    return balance


def withdrawMoney(balance):
    money = int(input("จำนวนเงิน ===> "))
    if money > balance:
        print("ยอดเงินมีไม่เพียงพอ")
        return balance
    else:
        balance -= money
        print(f"ยอดเงินคงเหลือ : {balance:,} บาท")
        return balance


def askBalance(balance):
    print(f"ยอดเงินทั้งหมดคือ {balance:,} บาท")


system('cls')
balance = randint(0, 100000)
print(f"ยอดเงินคงเหลือ : {balance:,} บาท")
while True:
    print("กรุณาเลือกเมนู")

    while True:
        try:
            choose = int(input("1:ฝาก, 2:ถอน, 3:ถามยอด, 0:ยกเลิก ===> "))
            if choose >= 0 and choose <= 3:
                break
            else:
                print('')
                print(" /!\ ใส่ตัวเลข 0-3 เท่านั้น /!\ ")
                print("กรุณาเลือกเมนู")
        except:
            print('')
            print(" /!\ ใส่ตัวเลข 0-3 เท่านั้น /!\ ")
            print("กรุณาเลือกเมนู")

    try:
        if choose == 1:
            balance = deposit(balance)
        elif choose == 2:
            balance = withdrawMoney(balance)
        elif choose == 3:
            askBalance(balance)
        elif choose == 0:
            YesNo = input("กด y เพื่อออกจากโปรแกรม >> ")
            if YesNo == "y":
                break
    except:
        print(" /!\ /!\ /!\ ERROR /!\ /!\ /!\ ")

    print('')

print("ขอบคุณที่ใช้บริการคะ")
