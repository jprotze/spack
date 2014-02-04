from spack import *

class Gperf(Package):
    """Generates a perfect hash function for various input."""
    homepage = "http://www.gnu.org/software/gperf/gperf.html"
    url      = "file:///Users/gamblin2/spack-mirror/gperf/gperf-3.0.4.tar.gz"

    versions = { '3.0.4' : 'c1f1db32fb6598d6a93e6e88796a8632', }

    def install(self, spec, prefix):
        configure("--prefix=%s" % prefix)
        make()
        make("install")
