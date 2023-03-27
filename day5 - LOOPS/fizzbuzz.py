#Write your code below this row 👇

#every number divisible by 3, print "Fizz"
#every number divisible by 5, print "Buzz"
#every number dibisible by both, print "FizzBuzz"

for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)