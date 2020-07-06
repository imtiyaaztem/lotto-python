# Imtiyaaz Temoore Class 2

# this program is used for lottery, to determent the lotto numbers
# this function is used to see if the user older than 18
# if the user is young than 18 the program will not continue
# but if the user is older than 18 the program will run
current_year = 2020
year_of_birth = int(input('Enter Year Of Birth: '))
age = current_year - year_of_birth
mytext = 'You are %s years old.'
print(mytext % age)
if age < 18:
    print('You are not allowed to play the lotto as you are under age')
    exit()
else:
    print('Welcome To The Lottery.')

# this import a random number in a list
import random
def lotto():
    """
    >>> result = lotto()
    >>> all([1 <= values <= 50 for values in result])
    True
    """
    lotteryNumbers = []
    for i in range(0, 6):
        number = random.randint(1, 49)
        # this check if the number was already picked
        while number in lotteryNumbers:
            # THIS REPLACE THE NUMBER IF IT IS ALREADY BEEN PICKED IN A LIST
            number = random.randint(1, 49)
        lotteryNumbers.append(number)
    lotteryNumbers.sort()
    return lotteryNumbers
x=lotto()
print("Today lotto numbers")
print(x)
# this function allow user to enter there lotto numbers
userNumbers = []
for i in range(0, 6):
    number = int(input("please enter a number between 1 and 50:"))
    while number < 1 or number > 50:
        number = int(input("please enter a number between 1 and 50:"))

    userNumbers.append(number)

userNumbers.sort()

# this print your lotto numbers
print(">>> your lottery numbers:")
print(userNumbers)
# this function show how much lotto number u got corrrect
counter = 0
for number in userNumbers:
    if number in x:
        counter += 1

print("you have guessed " + str(counter) + " number(s) correctly")

# the if statement is being used to determent the prize u won
# if u get less than 1 you will not get a prize
if counter <= 1:
    print("YOU HAVE NO PRIZE")
# if u get 2 right there is a prize for u
elif counter == 2:
    print("your prize is:R20")
# if u get 3 right there is a prize for u
elif counter == 3:
    print("your prize is:R100,50")
# if u get 4 right there is a prize for u
elif counter == 4:
    print("your prize is:R2 384")
# if u get 5 right there is a prize for u
elif counter == 5:
    print("your prize is:R8 584")
# if you get all 6 numbers then u are the bonus winner
elif counter == 6:
    print("You are the bonus winner, Your prize is:R10 000 000")

import datetime

todays_date = datetime.date.today()

print(todays_date)

with open("lottoresult.txt", "w") as feedback:
    feedback.write(str("Todays lotto numbers") + '\n')
    feedback.write(str(x) + '\n')

    feedback.write(str("Your lotto numbers") + '\n')
    feedback.write(str(userNumbers) + '\n')

    feedback.write(str("Your numbers you got right:"))
    feedback.write(str(counter) + '\n')

    feedback.write(str("Date:"))
    feedback.write(str(todays_date) + '\n')



