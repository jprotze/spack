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
import argparse

import spack.cmd
import spack.packages as packages


description="Expand downloaded archive in preparation for install"

def setup_parser(subparser):
    subparser.add_argument(
        '-n', '--no-checksum', action='store_true', dest='no_checksum',
        help="Do not check packages against checksum")
    subparser.add_argument(
        'packages', nargs=argparse.REMAINDER, help="specs of packages to stage")


def stage(parser, args):
    if not args.packages:
        tty.die("stage requires at least one package argument")

    if args.no_checksum:
        spack.do_checksum = False

    specs = spack.cmd.parse_specs(args.packages, concretize=True)
    for spec in specs:
        package = packages.get(spec)
        package.do_stage()
