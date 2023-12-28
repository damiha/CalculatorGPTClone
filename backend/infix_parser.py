from typing import List
from collections import deque

def to_infix_tokens(infix_str: str, precedence_order: dict) -> List[str]:
    
    last_was_digit = False

    str_with_whitespaces = ""

    operators_with_whitespaces = set(precedence_order.keys()).union({"(", ")"})
    digits = set(map(lambda d: str(d), range(10)))

    for c in infix_str:

        if c in operators_with_whitespaces:
            str_with_whitespaces += f" {c} "
            last_was_digit = False

        elif c in digits or c == ".":
            if last_was_digit:
                str_with_whitespaces += f"{c}"
            else:
                last_was_digit = True
                str_with_whitespaces += f" {c}"
            

    str_with_whitespaces += " "

    infix_tokens = list(filter(lambda t: len(t) > 0, str_with_whitespaces.split(" ")))

    return infix_tokens


def is_convertible_to_number(s):
    try:
        # Try converting to a float first (since it can include integers as well)
        float(s)
        return True
    except ValueError:
        # If an error is raised, it means the string cannot be converted to a number
        return False

def infix_to_rpn(infix_tokens: List[str], precedence_order: dict)->List[str]:

    # apply dijkstra's shunting yard
    output_queue = []
    operator_stack = []

    for token in infix_tokens:
        # numbers are directed to the output queue
        if is_convertible_to_number(token):
            output_queue.append(token)

        elif token in precedence_order:

            if len(operator_stack) > 0:
                # comparing precedence levels
                operator_on_top = operator_stack[-1]

                if operator_on_top != "(" and precedence_order[operator_on_top] >= precedence_order[token]:
                    output_queue.append(operator_stack.pop())

            operator_stack.append(token)

        elif token == "(":
            operator_stack.append(token)

        elif token == ")":
            
            while True:
                if len(operator_stack) == 0:
                    raise Exception("Could not find matching left parantheses!")
                
                operator_on_top = operator_stack.pop()

                if operator_on_top == "(":
                    break

                else:
                    output_queue.append(operator_on_top)

        else:
            raise Exception(f"Could not parse {token}")

    output_queue += operator_stack[::-1]

    return output_queue

def rpn_to_number(rpn: List[str]) -> float:
    
    operand_stack: List[float] = []

    binops = {
        "+": lambda a, b: a + b,
        "*": lambda a, b: a * b,
        "-": lambda a, b: a - b,
        "/": lambda a, b: a / b
    }

    for token in rpn:
        if is_convertible_to_number(token):
            operand_stack.append(float(token))

        elif token in binops:
            
            if len(operand_stack) < 2:
                raise Exception("Parser error; Binary operation doesn't have two operands!")
            
            b = operand_stack.pop()
            a = operand_stack.pop()

            result = binops[token](a, b)

            operand_stack.append(result)

        else:
            raise Exception(f"Unknown token {token}")
            
    if len(operand_stack) != 1:
        raise Exception("Operand stack doesn't have exactly one element!")

    return operand_stack[0]

def parse(infix_str, precedence_order: dict) -> float:
    infix_tokens = to_infix_tokens(infix_str, precedence_order)
    return rpn_to_number(infix_to_rpn(infix_tokens, precedence_order))
    

precedence_order = {
    "*": 2,
    "/": 2,
    "+": 1,
    "-": 1
}