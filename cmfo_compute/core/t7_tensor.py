import numpy as np
from .gamma_phi import gamma_step


class T7Tensor:
    def __init__(self, v):
        self.v = np.array(v, dtype=float)

    def evolve(self, steps=1):
        v = self.v.copy()
        for _ in range(steps):
            v = gamma_step(v)
        return T7Tensor(v)

    def norm(self):
        return float(np.linalg.norm(self.v))
