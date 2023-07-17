line = int(input("Enter number of lines : "))
time_tab = line + 1
for j in range(1, line+1):
    list_behide_num = []
    behide_num = ''
    text_num = ''
    for i in range(j):
        if i == line-1:
            num = 2**i
            list_behide_num.append(num)
            text_num += str(num) + '\t '
        else:
            num = 2**i
            list_behide_num.append(num)
            text_num += str(num) + '\t '
    for k in list_behide_num[-1::-1]:
        if k < list_behide_num[-1]:
            text_num += str(k) + '\t '
    time_tab = time_tab-1
    print('\t'*(time_tab),text_num)