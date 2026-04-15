import math
import sys


class RPNError(Exception):
    pass


def pop1(stack):
    if len(stack) < 1:
        raise RPNError("pila insuficiente")
    return stack.pop()


def pop2(stack):
    if len(stack) < 2:
        raise RPNError("pila insuficiente")
    b = stack.pop()
    a = stack.pop()
    return a, b


def eval_rpn(expr):

    stack = []
    mem = [0.0] * 10

    const = {"p": math.pi, "e": math.e, "j": (1 + math.sqrt(5)) / 2}

    tokens = expr.split()

    for t in tokens:

        # NUMEROS
        try:
            stack.append(float(t))
            continue
        except ValueError:
            pass

        # CONSTANTES
        if t in const:
            stack.append(const[t])
            continue

        # OPERADORES
        if t in "+-*/":
            a, b = pop2(stack)

            if t == "+":
                stack.append(a + b)

            elif t == "-":
                stack.append(a - b)

            elif t == "*":
                stack.append(a * b)

            elif t == "/":
                if b == 0:
                    raise RPNError("division por cero")
                stack.append(a / b)

            continue

        # COMANDOS DE PILA
        if t == "dup":
            a = pop1(stack)
            stack.append(a)
            stack.append(a)
            continue

        if t == "swap":
            a, b = pop2(stack)
            stack.append(b)
            stack.append(a)
            continue

        if t == "drop":
            pop1(stack)
            continue

        if t == "clear":
            stack.clear()
            continue

        # CHS
        if t == "chs":
            stack.append(-pop1(stack))
            continue

        # FUNCIONES
        if t == "sqrt":
            stack.append(math.sqrt(pop1(stack)))
            continue

        if t == "log":
            stack.append(math.log10(pop1(stack)))
            continue

        if t == "ln":
            stack.append(math.log(pop1(stack)))
            continue

        if t == "ex":
            stack.append(math.exp(pop1(stack)))
            continue

        if t == "10x":
            stack.append(10 ** pop1(stack))
            continue

        if t == "1/x":
            a = pop1(stack)
            if a == 0:
                raise RPNError("division por cero")
            stack.append(1 / a)
            continue

        if t == "yx":
            a, b = pop2(stack)
            stack.append(a**b)
            continue

        # TRIGONOMETRICAS (grados)
        if t == "sin":
            stack.append(math.sin(math.radians(pop1(stack))))
            continue

        if t == "cos":
            stack.append(math.cos(math.radians(pop1(stack))))
            continue

        if t == "tg":
            stack.append(math.tan(math.radians(pop1(stack))))
            continue

        if t == "asin":
            stack.append(math.degrees(math.asin(pop1(stack))))
            continue

        if t == "acos":
            stack.append(math.degrees(math.acos(pop1(stack))))
            continue

        if t == "atg":
            stack.append(math.degrees(math.atan(pop1(stack))))
            continue

        # MEMORIAS
        if t == "sto":
            i = int(pop1(stack))
            if not 0 <= i <= 9:
                raise RPNError("memoria invalida")
            mem[i] = pop1(stack)
            continue

        if t == "rcl":
            i = int(pop1(stack))
            if not 0 <= i <= 9:
                raise RPNError("memoria invalida")
            stack.append(mem[i])
            continue

        raise RPNError(f"token invalido: {t}")

    if len(stack) != 1:
        raise RPNError("la pila no termino con un unico valor")

    return stack[0]


def main():

    try:

        if len(sys.argv) > 1:
            expr = " ".join(sys.argv[1:])
        else:
            expr = input("RPN> ")

        result = eval_rpn(expr)

        print(result)

    except RPNError as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
