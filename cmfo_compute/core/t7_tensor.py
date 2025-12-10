import numpy as np
from .phi_math import phi_norm
from .gamma_phi import gamma_step

class T7Tensor:
    def __init__(self, data):
        arr = np.array(data, dtype=float)
        self.v = arr  # API pública requerida por tests
        self.data = arr  # respaldo interno

    def evolve(self, steps=1):
        out = self.v.copy()
        for _ in range(steps):
            out = gamma_step(out)
        return T7Tensor(out)

    def norm(self):
        return phi_norm(self.v)

    def __repr__(self):
        return f"T7Tensor({self.v})"
