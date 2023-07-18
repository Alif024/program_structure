list_score = [2, 4, 8, 1, 9, 3]
sum_score = 0
for i in list_score:
    sum_score += i
max_score = list_score[0]
for i in list_score:
    if i > max_score:
        max_score = i
min_score = list_score[0]
for i in list_score:
    if i < min_score:
        min_score = i
print("• คำตอบ")
print(f"• sum_score = {sum_score}")
print(f"• max_score = {max_score}")
print(f"• min_score = {min_score}")