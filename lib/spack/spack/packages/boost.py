from spack import *

class Boost(Package):
    """Boost provides free portable peer-reviewed C++ libraries. The
       emphasis is on portable libraries which work well with the C++
       Standard Library.
    """
    # FIXME: add a proper url for your package's homepage here.
    homepage = "http://www.boost.org"
    url      = "file:///Users/gamblin2/spack-mirror/boost/boost_1_54_0.tar.bz2"

    versions = { '1_54_0' : '15cb8c0803064faef0c4ddf5bc5ca279', }

    def install(self, spec, prefix):
        bootstrap = Executable('./bootstrap.sh')
        bootstrap("--prefix=%s" % prefix)

        b2 = Executable('./b2')
        b2()
        b2("install")
