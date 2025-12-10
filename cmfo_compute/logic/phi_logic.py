import numpy as np
from cmfo_compute.core.gamma_phi import gamma_step


def phi_sign(v):
    """
    Indicación modal φ-signo sobre vector 7D.

    Implementación formal:
        φ_sign(v) = sign( sum( gamma_step(v) ) )
    donde gamma_step aplica la proyección CMFO de un vector en ℝ⁷.
    """
    v = np.array(v, dtype=float)
    g = gamma_step(v)
    return float(np.sign(np.sum(g)))


def phi_and(a, b):
    """
    Lógica AND φ-modal:
        ANDφ(a, b) = sign( φ_sign(a) + φ_sign(b) )
    """
    return float(np.sign(phi_sign(a) + phi_sign(b)))


def phi_or(a, b):
    """
    OR φ-modal:
        ORφ(a, b) = sign( φ_sign(a) + φ_sign(b) + 1 )
    """
    return float(np.sign(phi_sign(a) + phi_sign(b) + 1))


def phi_not(a):
    """
    NOT φ-modal:
        NOTφ(a) = -φ_sign(a)
    """
    return -phi_sign(a)


def phi_xor(a, b):
    """
    XOR φ-modal:
        XORφ(a, b) = sign( φ_sign(a) - φ_sign(b) )
    """
    return float(np.sign(phi_sign(a) - phi_sign(b)))


def phi_nand(a, b):
    """
    NAND φ-modal:
        NANDφ(a, b) = NOT(ANDφ(a, b))
    """
    return -phi_and(a, b)
