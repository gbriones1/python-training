def to_decimal(string):
    if string.startswith('0b'):
        string = string[2:]
    if string and set(string) <= set('01'):
        return int(string, 2)
    return "Input is not a binary: "+string

def to_binary(string):
    if string.isdigit():
        return bin(int(string))
    return "Input is not a decimal: "+string

if __name__ == "__main__":
    string = raw_input("Enter a binary: ")
    print "Converting to decimal..."
    print to_decimal(string)
    string = raw_input("Enter a decimal: ")
    print "Converting to binary..."
    print to_binary(string)