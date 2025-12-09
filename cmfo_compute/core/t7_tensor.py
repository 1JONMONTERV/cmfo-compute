"""
Tensor fractal en R7
"""

import numpy as np
from .gamma_phi import gamma_step


class T7Tensor:
    def __init__(self, v):
        self.v = np.array(v, dtype=float)

    def evolve(self, steps: int):
        v = self.v.copy()
        for _ in range(steps):
            v = gamma_step(v)
        return T7Tensor(v)

    def __repr__(self) -> str:
        return f"T7Tensor({self.v})"
