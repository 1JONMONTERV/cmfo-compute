import cmfo_compute as cmfo


def test_tensor_creation():
    t = cmfo.tensor([1, 2, 3, 4, 5, 6, 7])
    assert t.v[0] == 1


def test_tensor_evolve():
    y = cmfo.evolve([1, 2, 3, 4, 5, 6, 7], 3)
    assert isinstance(y.v[0], float)
