"""
Matemática φ esencial
"""

import numpy as np

PHI = (1 + 5 ** 0.5) / 2


def phi_pow(n: int) -> float:
    return PHI ** n


def phi_weights() -> np.ndarray:
    return np.diag([phi_pow(i) for i in range(7)])


def phi_norm(v: np.ndarray) -> float:
    w = phi_weights()
    return float(np.sqrt(np.dot(v, w @ v)))
