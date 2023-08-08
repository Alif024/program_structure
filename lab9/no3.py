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
    try:
        print("กรุณาเลือกเมนู")
        choose = int(input("1:ฝาก, 2:ถอน, 3:ถามยอด, 0:ยกเลิก ===> "))
        if choose == 1:
            balance = deposit(balance)
            input("ไปหน้าเมนูกด Enter")
        elif choose == 2:
            balance = withdrawMoney(balance)
            input("ไปหน้าเมนูกด Enter")
        elif choose == 3:
            askBalance(balance)
            input("ไปหน้าเมนูกด Enter")
        elif choose == 0:
            YesNo = input("กด y เพื่อออกจากโปรแกรม >> ")
            if YesNo == "y":
                break
        print('')
    except:
        print('')
        print("เลือก 0-3 เท่านั้น")
        pass

print("ขอบคุณที่ใช้บริการคะ")

