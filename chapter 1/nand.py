# not of and

import sys

def boolean_nand(x:int,y:int)-> int:
    if x and y not in [0,1]:
        print("only 1 & 0 permittible as input")
        sys.exit()
    if x==y==1:
        return 0
    else:
        return 1

x= int(input("operand x: "))
y= int(input("operand y: "))

print(f"\nnand({x},{y}) = {boolean_nand(x,y)}")        