import math

def main():
    binary = input_bin()
    print(calculation(binary))

def input_bin():
    return input("Enter your 8-digit binary number ")
    
def calculation(binary):
    total = 0
    length_of_number = len(binary)
    for i in range(length_of_number):
        digit = int(binary[i]) * 2 ** (length_of_number - 1)
        total += digit
        return total


main()