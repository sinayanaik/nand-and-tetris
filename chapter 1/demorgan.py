import sys

demorgan_rule = """
    Not(x And y) = Not(x) Or Not(y)
    Not(x Or y) = Not(x) and Not(y)
"""
print(f"The two rules of demorgan are{demorgan_rule}")


def boolean_and(x: int, y: int) -> int:
    if x == y == 1:
        return 1
    else:
        return 0


def boolean_or(x: int, y: int) -> int:
    if x == y == 0:
        return 0
    else:
        return 1


def bool_not(x: int)-> int:
    if x == 1:
        return 0
    elif x == 0:
        return 1


def boolean_demorgan(x: int, y: int)-> int:
    if x and y not in [0, 1]:
        print("only 0 and 1 permitted input")
        sys.exit()
    x_and_y = int(boolean_and(x, y))
    x_or_y = int(boolean_or(x, y))
    not_x = int(not(x))
    not_y = int(not(y))
    not_x_and_y = int(not(x_and_y))
    not_x_or_y = int(not(x_or_y))
    #1st formula
    print(f"\n\tNot({x} And {y}) = Not({x}) Or Not({y})")
    print(f"\tNot({x_and_y}) = {not_x} Or {not_y}")
    print(f"\t{not_x_and_y} = {boolean_or(not_x,not_y)}")
    #2ndformula
    print(f"\n\tNot({x} Or {y}) = Not({x}) and Not({y})")
    print(f"\tNot({x_or_y}) = {not_x} and {not_y}")
    print(f"\t{not_x_or_y} = {boolean_and(not_x,not_y)}")

x = int(input("enter operand x: "))
y = int(input("enter operand y: "))

boolean_demorgan(x, y)
