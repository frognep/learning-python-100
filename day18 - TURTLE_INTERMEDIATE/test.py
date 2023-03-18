from math import sqrt

while True:
    num=int(input("Please input a number:"))
    if num == 0:
        print("exiting..")
        break

    elif num < 0:
        print("Invalid number")
    else:
       print(sqrt(num))