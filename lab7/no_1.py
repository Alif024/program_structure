num = list(input("กรุณาใส่ตัวเลขจำนวนเต็ม >> "))
num = [int(i) for i in num]
print(f'ตัวเลขที่มีค่ามากที่สุด : {max(num)}')
print(f'ผลบวกของเลขโดดทั้งหมด : {sum(num)}')