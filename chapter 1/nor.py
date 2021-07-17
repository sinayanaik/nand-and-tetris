# not of or
import sys

def boolean_or(x:int,y:int)-> int:
    if x and y not in [0,1]:
        print("only 1 & 0 permittible as input")
        sys.exit()
    if x==y==0:
        return 1
    else:
        return 0

x= int(input("operand x: "))
y= int(input("operand y: "))

print(f"\nboolean or({x},{y}) = {boolean_or(x,y)}")