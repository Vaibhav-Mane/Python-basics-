
import operator
num1 = int(input("enter your first number: "))
num2 = int(input("enter your second number: "))
ops1 = int(input("enter your operator"))
ops= {"+":operator.add,
      "-":operator.sub,
      "*":operator.mul,
      "/":operator.div
      }
if ops1 in ops:
    print(ops)

