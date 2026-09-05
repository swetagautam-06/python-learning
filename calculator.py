def add(n1, n2):
    return n1+n2

def subtract(n1, n2):
    return n1-n2

def multiply(n1, n2):
    return n1*n2

def divide(n1, n2):
    return n1/n2

operation ={
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
    }

num1 = int(input("First number: "))
for symbol in operation:
    print(symbol)
should_continue = True

while should_continue:
    op_symbol = input("pick an operation from the line above: ")
    num2 = int(input("Second number: "))
    calculation_function = operation[op_symbol]
    f_answer = calculation_function(num1, num2)

    print(f"{num1} {op_symbol} {num2} = {f_answer}")

    op_symbol = input("Pick another operation")
    num3 = int(input("next number: "))
    calculation_function = operation[op_symbol]
    s_answer = calculation_function(calculation_function(num1, num2), num3)

    print(f"{f_answer} {op_symbol} {num3} = {s_answer}")










