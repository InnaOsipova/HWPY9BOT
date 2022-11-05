from fractions import Fraction

def calculation(a, operation, b):
    result = None
    if operation == '+':
        result = a + b
    elif operation == '-':
        result = a - b
    elif operation == '/' or '/':
        result = a / b
    elif operation == '*':
        result = a * b
    else:
        print('Неизвестный оператор')
    return result


def calc_ration(massage):
    user_expression = massage.split()
    first_number, second_number = (user_expression[0]).split('/'), user_expression[2].split('/')

    number_a = Fraction(int(first_number[0]), int(first_number[1]))
    number_b = Fraction(int(second_number[0]), int(second_number[1]))

    calc_result = calculation(number_a, user_expression[1], number_b)
    result = str("".join(map(str, user_expression)) + " = " + str(calc_result))
    print(result)
    return result


def calc_complex(massege1):
    user_expression = massege1.split()
    a_imaginary_part, b_imaginary_part = float(user_expression[2]), float(user_expression[6])

    if user_expression[1] == '-':
        a_imaginary_part = float(user_expression[2]) * -1
    if user_expression[5] == '-':
        b_imaginary_part = float(user_expression[6]) * -1

    number_a = complex(float(user_expression[0]), a_imaginary_part)
    number_b = complex(float(user_expression[4]), b_imaginary_part)
    calc_result = calculation(number_a, user_expression[3], number_b)
    result = str("".join(map(str, user_expression)) + " = " + str(calc_result))
    print(result)
    return result
