member = input("y, n :")
while True:
    if member == "y" or member == "n":
        break
    member = input("กรุณาป้อน y, n เท่านั้น")
ticketAdult = int(input())
ticketKid = int(input())
if ticketAdult + ticketKid >= 10 and ticketKid >= 1 and member == "y":
    discount = 0.5
elif ticketAdult + ticketKid >= 5 and ticketKid >= 1 and member == "y":
    discount = 0.3
elif ticketAdult + ticketKid < 5 and ticketKid >= 1 and member == "y":
    discount = 0.2
elif member == "y" and ticketKid == 0:
    discount = 0.1
else:
    discount = 0.05
print("{} {}".format(((ticketAdult*100*discount)+(ticketKid*50*discount)), ((ticketAdult*100)-(ticketAdult*100*discount))+((ticketKid*50)-(ticketKid*50*discount))))