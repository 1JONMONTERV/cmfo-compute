import numpy as np
from .phi_math import PHI

def gamma_matrix():
    G = np.eye(7)
    # Usamos tres ángulos φ para rotaciones parciales
    angles = [(PHI**(k-3)) % np.pi for k in range(3)]
    for i, th in enumerate(angles):
        c = np.cos(th)
        s = np.sin(th)
        j = i + 1
        R = np.eye(7)
        R[i, i] = c
        R[j, j] = c
        R[i, j] = -s
        R[j, i] = s
        G = R @ G
    return G

GAMMA = gamma_matrix()

def gamma_step(v):
    v = np.array(v, dtype=np.float64)
    return GAMMA @ v
