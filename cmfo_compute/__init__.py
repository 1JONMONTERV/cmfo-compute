from .core.t7_tensor import T7Tensor
from .core.phi_math import PHI, phi_pow, phi_norm, phi_weights
from .core.gamma_phi import gamma_step
from .logic.phi_logic import (
    phi_sign, phi_and, phi_or, phi_not, phi_xor, phi_nand
)

def tensor(x):
    return T7Tensor(x)

def evolve(x, steps=1):
    t = T7Tensor(x)
    return t.evolve(steps)

__all__ = [
    "T7Tensor",
    "tensor",
    "evolve",
    "PHI",
    "phi_pow",
    "phi_norm",
    "phi_weights",
    "gamma_step",
    "phi_sign",
    "phi_and",
    "phi_or",
    "phi_not",
    "phi_xor",
    "phi_nand",
]
