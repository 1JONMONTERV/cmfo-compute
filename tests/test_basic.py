import cmfo_compute as cmfo

def test_tensor_creation():
    t = cmfo.tensor([1,2,3,4,5,6,7])
    assert t.v[0] == 1

def test_norm_phi():
    t = cmfo.tensor([1,2,3,4,5,6,7])
    n = t.norm()
    assert n > 0
