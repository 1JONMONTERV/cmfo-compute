"""
Operador Γφ: rotación fractal sobre R7
"""

import numpy as np


def gamma_step(v: np.ndarray) -> np.ndarray:
    g = np.array(
        [
            [0, 1, 0, 0, 0, 0, 0],
            [-1, 0, 0, 0, 0, 0, 0],
            [0, 0,  1, 0, 0, 0, 0],
            [0, 0, 0,  1, 0, 0, 0],
            [0, 0, 0, 0,  1, 0, 0],
            [0, 0, 0, 0, 0,  1, 0],
            [0, 0, 0, 0, 0, 0,  1],
        ],
        dtype=float,
    )
    return g @ v
