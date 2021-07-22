#  gives a true (1) output when the number of true inputs is odd

import sys

def boolean_xor(x:int,y:int)-> int:
    if x and y not in [0,1]:
        print("only 1 & 0 permittible as input")
        sys.exit()
    if x+y==1:
        return 1
    else:
        return 0

x= int(input("operand x: "))
y= int(input("operand y: "))

print(f"\nxor({x},{y}) = {boolean_xor(x,y)}")