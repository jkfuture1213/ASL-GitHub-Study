#!/usr/bin/env python3

"""Simple arithmetic calculator.

Input examples:
  3 + 4
  10 / 2
  5 * 6
  7 - 2

Type 'quit', 'exit', or press Ctrl+C to exit.
"""

import operator

OPS = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
}


def calculate(expression: str) -> float:
    """Evaluate a simple expression and return the result."""
    parts = expression.strip().split()
    if len(parts) != 3:
        raise ValueError("Expression must be in the form 'number operator number'.")

    left, op, right = parts
    if op not in OPS:
        raise ValueError(f"Unsupported operator: {op}")

    try:
        left_value = float(left)
        right_value = float(right)
    except ValueError as exc:
        raise ValueError("Please enter valid numbers.") from exc

    if op == '/' and right_value == 0:
        raise ZeroDivisionError("Cannot divide by zero.")

    return OPS[op](left_value, right_value)


if __name__ == '__main__':
    print("Simple arithmetic calculator")
    print("Example: 3 + 4")
    print("Exit: quit, exit, Ctrl+C")

    while True:
        try:
            expression = input('> ').strip()
        except (KeyboardInterrupt, EOFError):
            print('\nExiting.')
            break

        if not expression:
            continue

        if expression.lower() in {'quit', 'exit'}:
            print('Exiting.')
            break

        try:
            result = calculate(expression)
        except Exception as exc:
            print(f'Error: {exc}')
        else:
            if result.is_integer():
                print(int(result))
            else:
                print(result)
