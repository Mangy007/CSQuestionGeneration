from random import randint
import core.question_solver.module_1_solver as solver

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
    12: "Hexadecimal to Decimal"
}

question_type = randint(1,12)
value = randint(1,99999)
print(question_type)
print("Convert")

if question_type == 1:
    print("(",value,")base10  -->  (?)base2")
    value = solver.decimal_to_binary(value)
    print(value)
elif question_type == 2:
    print("(",value,")base10  -->  (?)base8")
    value = solver.decimal_to_octal(value)
    print(value)
elif question_type == 3:
    print("(",value,")base10  -->  (?)base16")
    value = solver.decimal_to_hexadecimal(value)
    print(value)
elif question_type == 4:
    converted_value = solver.decimal_to_binary(value)
    print("(",converted_value,")base2  -->  (?)base8")
    value = solver.decimal_to_octal(value)
    print(value)
elif question_type == 5:
    # solver.binary_to_decimal() 
    converted_value = solver.decimal_to_binary(value)
    print("(",converted_value,")base2  -->  (?)base10")
    print(value)
elif question_type == 6:
    # solver.binary_to_hexadecimal()
    converted_value = solver.decimal_to_binary(value)
    print("(",converted_value,")base2  -->  (?)base8")
    value = solver.decimal_to_hexadecimal(value)
    print(value)
elif question_type == 7:
    # solver.octal_to_binary() 
    converted_value = solver.decimal_to_octal(value)
    print("(",converted_value,")base8  -->  (?)base2")
    value = solver.decimal_to_binary(value)
    print(value)
elif question_type == 8:
    # solver.octal_to_decimal()
    converted_value = solver.decimal_to_octal(value)
    print("(",converted_value,")base8  -->  (?)base10")
    print(value)
elif question_type == 9:
    # solver.octal_to_hexadecimal() 
    converted_value = solver.decimal_to_octal(value)
    print("(",converted_value,")base8  -->  (?)base16")
    value = solver.decimal_to_hexadecimal(value)
    print(value)
elif question_type == 10:
    # solver.hexadecimal_to_binary()
    converted_value = solver.decimal_to_hexadecimal(value)
    print("(",converted_value,")base16  -->  (?)base2")
    value = solver.decimal_to_binary(value)
    print(value)
elif question_type == 11:
    # solver.hexadecimal_to_octal() 
    converted_value = solver.decimal_to_hexadecimal(value)
    print("(",converted_value,")base16  -->  (?)base8")
    value = solver.decimal_to_octal(value)
    print(value)
elif question_type == 12:
    # solver.hexadecimal_to_decimal()
    converted_value = solver.decimal_to_hexadecimal(value)
    print("(",converted_value,")base16  -->  (?)base10")
    print(value)