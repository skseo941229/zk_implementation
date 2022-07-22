import sys
from pybp.pederson import PedersonCommitment
from pybp.rangeproof import RangeProof

value = int(sys.argv[1])
print(value)

rp = RangeProof(32) 
proofval = value & (2**32 - 1)
rp.generate_proof(proofval)
Varg = PedersonCommitment(value, b = rp.gamma)
print("Commited Value: ", Varg.get_commitment())

print("Keep below values to verify your commitment")
print("H: ", Varg.h)
print("r:", Varg.b)

print("v:", Varg.v)