total_weight = 0
for count in range(1, 7):
    weight = float(input(f"น้ำหนักของคนที่ {count} >> "))
    if total_weight + weight > 450:
        while total_weight + weight > 450:
            print("น้ำหนักเกินกำหนด")
            weight = float(input(f"น้ำหนักของคนที่ {count} >> "))
        total_weight += weight
    else:
        total_weight += weight
print(f"น้ำหนักรวม : {total_weight}")