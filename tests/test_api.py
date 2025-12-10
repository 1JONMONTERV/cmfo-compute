import cmfo_compute as cmfo

x = cmfo.tensor([1,2,3,4,5,6,7])
print("Tensor creado:", x)

y = cmfo.evolve([1,2,3,4,5,6,7], 5)
print("Evolución:", y)

a, b = 1, -1
print("phi_and:", cmfo.phi_and(a,b))
print("phi_or :", cmfo.phi_or(a,b))
print("phi_xor:", cmfo.phi_xor(a,b))
print("phi_not:", cmfo.phi_not(a))
print("phi_nand:", cmfo.phi_nand(a,b))
