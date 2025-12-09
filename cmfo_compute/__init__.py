from .core.t7_tensor import T7Tensor
from .core.gamma_phi import gamma_step
from .core.phi_math import phi_norm, PHI
from .logic.phi_logic import (
    phi_sign,
    phi_and,
    phi_or,
    phi_not,
    phi_xor,
    phi_nand,
)

# API principal estilo NumPy/Torch

def tensor(v):
    return T7Tensor(v)

def evolve(v, steps):
    # transforma lista a tensor y aplica evolución
    v = T7Tensor(v)
    return v.evolve(steps)

def norm_phi(v):
    return phi_norm(v)
