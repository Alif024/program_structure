data = {}
while True:
    print("""การทำงานของโปรแกรม
    1 : ใส่ข้อมูลพนักงาน
    2 : แสดงชื่อพนักงานทั้งหมด
    3 : แสดงข้อมูลของพนักงาน
    4 : ออกจากโปรแกรม
""")    
    mode = input("เลือกโหมด >> ")
    match mode:
        case "1":
            while True:
                id = input("Enter ID >> ")
                name = input("Enter name >> ")
                summit = int(input("Enter summit >> "))
                if summit > 50000:
                    bonus = summit + summit*30/100
                else:
                    bonus = summit + summit*10/100
                data[id] = {"name": name, "summit": summit, "bonus": bonus}
                mode1 = input("again? y, [n] ")
                if mode1 == 'y':
                    pass
                else:
                    break
        case "2":
            for i in data.keys():
                name_show = data[i].get('name')
                print(f"{i} : {name_show}")
                input("***Press enter***")
        case "4":
                break