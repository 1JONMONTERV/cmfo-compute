import numpy as np


def gamma_step(v):
    v = np.array(v, dtype=float)
    g = np.sin(v) + np.cos(v)
    return g
