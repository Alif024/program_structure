count_user = int(input("จำนวนนักศึกษา : "))
sum_score = 0
for i in range(count_user):
    score = float(input("Score : "))
    sum_score += score
print(f"Sum = {sum_score} Average = {sum_score/count_user:.2f}")