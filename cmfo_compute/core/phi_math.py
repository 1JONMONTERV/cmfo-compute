import numpy as np

PHI = 1.6180339887498948

def phi_pow(n):
    return PHI ** n

def phi_weights():
    # diag(φ^0, φ^-1, ..., φ^-6)
    return np.diag([PHI**(-i) for i in range(7)])

def phi_norm(v):
    W = phi_weights()
    v = np.array(v, dtype=np.float64)
    return np.sqrt(v.T @ W @ v)
