lines = int(input("Enter number of lines : "))
if lines == 1:
    member = 1
else:
    member = lines + 2
nums = []
for j in range(lines):
    nums.append(2**j)
    coppy_nums = nums.copy()
    while len(coppy_nums) != member:
        coppy_nums.insert(0, "")
    text = ""
    for i in range(len(coppy_nums)):
        text += "{" + str(i) + ":<7} " 
    for i in range(len(coppy_nums)-2, -1, -1):
        text += "{" + str(i) + ":<7} "
    print(text.format(*coppy_nums))
print("-"*200)