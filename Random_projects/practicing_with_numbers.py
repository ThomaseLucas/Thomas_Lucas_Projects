import math

def main():
    nth_number = int(input("Please enter a number to display pi to: "))
    pi_to_nth(nth_number)
    return 0

def pi_to_nth(nth):

    formatted_num = "{:.{}f}".format(math.pi, nth)
    print(formatted_num)

if __name__ == "__main__":
    main()