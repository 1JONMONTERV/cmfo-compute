import numpy as np
from .phi_math import phi_weights

def gamma_step(x):
    x = np.array(x, dtype=float)
    w = phi_weights(len(x))
    return np.tanh(x * w)
