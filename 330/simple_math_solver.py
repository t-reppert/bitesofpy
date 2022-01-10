from itertools import permutations
from operator import add, sub, mul
from typing import List, Union, Iterable, Any

OPERATORS = {
    '+': add,
    '-': sub,
    '*': mul
}

def calculate(values: List[Any], operators: List[Any]) -> int:
    ops = operators.copy()
    nums = values.copy()
    calculation = nums.pop(0)
    while ops:
        operate = ops.pop(0)
        next_val = nums.pop(0)
        while ops and ops[0] == mul:
            ops.pop(0)
            next_val *= nums.pop(0)
        calculation = operate(calculation, next_val)
    return calculation


def find_all_solutions(
    operator_path: List[str], expected_result: int
) -> Union[List[List[int]], Iterable[List[int]]]:
    solutions = []
    operators = []
    if not isinstance(expected_result, int):
        raise ValueError('Expected result needs to be integer!')
    for op in operator_path:
        if op not in OPERATORS:
            raise ValueError('Allowed operators: + - and * only!')
        operators.append(OPERATORS[op])
    if len(operators) > 10:
        raise ValueError('Too many operators')

    for values in permutations(range(1, 10), len(operator_path) + 1):
        values = list(values)
        if calculate(values, operators) == expected_result:
            solutions.append(values)
    return solutions
