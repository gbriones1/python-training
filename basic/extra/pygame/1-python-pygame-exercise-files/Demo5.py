import ast

syntaxTree = ast.parse("""
temp = 20

for x in range(temp):
    print(x)
""")

print(ast.dump(syntaxTree))

import math

print("The square root of 64 is %f" % math.sqrt(64))