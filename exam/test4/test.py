data = {}
try:
    while True:
        print("""เลือกการทำงานของโปรแกรม
    1 : ใส่ข้อมูลพนักงาน
    2 : แสดงชื่อพนักงานทั้งหมด
    3 : แสดงข้อมูลของพนักงาน
""")
        id = int(input("Enter ID >> "))
        name = input("Enter name >> ")
        summit = int(input("Enter summit >> "))
        if summit > 50000:
            bonus = summit + summit*30/100
        else:
            bonus = summit + summit*10/100
        if id == "":
            break
        data[id] = {"name": f"{name}", "summit": summit, "bonus": bonus}
except :
    pass
    print(data)