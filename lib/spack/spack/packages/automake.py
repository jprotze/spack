from spack import *

class Automake(Package):
    """Automake is a tool for automatically generating Makefile.in files
       from files called Makefile.am. Each Makefile.am is basically a
       series of make variable definitions, with rules being thrown in
       occasionally. The generated Makefile.in files are compliant
       with the GNU Makefile standards.
    """
    homepage = "http://www.gnu.org/software/automake/"
    url      = "file:///Users/gamblin2/spack-mirror/automake/automake-1.14.tar.gz"

    versions = { '1.14' : 'a3c0d9298c6112f5f2c26c639ccaaed7', }

    depends_on('autoconf')

    def install(self, spec, prefix):
        configure("--prefix=%s" % prefix)
        make()
        make("install")
