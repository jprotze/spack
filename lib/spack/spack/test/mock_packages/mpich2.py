##############################################################################
# Copyright (c) 2013, Lawrence Livermore National Security, LLC.
# Produced at the Lawrence Livermore National Laboratory.
#
# This file is part of Spack.
# Written by Todd Gamblin, tgamblin@llnl.gov, All rights reserved.
# LLNL-CODE-647188
#
# For details, see https://scalability-llnl.github.io/spack
# Please also see the LICENSE file for our notice and the LGPL.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License (as published by
# the Free Software Foundation) version 2.1 dated February 1999.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the IMPLIED WARRANTY OF
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the terms and
# conditions of the GNU General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program; if not, write to the Free Software Foundation,
# Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
##############################################################################
from spack import *

class Mpich2(Package):
    homepage   = "http://www.mpich.org"
    url        = "http://www.mpich.org/static/downloads/1.5/mpich2-1.5.tar.gz"
    list_url   = "http://www.mpich.org/static/downloads/"
    list_depth = 2

    versions = { '1.5' : '9c5d5d4fe1e17dd12153f40bc5b6dbc0',
                 '1.4' : 'foobarbaz',
                 '1.3' : 'foobarbaz',
                 '1.2' : 'foobarbaz',
                 '1.1' : 'foobarbaz',
                 '1.0' : 'foobarbaz' }

    provides('mpi@:2.0')
    provides('mpi@:2.1', when='@1.1:')
    provides('mpi@:2.2', when='@1.2:')

    def install(self, spec, prefix):
        configure("--prefix=%s" % prefix)
        make()
        make("install")
