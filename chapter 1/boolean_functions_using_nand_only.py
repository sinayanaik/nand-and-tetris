
import sys

def boolean_nand(x:int,y:int)-> int:
    if x and y not in [0,1]:
        print("only 1 & 0 permittible as input")
        sys.exit()
    if x==y==1:
        return 0
    else:
        return 1

def bool_not(x:int)->int:
    if x==1:
        return 0
    elif x== 0:
        return 1

def boolean_and(x:int,y:int)-> int:
    if x==y==1:
        return 1
    else:
        return 0

def boolean_or(x:int,y:int)-> int:
    if x==y==0:
        return 0
    else:
        return 1

x= int(input("operand x: "))
y= int(input("operand y: "))

print(f"\nnand({x},{y}) = {boolean_nand(x,y)}")

nand_gate = """
Observations In other words:
• Not ( x ) = x Nand x                   
• x And y = Not ( x Nand y)              
• x Or y = Not(Not(x) And Not(y))         
• (De Morgan)
"""

print(f"{nand_gate}")

# not 
print("\nNot can be realized using Nand")
print(f"\tNot({x}) = {x}Nand{x}")
print(f"\t{bool_not(x)} = {boolean_nand(x,x)}")

# and
x_nand_y = boolean_nand(x,y)
and_by_nand = bool_not(x_nand_y)
print("\nAnd can be realized using Nand")
print(f"\t{x} And {y} = Not ( {x} Nand {y})")
print(f"\t{boolean_and(x,y)} = Not ( {boolean_nand(x,y)})")
print(f"\t{boolean_and(x,y)} = {and_by_nand}")


# or
not_x = bool_not(x)
not_y = bool_not(y)
not_x_and_not_y = boolean_and(not_x,not_y)
or_by_nand = bool_not(not_x_and_not_y)

print("\nOr can be realized using Nand")
print(f"\t{x} Or {y} = Not(Not({x}) And Not({y}))")
print(f"\t{boolean_or(x,y)} = Not({bool_not(x)} And {bool_not(y)})")
print(f"\t{boolean_or(x,y)} = Not({boolean_and(bool_not(x),bool_not(y))})")
print(f"\t{boolean_or(x,y)} = {or_by_nand}")


