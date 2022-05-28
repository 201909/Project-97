import random
max_try = 5
max_num = 10

myList = list(range(1,max_num))


for i in range(1,max_try+1):
    choose = random.choice(myList)
    guess = int(input('Guess the number from {}   '.format(myList)))
    if (choose == guess):
        print('CONGRATULATION ! you guessed correctly after {} attempts'.format(i))
        break
    else:
        print('Wrong! Please try again!')
