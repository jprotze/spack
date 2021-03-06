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
from itertools import product
from spack.util.executable import which

# Supported archvie extensions.
PRE_EXTS = ["tar"]
EXTS     = ["gz", "bz2", "xz", "Z", "zip", "tgz"]

# Add EXTS last so that .tar.gz is matched *before* tar.gz
ALLOWED_ARCHIVE_TYPES = [".".join(l) for l in product(PRE_EXTS, EXTS)] + EXTS


def allowed_archive(path):
    return any(path.endswith(t) for t in ALLOWED_ARCHIVE_TYPES)


def decompressor_for(path):
    """Get the appropriate decompressor for a path."""
    tar = which('tar', required=True)
    tar.add_default_arg('-xf')
    return tar
