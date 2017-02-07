#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

if len(sys.argv) != 4:
    sys.exit('Usage: python3 calc.py operation operand1 operand2')

# sys.argv es una lista con los diferentes argumentos ("_" es el .py)
_, operacion, operando1, operando2 = sys.argv

try:
    operando1 = float(operando1)
    operando2 = float(operando2)
except ValueError:
    sys.exit('Operands must be floats. TY!')

if operacion == 'sumar':
    resultado = operando1 + operando2
    print('Resultado: ', resultado)
elif operacion == 'restar':
    resultado = operando1 - operando2
    print('Resultado: ', resultado)
elif operacion == 'dividir':
    try:
        resultado = operando1 / operando2
        print('Resultado: ', resultado)
    except ZeroDivisionError:
        print('Ops! Cannot divide by 0')

elif operacion == 'multiplicar':
    resultado = operando1 * operando2
    print('Resultado: ', resultado)
