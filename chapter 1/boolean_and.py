# input 2 variables only 1 or 0
# output 1 only if both inputs are 1
import sys

def boolean_and(x:int,y:int)-> int:
    if x and y not in [0,1]:
        print("only 1 & 0 permittible as input")
        sys.exit()
    if x==y==1:
        return 1
    else:
        return 0

x= int(input("operand x: "))
y= int(input("operand y: "))

print(f"\nboolean and({x},{y}) = {boolean_and(x,y)}")
