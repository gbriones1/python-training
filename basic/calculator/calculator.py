import sys

def multiply(numbers):
    acumulator = 1
    for n in numbers:
        acumulator *= n
    return acumulator
      
def is_string_int(number_string):
    if number_string.isdigit() or number_string.startswith("-") and number_string[1:].isdigit():
        return True
    return False
    
def validate_strings_are_numbers(strings):
    numbers = []
    for number_string in strings:
        if is_string_int(number_string):
            numbers.append(int(number_string))
        elif "." in number_string and len(number_string.split(".")) == 2 and is_string_int(number_string.split(".")[0]) and number_string.split(".")[1].isdigit():
            numbers.append(float(number_string))
        else:
            print "Argument: "+number_string+" is not a valid number"
            exit(1)
    return numbers
    
if __name__ == "__main__":
    if len(sys.argv) < 3:
        print "Not enough information"
        exit(1)
    operation = sys.argv[1]
    operate = None
    if operation == "sum":
        operate = sum
    elif operation == "multiply":
        operate = multiply
    if operate:
        numbers = validate_strings_are_numbers(sys.argv[2:])
        print "Result is: "+ str(operate(numbers))
    else:
        print "Operation not valid"
        exit(1)
    