
def aufgabe_3():
    stack = []
    for i in range(127):
        stack.append(i + 1)
    while len(stack) != 0:
        print(stack.pop())


def aufgabe_4():
    numbers, ops, operatoren = [], [], ["+", "*", "-", "/"]
    for element in input("Eingabe: ").split(" "):
        if element.isnumeric():
            numbers.append(int(element))
        elif element in operatoren:
            ops.append(element)
    while len(numbers) > 1:
        numbers.append(calc(numbers.pop(), numbers.pop(), ops.pop()))
    print(numbers[0])


def calc(number1: int, number2: int, operator: str):
    match operator:
        case "+":
            return number1 + number2
        case "*":
            return number1 * number2
        case"-":
            return number2 - number1
        case "/":
            return number2 / number1
