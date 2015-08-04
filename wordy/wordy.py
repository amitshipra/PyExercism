__author__ = 'dias'

def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def division(x, y):
    return float(x / y)


OPERATIONS = {'plus': add, 'minus': subtract, 'multiplied': multiply, 'divided': division}

def calculate(line):
    tokens = line.split()
    # Clean the last token and remove ? at the end.
    tokens.append(tokens.pop()[:-1])

    print(tokens)

    operands = [int(x) for x in tokens if is_number(x)]
    operators = [x for x in tokens if x in OPERATIONS]
    print(operands, operators)

    if len(operators) == 0 or (len(operands) - len(operators) != 1):
        raise ValueError()

    def process(operators, operands):
        first = operands.pop()
        second = operands.pop()
        operator = operators.pop()
        result = OPERATIONS[operator](first, second)
        operands.append(result)
        if len(operators) == 0:
            return operands[0]
        else:
            return process(operators, operands)

    return process(operators[::-1], operands[::-1])

def is_number(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

print(calculate("What is -12000 divided by 25 divided by -30?"))
