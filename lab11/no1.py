from random import randint


def random_num():
    rdNum = randint(0, 1000000)
    print(f"{rdNum:,}")
    split_num = list(str(rdNum))
    return [int(i) for i in split_num]


def even_num(listNum):
    return [even_num for even_num in listNum if even_num % 2 == 0]


def odd_num(listNum):
    return [odd_num for odd_num in listNum if odd_num % 2 != 0]


listNum = random_num()
print(f"sum = {sum(listNum)}")
print(f"{len(even_num(listNum))} ตัว {even_num(listNum)}")
print(f"{len(odd_num(listNum))} ตัว {odd_num(listNum)}")
