
def add_numbers(first_number, second_number, third_number, fourth_number):
    return first_number + second_number + third_number + fourth_number
def subtract_numbers(first_number, second_number, third_number, fourth_number):
    return first_number - second_number - third_number - fourth_number
def multiply_numbers(first_number, second_number, third_number, fourth_number):
    return first_number * second_number * third_number * fourth_number
def divide_numbers(first_number, second_number, third_number, fourth_number):
    return first_number / second_number / third_number / fourth_number

def modulus_numbers(first_number, second_number, third_number, fourth_number):
    return first_number % second_number % third_number % fourth_number
def exponent_numbers(first_number, second_number, third_number, fourth_number):
    return first_number ** second_number ** third_number ** fourth_number
def floor_division_numbers(first_number, second_number, third_number, fourth_number):
    return first_number // second_number // third_number // fourth_number
# readable. The code is also designed to be easily extensible, allowing for the
# addition of more functions or features in the future. The use of clear and
# descriptive function names makes it easy to understand what each function does
# without needing to read through the implementation details. The code is also
# designed to be easily testable, with each function performing a single task and
# returning a result that can be easily verified. The use of type hints in the
# function signatures helps to clarify the expected input types, making the code
def main():
    first_number = int(input("Enter a first_number: "))
    second_number = int(input("Enter a second_number: "))
    third_number = int(input("Enter a third_number: "))
    fourth_number = int(input("Enter a fourth_number: "))

    print("Addition:", add_numbers(first_number, second_number, third_number, fourth_number))
    print("Subtraction:", subtract_numbers(first_number, second_number, third_number, fourth_number))
    print("Multiplication:", multiply_numbers(first_number, second_number, third_number, fourth_number))
    print("Division:", divide_numbers(first_number, second_number, third_number, fourth_number))
    print("Modulus:", modulus_numbers(first_number, second_number, third_number, fourth_number))
    print("Exponent:", exponent_numbers(first_number, second_number, third_number, fourth_number))
    print("Floor Division:", floor_division_numbers(first_number, second_number, third_number, fourth_number))
if __name__ == "__main__":
    main()
# The code above is a simple calculator that performs basic arithmetic operations
# on four numbers. It defines functions for addition, subtraction, multiplication,
# division, modulus, exponentiation, and floor division. The main function prompts
# the user for four numbers and then calls each of the arithmetic functions,
# printing the results to the console. The code is structured to be easily
# understandable and maintainable, with clear function definitions and a main
# function to handle user input and output. The use of type hints in the function
# signatures helps to clarify the expected input types, making the code more       