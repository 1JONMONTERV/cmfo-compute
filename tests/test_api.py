import cmfo_compute as cmfo


def test_api_operations():
    x = cmfo.tensor([1, 2, 3, 4, 5, 6, 7])
    y = cmfo.evolve([1, 2, 3, 4, 5, 6, 7], 1)

    assert len(x.v) == 7
    assert len(y.v) == 7

    assert cmfo.phi_and(1, 1) == 1.0
    assert cmfo.phi_not(1) == -1.0
