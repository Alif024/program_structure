list = [["Olarik", 3.5], ["Kaveepoj", 3.9], ["Suwichai", 3.2]]
while True:
    state = input("Do you want add new student data (y,n)? ")
    if state == "y":
        name_GPA = []
        name = input("Please insert student name : ")
        GPA = float(input("Please insert student GPA : "))
        name_GPA.append(name)
        name_GPA.append(GPA)
        list.append(name_GPA)
    elif state == "n":
        break
    else:
        print("Enter : y, n only")
        pass
if len(list) != 0:
    print("=====================================")
    print("index\t\tname\t\tGPA")
    print("=====================================")
    for i in range(len(list)):
        if len(list[i][0]) > 7:
            print(f"{i+1}\t\t{list[i][0]}\t{list[i][1]}")
        else:
            print(f"{i+1}\t\t{list[i][0]}\t\t{list[i][1]}")
    print("=====================================")
    sum_GPA = 0
    for i in range(len(list)):
        sum_GPA += list[i][1]
    print(f"average\t\t\t\t{sum_GPA/len(list):.2f}")
    print("=====================================")