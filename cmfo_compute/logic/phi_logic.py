"""
Lógica φ-modal para CMFO Compute
"""

import numpy as np


KER = np.array(
    [
        0.66953749,
        -0.52523023,
        -0.28826978,
        -0.02423008,
        -0.29564348,
        0.14203233,
        -0.56358893,
    ]
)

D = np.array(
    [
        [0.66953749, 0.78583022, -0.14602454, 0.28411589, -0.02527228, 0.176075, 0.18316346],
        [-0.52523023, 0.85146346, 0.65078142, -0.09906758, 0.22756086, 0.01884947, 0.29554377],
        [-0.28826978, -0.46389767, 0.73047862, 0.6270363, -0.18530429, 0.21440992, 0.0918214],
        [-0.02423008, -0.09363701, -0.47808649, 0.78503518, 0.6107662, -0.14265541, 0.32685365],
        [-0.29564348, 0.01047315, -0.17783736, -0.49603321, 0.7066799, 0.58419713, -0.07674099],
        [0.14203233, -0.04402793, 0.07981365, -0.05536073, -0.44115166, 0.80543347, 0.74784479],
        [-0.56358893, -0.07167133, -0.26232202, -0.07291363, -0.24073814, -0.58861456, 0.77074485],
    ]
)


def phi_sign(v: np.ndarray) -> float:
    value = np.dot(D @ v, KER)
    return float(np.sign(value))


def phi_and(a: np.ndarray, b: np.ndarray) -> float:
    return phi_sign(a * b)


def phi_or(a: np.ndarray, b: np.ndarray) -> float:
    return phi_sign(a + b)


def phi_not(a: np.ndarray) -> float:
    return phi_sign(-a)


def phi_xor(a: np.ndarray, b: np.ndarray) -> float:
    return phi_sign(a - b)


def phi_nand(a: np.ndarray, b: np.ndarray) -> float:
    return -phi_and(a, b)
