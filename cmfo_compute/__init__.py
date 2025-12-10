"""
CMFO Compute – API pública limpia
"""

from .core.t7_tensor import T7Tensor
from .core.gamma_phi import gamma_step
from .logic.phi_logic import (
    phi_sign,
    phi_and,
    phi_or,
    phi_not,
    phi_xor,
    phi_nand,
)

__all__ = [
    "T7Tensor",
    "gamma_step",
    "phi_sign",
    "phi_and",
    "phi_or",
    "phi_not",
    "phi_xor",
    "phi_nand",
]


def tensor(x):
    return T7Tensor(x)


def evolve(x, steps=1):
    t = T7Tensor(x)
    t = t.evolve(steps)
    return t
