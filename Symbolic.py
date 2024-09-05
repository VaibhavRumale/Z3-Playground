from z3 import *

x = Int('x')
y = Int('y')

s = Solver()

s.add(x > 5)
s.add(x < 10)
s.add(y == x + 3)

if s.check() == sat:
    print("Satisfiable inputs:", s.model())
else:
    print("Unsatisfiable")

