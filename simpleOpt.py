from z3 import *

x = Int('x')
y = Int('y')
z = Int('z')

original_expr = (x + y) * z

optimized_expr = x * z + y * z

s = Solver()

s.add(original_expr != optimized_expr)

if s.check() == sat:
    print("The optimization is incorrect. Counterexample:")
    print(s.model())  # Print the counterexample
else:
    print("The optimization is correct.")

