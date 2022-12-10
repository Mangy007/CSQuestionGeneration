
def decimal_to_binary(value):
    return bin(value)[2:]

def decimal_to_octal(value):
    return oct(value)[2:]
    

def decimal_to_hexadecimal(value):
    return hex(value)[2:]

def binary_to_octal():
    print('4')
    

def binary_to_decimal():
    print('5')
    

def binary_to_hexadecimal():
    print('6')
    

def octal_to_binary():
    print('7')
    

def octal_to_decimal():
    print('8')
    

def octal_to_hexadecimal():
    print('9')
    

def hexadecimal_to_binary():
    print('10')
    

def hexadecimal_to_octal():
    print('11')
    

def hexadecimal_to_decimal():
    print('12')
    

def decimal_to_bcd(value):

    """
        reverse the digits and iterate through 
        all digits in rev and store each digit
        binary conversion in bits
    """
    
    if (value == 0) :
        print("0000")
        return
 
    rev = 0
 
    while (value > 0) :
        rev = rev * 10 + (value % 10)
        value = value // 10

    bits = ""

    while (rev > 0) :
        b = str(rev % 10)
        bits += "{0:04b}".format(int(b, 16)) + " "
        rev = rev // 10

    return bits

def decimal_to_gray_code(value):
    
    return value ^ (value >> 1)