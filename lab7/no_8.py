num_list = []
for i in range(5):
    num = float(input(f"Enter number => {i+1} = "))
    num_list.append(num)
print("========== Result ==========")
print(f'Total = {sum(num_list):.2f}')
print(f'Average = {sum(num_list)/len(num_list):.2f}')