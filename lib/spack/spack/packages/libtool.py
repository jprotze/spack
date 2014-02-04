from spack import *

class Libtool(Package):
    """GNU libtool is a generic library support script. Libtool hides the
       complexity of using shared libraries behind a consistent,
       portable interface.
    """
    homepage = "http://www.gnu.org/software/libtool/"
    url      = "file:///Users/gamblin2/spack-mirror/libtool/libtool-2.4.2.tar.gz"

    versions = { '2.4.2' : 'd2f3b7d4627e69e13514a40e72a24d50', }

    depends_on('autoconf')
    depends_on('automake')

    def install(self, spec, prefix):
        configure("--prefix=%s" % prefix)
        make()
        make("install")
