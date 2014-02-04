from spack import *

class Autoconf(Package):
    """Autoconf is an extensible package of m4 macros that produce shell
       scripts to automatically configure software source code
       packages. These scripts can adapt the packages to many kinds of
       UNIX-like systems without manual user intervention. Autoconf
       creates a configuration script for a package from a template
       file that lists the operating system features that the package
       can use, in the form of m4 macro calls.
    """
    homepage = "http://www.gnu.org/software/autoconf/"
    url      = "file:///Users/gamblin2/spack-mirror/autoconf/autoconf-2.69.tar.xz"

    versions = { '2.69' : '50f97f4159805e374639a73e2636f22e', }

    def install(self, spec, prefix):
        configure("--prefix=%s" % prefix)
        make()
        make("install")
