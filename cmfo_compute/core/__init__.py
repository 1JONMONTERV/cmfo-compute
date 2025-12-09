"""
Core CMFO - Operador φ, matemáticas φ y T7Tensor
"""

from .phi_math import (
    PHI,
    phi_pow,
    phi_weights,
    phi_norm,
)
from .gamma_phi import gamma_step
from .t7_tensor import T7Tensor

__all__ = [
    "PHI",
    "phi_pow",
    "phi_weights",
    "phi_norm",
    "gamma_step",
    "T7Tensor",
]
