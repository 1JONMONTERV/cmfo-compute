def phi_sign(x):
    x = float(x)
    return 1.0 if x >= 0 else -1.0

def phi_and(a, b):
    return phi_sign(a) * phi_sign(b)

def phi_or(a, b):
    return phi_sign(a + b)

def phi_not(a):
    return -phi_sign(a)

def phi_xor(a, b):
    return phi_sign(a) * -phi_sign(b)

def phi_nand(a, b):
    return -phi_and(a, b)

