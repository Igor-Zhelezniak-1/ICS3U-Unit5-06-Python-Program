#!/usr/bin/env python3

# Created by: Igor
# Created on: Nov 2021
# this program rounds numbers

from decimal import Decimal


def rounder(number, number_of_decimal_places):
    # this function rounds number

    # process
    answer = (number * (10.0 ** number_of_decimal_places)) + 0.5
    answer = int(answer)
    answer = answer / (10 ** number_of_decimal_places)

    return answer


def main():
    # this is main function

    # input
    integer1 = input("Enter the number you want to round: ")
    integer2 = input("Enter how many decimal places you want round by: ")

    try:
        number = float(integer1)
        number_of_decimal_places = int(integer2)

        if number_of_decimal_places < 0:
            print("Invalid input")
        else:
            answer = rounder(number, number_of_decimal_places)
            print("\nThe rounded number is {0}".format(answer))
    except Exception:
        print("\nInvalid input")

    print("\nDone.")


if __name__ == "__main__":
    main()
