count = int(input())
price = float(input())
if count >= 6:
    if price-(count*12) < price-(count*0.05):
        print("{} {}".format(count*12 ,(price-(count*12))))
    else:
        print("{} {}".format(count*0.05, (price-(count*0.05))))
elif count >= 2:
    print("{} {}".format(count*10 ,(price-(count*10))))
else:
    print("{} {}".format(count*5 ,(price-(count*5))))