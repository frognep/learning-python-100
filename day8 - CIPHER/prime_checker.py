#Write your code below this line 👇

def prime_checker(number):
    divisor_list = []
    for dividend in range(1, number + 1):
        divided = number % dividend
        if divided == 0:
            divisor_list.append(dividend)
    if len(divisor_list) > 2:
        print("It's not a prime number.")
    else:
        print("It's a prime number.")

#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)