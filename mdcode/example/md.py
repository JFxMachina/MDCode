"""Example that demonstrates molecular dynamics with constant energy."""

from asap3 import Trajectory
from ase.lattice.cubic import FaceCenteredCubic
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase.md.verlet import VelocityVerlet
from ase import units

# Use Asap for a huge performance increase if it is installed
use_asap = True

if use_asap:
    from asap3 import EMT
    size = 10
else:
    from ase.calculators.emt import EMT
    size = 3


def calcenergy(atoms):
    """Calculate the potential, kinetic and total energy per atom."""
    epot = atoms.get_potential_energy() / len(atoms)
    ekin = atoms.get_kinetic_energy() / len(atoms)
    Tinst = ekin / (1.5 * units.kB)
    etot = epot + ekin
    return (epot, ekin, Tinst, etot)


def run_md():
    """Run an example MD simulation for a Cu fcc crystal."""
    # Set up a crystal
    atoms = FaceCenteredCubic(directions=[[1, 0, 0], [0, 1, 0], [0, 0, 1]],
                              symbol="Cu",
                              size=(size, size, size),
                              pbc=True)
    
    # Describe the interatomic interactions with the Effective Medium Theory
    atoms.calc = EMT()
    # Set the momenta corresponding to T=300K
    MaxwellBoltzmannDistribution(atoms, temperature_K=300)
    
    # We want to run MD with constant energy using the VelocityVerlet algorithm.
    dyn = VelocityVerlet(atoms, 5 * units.fs)  # 5 fs time step.
    traj = Trajectory("cu.traj", "w", atoms)
    dyn.attach(traj.write, interval=5)
    
    
    def printenergy(a=atoms):  # store a reference to atoms in the definition.
        """Print the potential, kinetic and total energy per atom."""
        res = calcenergy(a)
        print('Energy per atom: Epot = %.3feV  Ekin = %.3feV (T=%3.0fK)  '
              'Etot = %.3feV' % res)
    
    
    # Now run the dynamics
    dyn.attach(printenergy, interval=10)
    printenergy()
    dyn.run(200)


if __name__ == "__main__":
    run_md()
