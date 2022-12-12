import math


def decimal_to_binary(value):
    return bin(value)[2:]

def decimal_to_octal(value):
    return oct(value)[2:]
    

def decimal_to_hexadecimal(value):
    return hex(value)[2:]

# def binary_to_octal():
#     print('4')
    

# def binary_to_decimal():
#     print('5')
    

# def binary_to_hexadecimal():
#     print('6')
    

# def octal_to_binary():
#     print('7')
    

# def octal_to_decimal():
#     print('8')
    

# def octal_to_hexadecimal():
#     print('9')
    

# def hexadecimal_to_binary():
#     print('10')
    

# def hexadecimal_to_octal():
#     print('11')
    

# def hexadecimal_to_decimal():
#     print('12')
    

def decimal_to_bcd(value):

    """
        reverse the digits and iterate through 
        all digits in rev and store each digit
        binary conversion in bits variable.
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

    """
        converts decimal to gray code
    """
    
    return value ^ (value >> 1)


def decimal_to_1s_complement(value):
    """
        converts decimal to 1's complement
    """

    number_of_bits = (int)(math.floor(math.log(value) / math.log(2))) + 1;

    return ((1 << number_of_bits) - 1) ^ value;


def decimal_to_2s_complement(value):
    """
        converts decimal to 2's complement
    """

    bits = decimal_to_binary(value)
    n = len(bits)
    i = n - 1
    while(i >= 0):
        if (bits[i] == '1'):
            break
        i -= 1
    if (i == -1):
        return int('1'+bits, 2)
    k = i - 1
    while(k >= 0):
        if (bits[k] == '1'):
            bits = list(bits)
            bits[k] = '0'
            bits = ''.join(bits)
        else:
            bits = list(bits)
            bits[k] = '1'
            bits = ''.join(bits)
            
        k -= 1
    return int(bits, 2)    
    