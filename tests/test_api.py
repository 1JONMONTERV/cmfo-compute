import cmfo_compute as cmfo


def test_tensor_and_evolve():
    x = cmfo.tensor([1, 2, 3, 4, 5, 6, 7])
    assert x.v[0] == 1

    y = cmfo.evolve([1, 2, 3, 4, 5, 6, 7], 5)
    assert isinstance(y.v[0], float)

    a = [1, -1, 2]
    b = [-1, 1, -2]

    print("phi_and:", cmfo.phi_and(a, b))
    print("phi_or:", cmfo.phi_or(a, b))
    print("phi_not:", cmfo.phi_not(a))
    print("phi_xor:", cmfo.phi_xor(a, b))
    print("phi_nand:", cmfo.phi_nand(a, b))
