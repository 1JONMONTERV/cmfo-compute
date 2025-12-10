import cmfo_compute as cmfo


def test_tensor_creation():
    t = cmfo.tensor([1, 2, 3, 4, 5, 6, 7])
    assert t.v[0] == 1


def test_evolution():
    t = cmfo.tensor([1, 1, 1, 1, 1, 1, 1])
    y = t.evolve(1)
    assert len(y.v) == 7
