from spack import *

class Openmpi(Package):
    """Open MPI is a project combining technologies and resources from
       several other projects (FT-MPI, LA-MPI, LAM/MPI, and PACX-MPI)
       in order to build the best MPI library available.  A completely
       new MPI-2 compliant implementation, Open MPI offers advantages
       for system and software vendors, application developers and
       computer science researchers.
    """
    homepage = "http://www.open-mpi.org"
    url      = "file:///Users/gamblin2/spack-mirror/openmpi/openmpi-1.7.2.tar.bz2"

    versions = { '1.7.2' : 'b897b92100bd13b367e651df483421d5', }

    def install(self, spec, prefix):
        configure("--prefix=%s" % prefix)
        make()
        make("install")
