from z3 import *

num_threads = 32

thread_ids = [BitVec(f'thread{i}', 32) for i in range(num_threads)]

shared_memory = [BitVec(f'shared_mem_{i}', 32) for i in range(num_threads)]

sync_before_read = Bool('sync_before_read')

solver = Solver()

for i in range(num_threads - 1):
    solver.add(shared_memory[i+1] == shared_memory[i] + 1)


for i in range(num_threads):

    solver.add(Implies(Not(sync_before_read), thread_ids[i] == -1))

if solver.check() == sat:
    print("Synchronization issue or memory coalescing failure. Counterexample:")
    print(solver.model())
else:
    print("Memory accesses are correctly coalesced and synchronized.")

