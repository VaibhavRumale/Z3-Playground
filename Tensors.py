from z3 import *

def to_fp16(x):
    return FPVal(float(x), FPSort(11, 5))  

#floating-point variables for matrices A, B, and C
a11, a12, a21, a22 = [FP('a'+str(i), FPSort(11, 5)) for i in range(1, 5)]
b11, b12, b21, b22 = [FP('b'+str(i), FPSort(11, 5)) for i in range(1, 5)]
c11, c12, c21, c22 = [FP('c'+str(i), FPSort(11, 5)) for i in range(1, 5)]

#C = A * B + C
fused_c11 = fpAdd(RNE(), fpMul(RNE(), a11, b11), c11)
fused_c12 = fpAdd(RNE(), fpMul(RNE(), a12, b12), c12)
fused_c21 = fpAdd(RNE(), fpMul(RNE(), a21, b21), c21)
fused_c22 = fpAdd(RNE(), fpMul(RNE(), a22, b22), c22)

#non-fused version: temp = A * B; C = temp + C
temp_c11 = fpAdd(RNE(), fpMul(RNE(), a11, b11), c11)
temp_c12 = fpAdd(RNE(), fpMul(RNE(), a12, b12), c12)
temp_c21 = fpAdd(RNE(), fpMul(RNE(), a21, b21), c21)
temp_c22 = fpAdd(RNE(), fpMul(RNE(), a22, b22), c22)

s = Solver()

s.add(fused_c11 != temp_c11)
s.add(fused_c12 != temp_c12)
s.add(fused_c21 != temp_c21)
s.add(fused_c22 != temp_c22)

if s.check() == sat:
    print("The optimization is incorrect. Counterexample found:")
    print(s.model())
else:
    print("The optimization is correct.")

