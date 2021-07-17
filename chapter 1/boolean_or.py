# input 2 variables only 1 or 0
# output 0 only if both inputs are 0
import sys

def boolean_or(x:int,y:int)-> int:
    if x and y not in [0,1]:
        print("only 1 & 0 permittible as input")
        sys.exit()
    if x==y==0:
        return 0
    else:
        return 1

x= int(input("operand x: "))
y= int(input("operand y: "))

print(f"\nboolean or({x},{y}) = {boolean_or(x,y)}")