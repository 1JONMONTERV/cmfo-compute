import numpy as np
from .gamma_phi import gamma_step
from .phi_math import phi_norm

class T7Tensor:
    def __init__(self, v):
        self.v = np.array(v, dtype=np.float64)

    def norm(self):
        return phi_norm(self.v)

    def evolve(self, steps):
        x = self.v.copy()
        for _ in range(steps):
            x = gamma_step(x)
        return T7Tensor(x)

    def __repr__(self):
        return f"T7Tensor({self.v})"
