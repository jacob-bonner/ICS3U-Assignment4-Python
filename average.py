#!/usr/bin/env python3

# Created by: Jacob Bonner
# Created on: September 2019
# This program finds the average of three numbers between 1 and 100


def main():
    # This program finds the average of three numbers between 1 and 100

    # Input
    first_number = input("Enter your first number between 1-100: ")
    second_number = input("Enter your second number between 1-100: ")
    third_number = input("Enter your third number between 1-100: ")
    print("")

    # Process
    try:
        first_number = int(first_number)
        second_number = int(second_number)
        third_number = int(third_number)

        if first_number <= 100 and first_number >= 1:
            if second_number <= 100 and second_number >= 1:
                if third_number <= 100 and third_number >= 1:
                    average = (first_number + second_number + third_number)/3
                    print("The average of your three number is", average)
                else:
                    print("Error: unable to calculate average")
            else:
                print("Error: unable to calculate average")
        else:
            print("Error: unable to calculate average")
    except Exception:
        print("Error: unable to calculate average")


if __name__ == "__main__":
    main()
