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
"""
This file contains utilities to help with installing packages.
"""
from spack.util.filesystem import new_path

class Prefix(str):
    """This class represents an installation prefix, but provides useful
       attributes for referring to directories inside the prefix.

       For example, you can do something like this::

           prefix = Prefix('/usr')
           print prefix.lib
           print prefix.lib64
           print prefix.bin
           print prefix.share
           print prefix.man4

       This program would print:

           /usr/lib
           /usr/lib64
           /usr/bin
           /usr/share
           /usr/share/man/man4

       Prefix objects behave identically to strings.  In fact, they
       subclass str.  So operators like + are legal:

           print "foobar " + prefix

       This prints 'foobar /usr". All of this is meant to make custom
       installs easy.
    """

    def __new__(cls, path):
        s = super(Prefix, cls).__new__(cls, path)
        s.bin     = new_path(s, 'bin')
        s.sbin    = new_path(s, 'sbin')
        s.etc     = new_path(s, 'etc')
        s.include = new_path(s, 'include')
        s.lib     = new_path(s, 'lib')
        s.lib64   = new_path(s, 'lib64')
        s.libexec = new_path(s, 'libexec')
        s.share   = new_path(s, 'share')
        s.doc     = new_path(s.share, 'doc')
        s.info    = new_path(s.share, 'info')
        s.man     = new_path(s.share, 'man')
        s.man1    = new_path(s.man, 'man1')
        s.man2    = new_path(s.man, 'man2')
        s.man3    = new_path(s.man, 'man3')
        s.man4    = new_path(s.man, 'man4')
        s.man5    = new_path(s.man, 'man5')
        s.man6    = new_path(s.man, 'man6')
        s.man7    = new_path(s.man, 'man7')
        s.man8    = new_path(s.man, 'man8')
        return s
