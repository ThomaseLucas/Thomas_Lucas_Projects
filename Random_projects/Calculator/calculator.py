import time
import os

def main():

    while True:
        choice = input("Would you like to use the calculator?\n1. Yes\n2. No \n")
        try:
            choice = int(choice)
            if choice == 1:
                print("Calculator loading...")
                time.sleep(3)
                clear_terminal()
                calculator_setup()
                while True:
                    clear_terminal()
                    calculator_setup()
                    first_number = float(input("Please enter your first number: "))
                    try: 
                        
                            clear_terminal()
                            calculator_setup()
                            operation_choice = input("Please enter your operator x, /, +, - : ")
                            
                            if operation_choice in ['+', '-', '/', '*']:
                               clear_terminal()
                               calculator_setup()
                               second_number = float(input("Please enter the next number: "))
                               calculation = calculate(first_number, operation_choice, second_number)
                               clear_terminal()
                               calculator_setup()
                               print(f"Your total is: {calculation}")
                               break     
                            else: 
                                print("Error. Enter a valid operator.")
                                time.sleep(2)

                    except ValueError:
                        print("Error. Please enter a valid number")
            
            elif choice == 2:
                print("Exiting the program...")
                time.sleep(3)
                break

            else:
                print("Invalid number, please enter one or two.")

        except ValueError:
            print("Invalid input. Please enter a number.")    

def calculate(num1, operator, num2):

    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 == 0:
            return "Error. Division by 0"
        else:
            return num1 / num2
    else:
        return "Invalid operator. Enter valid operator."

def calculator_setup():
    print("1        2       3     +\n\n4        5       6     -\n\n7        8       9     *\n\n         0             / ")
    return None   

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')


main()
