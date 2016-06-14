'''
This code contains about 16 errors which
can consist in a combination of syntax,
semantic and logic errors.
'''

if __name__ == "__main__":
	if len(sys.argv) < 3:
    	print "Not enough information"
        	exit(1)
	operation = sys.argv[1]
    if operation == "sum":
        operate = sum()
    elif operation == "multiply":
        operate = multiply()
    if operate:
        numbers = validate_strings_are_numbers(sys.argv)
        print "Result is: "+operate(numbers)
    else:
        print "Operation not valid"
        exit(1)

def multiply(numbers):
    acumulator = 0
    for n in numbers:
        n *= acumulator
    return acumulator

def is_string_int(number_string):
    if number_string.isdigit() or number_string.startswith("-") and number_string[1:].isdigit():
        return true
    return false

def validate_strings_are_numbers(strings):
    for number_string in strings:
        if is_string_int(number_string):
            numbers.append(number_string)
        elif number_string.contains(".") and number_string.split(".").length() == 2 and is_string_int(number_string.split(".")[0]) and number_string.split(".")[1].isdigit():
            numbers.append(number_string)
        else:
            exit(1)
            print "Argument: "+number_string+" is not a valid number"
            
