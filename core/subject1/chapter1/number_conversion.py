from random import randint, shuffle
import core.subject1.chapter1.solver.number_conversion_solver as solver

question_map = {
    1: "Decimal to Binary",
    2: "Decimal to Octal",
    3: "Decimal to Hexadecimal",
    4: "Binary to Octal",
    5: "Binary to Decimal",
    6: "Binary to Hexadecimal",
    7: "Octal to Binary",
    8: "Octal to Decimal",
    9: "Octal to Hexadecimal",
    10: "Hexadecimal to Binary",
    11: "Hexadecimal to Octal",
    12: "Hexadecimal to Decimal",
    13: "Decimal to BCD",
    14: "Decimal to Gray Code",
    15: "1's Complement",
    16: "2's Complement"
}

def print_options(options):
    """
        Function to print generated options
    """
    for i,val in enumerate(options):
        print(chr(97+i), val)

def number_conversion(question_type, value, option_values):
    if question_type == 1:
        print("(",value,")base10  -->  (?)base2")
        value = solver.decimal_to_binary(value)
        options = [solver.decimal_to_binary(val) for val in option_values]
        options.append(value)
        shuffle(options)
        print_options(options)
        print("Correct answer: ",value)
    elif question_type == 2:
        print("(",value,")base10  -->  (?)base8")
        value = solver.decimal_to_octal(value)
        options = [solver.decimal_to_octal(val) for val in option_values]
        options.append(value)
        shuffle(options)
        print_options(options)
        print("Correct answer: ",value)
    elif question_type == 3:
        print("(",value,")base10  -->  (?)base16")
        value = solver.decimal_to_hexadecimal(value)
        options = [solver.decimal_to_hexadecimal(val) for val in option_values]
        options.append(value)
        shuffle(options)
        print_options(options)
        print("Correct answer: ",value)
    elif question_type == 4:
        converted_value = solver.decimal_to_binary(value)
        print("(",converted_value,")base2  -->  (?)base8")
        value = solver.decimal_to_octal(value)
        options = [solver.decimal_to_octal(val) for val in option_values]
        options.append(value)
        shuffle(options)
        print_options(options)
        print("Correct answer: ",value)
    elif question_type == 5:
        # solver.binary_to_decimal() 
        converted_value = solver.decimal_to_binary(value)
        print("(",converted_value,")base2  -->  (?)base10")
        option_values.append(value)
        shuffle(option_values)
        print_options(option_values)
        print("Correct answer: ",value)
    elif question_type == 6:
        # solver.binary_to_hexadecimal()
        converted_value = solver.decimal_to_binary(value)
        print("(",converted_value,")base2  -->  (?)base8")
        value = solver.decimal_to_hexadecimal(value)
        options = [solver.decimal_to_hexadecimal(val) for val in option_values]
        options.append(value)
        shuffle(options)
        print_options(options)
        print("Correct answer: ",value)
    elif question_type == 7:
        # solver.octal_to_binary() 
        converted_value = solver.decimal_to_octal(value)
        print("(",converted_value,")base8  -->  (?)base2")
        value = solver.decimal_to_binary(value)
        options = [solver.decimal_to_binary(val) for val in option_values]
        options.append(value)
        shuffle(options)
        print_options(options)
        print("Correct answer: ",value)
    elif question_type == 8:
        # solver.octal_to_decimal()
        converted_value = solver.decimal_to_octal(value)
        print("(",converted_value,")base8  -->  (?)base10")
        option_values.append(value)
        shuffle(option_values)
        print_options(option_values)
        print("Correct answer: ",value)
    elif question_type == 9:
        # solver.octal_to_hexadecimal() 
        converted_value = solver.decimal_to_octal(value)
        print("(",converted_value,")base8  -->  (?)base16")
        value = solver.decimal_to_hexadecimal(value)
        options = [solver.decimal_to_hexadecimal(val) for val in option_values]
        options.append(value)
        shuffle(options)
        print_options(options)
        print("Correct answer: ",value)
    elif question_type == 10:
        # solver.hexadecimal_to_binary()
        converted_value = solver.decimal_to_hexadecimal(value)
        print("(",converted_value,")base16  -->  (?)base2")
        value = solver.decimal_to_binary(value)
        options = [solver.decimal_to_binary(val) for val in option_values]
        options.append(value)
        shuffle(options)
        print_options(options)
        print("Correct answer: ",value)
    elif question_type == 11:
        # solver.hexadecimal_to_octal() 
        converted_value = solver.decimal_to_hexadecimal(value)
        print("(",converted_value,")base16  -->  (?)base8")
        value = solver.decimal_to_octal(value)
        options = [solver.decimal_to_octal(val) for val in option_values]
        options.append(value)
        shuffle(options)
        print_options(options)
        print("Correct answer: ",value)
    elif question_type == 12:
        # solver.hexadecimal_to_decimal()
        converted_value = solver.decimal_to_hexadecimal(value)
        print("(",converted_value,")base16  -->  (?)base10")
        option_values.append(value)
        shuffle(option_values)
        print_options(option_values)
        print("Correct answer: ",value)
    elif question_type == 13:
        print("(",value,")base10  -->  (?)bcd")
        converted_value = solver.decimal_to_bcd(value)
        options = [solver.decimal_to_bcd(val) for val in option_values]
        options.append(converted_value)
        shuffle(options)
        print_options(options)
        print("Correct answer: ",converted_value)
    elif question_type == 14:
        print("(",value,")base10  -->  (?)gray_code")
        converted_value = solver.decimal_to_gray_code(value)
        options = [solver.decimal_to_gray_code(val) for val in option_values]
        options.append(converted_value)
        shuffle(options)
        print_options(options)
        print("Correct answer: ",converted_value)
    elif question_type == 15:
        print(question_map[question_type]," of ",value)
        converted_value = solver.decimal_to_1s_complement(value)
        options = [solver.decimal_to_1s_complement(val) for val in option_values]
        options.append(converted_value)
        shuffle(options)
        print_options(options)
        print("Correct answer: ",converted_value)
    elif question_type == 16:
        print(question_map[question_type]," of ",value)
        converted_value = solver.decimal_to_2s_complement(value)
        options = [solver.decimal_to_2s_complement(val) for val in option_values]
        options.append(converted_value)
        shuffle(options)
        print_options(options)
        print("Correct answer: ",converted_value)

def generate_questions():
    """
        Function to generate options
    """
    question_type = randint(1,len(question_map))
    value = randint(1,99999)
    option_values = [value+1, value+2, value+3]
    print("Convert")
    number_conversion(question_type, value, option_values)
