nums = []
count = int(input("Enter number of times : "))
for i in range(count):
    num = int(input(f"Enter number {i+1} : "))
    nums.append(num)
sum = 0
for i in nums:
    sum += i
print(f"แสดงตัวแปรลิส nums : {nums}")
print(f"ค่าเฉลี่ยของสมาชิกในลิสต์ nums : {sum/len(nums):.2f}")
max = nums[0]
for i in nums:
    if i > max:
        max = i
min = nums[0]
for i in nums:
    if i < min:
        min = i
print(f"ค่าที่มากที่สุดคือ {max} และค่าที่น้อยที่สุดคือ {min}")
'''nums_2 = nums.copy()
nums_2.remove(max)
nums_2.remove(min)
max = nums_2[0]
for i in nums_2:
    if i > max:
        max = i
min = nums_2[0]
for i in nums_2:
    if i < min:
        min = i
print(f"ค่ามากที่สุดอันดับที่ 2 คือ {max} และค่าน้อยที่สุดอันดับที่ 2 คือ {min}")'''
nums.sort()
print(f"ค่ามากที่สุดอันดับที่ 2 คือ {nums[-2]} และค่าน้อยที่สุดอันดับที่ 2 คือ {nums[1]}")
odd_nums = []
for i in nums:
    if i%2 != 0: 
        odd_nums.append(i)
print(f"จำนวนเลขคี่คือ {len(odd_nums)} และในลิสต์นี้คือ {odd_nums}")