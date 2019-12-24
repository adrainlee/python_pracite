#!/usr/bin/env python3

import random

luck_num = random.randint(0,100)
print(luck_num)
guess_times = 0

while True:
    input_num = input("Please input a number: ")
    try:
        if input_num.isdigit:
            guess_num = int(input_num)
            if guess_num == luck_num:
                print("You got it")
                print("You guessed {} times".format(guess_times))
                break
            elif guess_num > luck_num:
                guess_times += 1
                print("Input number is bigger{}".format(guess_times))
            else:
                guess_times += 1
                print("Input number is smaller{}".format(guess_times))
    except:
        print("Value error")
        guess_times += 1
