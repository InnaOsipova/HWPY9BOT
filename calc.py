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


def calc_ration():
    user_expression = input('Введите выражение для вычисления в формате: "A/B действие C/D, где:"'
                            '\n A и B - числители первой и второй дроби'
                            '\n C и D - знаменатели первой и второй дроби'
                            '\nдействие - математическая операция которую нужно произвести с двумя числами'
                            '\nМежду дробями и действием ставьте пробелы:'
                            '\n').split()
    first_number, second_number = (user_expression[0]).split('/'), user_expression[2].split('/')

    number_a = Fraction(int(first_number[0]), int(first_number[1]))
    number_b = Fraction(int(second_number[0]), int(second_number[1]))

    calc_result = calculation(number_a, user_expression[1], number_b)
    result = str("".join(map(str, user_expression)) + " = " + str(calc_result))
    print(result)
    return result


def calc_complex():
    user_expression = input('Введите выражение для вычисления в формате: "A знак B действие C знак D, где:'
                            '\n A и C - действительные части чисел"'
                            '\n B и D - мнимые части чисел'
                            '\n действие - математическая операция которую нужно произвести с двумя числами'
                            '\nМежду числами и знаком ставьте пробелы:'
                            '\n').split()
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
