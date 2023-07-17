import random
random_num = random.randint(1,10)
print("โปรแกรมทายตัวเลข 1-10")
num = int(input("ตัวเลขที่คนทายคือ >> "))
while random_num != num:
    if num > random_num:
        print("ตัวเลขที่คุณทายมีค่ามากไป")
        num = int(input("ตัวเลขที่คนทายคือ >> "))
    elif num < random_num:
        print("ตัวเลขที่คุณทายมีค่าน้อยไป")
        num = int(input("ตัวเลขที่คนทายคือ >> "))
    else:
        break
print(f"คุณทายถูกต้อง คำตอบคือ {random_num}")