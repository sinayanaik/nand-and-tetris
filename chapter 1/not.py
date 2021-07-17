# invert the input
import sys

def bool_not(x:int):
    if x not in [0,1]:
        print("only 1 & 0 permittible as input")
        sys.exit()
    if x==1:
        return 0
    elif x== 0:
        return 1

x= int(input("enter operand x: "))
print(f"not({x}) = {bool_not(x)}")         
