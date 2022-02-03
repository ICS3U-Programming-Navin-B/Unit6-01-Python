#!/usr/bin/env python3

# Created by: Navin Balekomebole
# Created on: Jan 27 2022
# This program generates 10 random numbers
# and calculates the average.
import constant
import random


def main():
    # declare variables
    list_of_int = []
    sum = 0
    # add numbers to array
    for counter in range(constant.MAX_NUM + 1):
        rand_num = random.randint(1, 101)
        list_of_int.append(rand_num)
        print("{} was added to the array at position {}"
              . format(rand_num, counter))
    # calc sum
    for counter in range(constant.MAX_NUM + 1):
        sum = sum + list_of_int[counter]
    # calc average
    average = sum / constant.MAX_NUM
    print("The average is {}". format(average))


if __name__ == "__main__":
    main()
