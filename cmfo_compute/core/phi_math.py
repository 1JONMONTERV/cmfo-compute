import numpy as np

PHI = (1 + 5**0.5) / 2


def phi_pow(x):
    return x**PHI


def phi_norm(v):
    v = np.array(v, dtype=float)
    return np.linalg.norm(v) ** (1 / PHI)
