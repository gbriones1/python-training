def to_decimal(string):
    pass

def to_binary(string):
    pass

if __name__ == "__main__":
    string = raw_input("Enter a binary: ")
    print "Converting to decimal..."
    print to_decimal(string)
    string = raw_input("Enter a decimal: ")
    print "Converting to binary..."
    print to_binary(string)