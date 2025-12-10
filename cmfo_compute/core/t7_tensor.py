import numpy as np


class T7Tensor:
    """Tensor CMFO 7D con estructura φ-modal."""

    def __init__(self, v):
        self.v = np.array(v, dtype=float)

    def evolve(self, steps=1):
        """Evolución CMFO básica."""
        out = self.v.copy()
        for _ in range(steps):
            out = np.tanh(out)
        return T7Tensor(out)

    def norm(self):
        """Norma φ-modal."""
        return float(np.linalg.norm(self.v))

    def __repr__(self):
        return f"T7Tensor({self.v})"
