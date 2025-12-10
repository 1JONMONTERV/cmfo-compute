import numpy as np

PHI = (1 + 5**0.5) / 2

def phi_pow(x):
    return np.power(PHI, x)

def phi_weights(n):
    return np.array([phi_pow(i) for i in range(1, n+1)])

def phi_norm(x):
    return np.sqrt(np.sum(np.array(x, dtype=float)**2))
