from mdcode.example.md import calcenergy

def test_calcenergy():
    # Use Asap for a huge performance increase if it is installed
    use_asap = True

    if use_asap:
        from asap3 import EMT
        size = 10
    else:
        from ase.calculators.emt import EMT
        size = 3

    from ase.lattice.cubic import FaceCenteredCubic
    from ase.md.velocitydistribution import MaxwellBoltzmannDistribution

    atoms = FaceCenteredCubic(directions=[[1, 0, 0], [0, 1, 0], [0, 0, 1]],
                      symbol="Cu",
                      size=(size, size, size),
                      pbc=True)
    atoms.calc = EMT()
    MaxwellBoltzmannDistribution(atoms, temperature_K=300)

    res = calcenergy(atoms)
    assert abs((res[0] + res[1] - res[3])/(res[0] + res[1])) < 1e-3
