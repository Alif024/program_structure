calorie = int(input("วันนี้คุณมีพลังงานทั้งหมด > "))
if calorie > 1800:
    time = 60
    print("คุณควรจะวิ่งมากกว่า {} นาที".format(time))
elif calorie > 1500 :
    time = ((calorie - 1500) / 10) + 15
    print("คุณควรจะวิ่งอย่างน้อย {} นาที".format(int(time)))
else:
    time = 15
    print("คุณควรจะวิ่ง {} นาที".format(time))