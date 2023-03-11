
# Lottery Game
import random
firstPrice = 10000
secondPrice = 3000
thirdprice = 1000

lottery = random.randint(10, 99)


guess = eval(input("Enter any two digits number: "))

lotterydigit1 = lottery // 10
lotterydigit2 = lottery % 10

guessdigit1 = guess // 10
guessdigit2 = guess % 10

if lottery == guess:
    print("You won, your price is $", firstPrice)
elif (lotterydigit1 == guessdigit2 and lotterydigit2 == guessdigit1):
    print("You won, your price is $", secondPrice)
elif (guessdigit1 == lotterydigit1 \
         or guessdigit1 == lotterydigit2 \
         or guessdigit2 == lotterydigit1 \
         or guessdigit2 == lotterydigit2):
    print("Match one digit: you win $", thirdprice, "the correct guess is ", lottery)
else:
    print("You lost! Try again, the correct guess is ", lottery)