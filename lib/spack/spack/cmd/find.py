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
import collections
import argparse
from StringIO import StringIO

import spack
import spack.spec
import spack.packages as packages
import spack.colify
from spack.color import *
from spack.colify import colify

description ="Find installed spack packages"

def setup_parser(subparser):
    subparser.add_argument(
        '-p', '--paths', action='store_true', dest='paths',
        help='Show paths to package install directories')
    subparser.add_argument(
        '-l', '--long', action='store_true', dest='full_specs',
        help='Show full-length specs of installed packages')
    subparser.add_argument(
        'query_specs', nargs=argparse.REMAINDER,
        help='optional specs to filter results')


# TODO: move this and colify to tty.
def hline(label, char, color=''):
    max_width = 64
    cols, rows = spack.colify.get_terminal_size()
    if not cols:
        cols = max_width
    else:
        cols -= 2
    cols = min(max_width, cols)

    label = str(label)
    prefix = char * 2 + " " + label + " "
    suffix = (cols - len(prefix)) * char

    out = StringIO()
    if color:
        prefix = char * 2 + " " + color + cescape(label) + "@. "
        cwrite(prefix, stream=out, color=True)
    else:
        out.write(prefix)
    out.write(suffix)

    return out.getvalue()


def find(parser, args):
    def hasher():
        return collections.defaultdict(hasher)

    query_specs = []
    if args.query_specs:
        query_specs = spack.cmd.parse_specs(args.query_specs, normalize=True)

    # Make a dict with specs keyed by architecture and compiler.
    index = hasher()
    for spec in packages.installed_package_specs():
        if query_specs and not any(spec.satisfies(q) for q in query_specs):
            continue

        if spec.compiler not in index[spec.architecture]:
            index[spec.architecture][spec.compiler] = []
        index[spec.architecture][spec.compiler].append(spec)

    # Traverse the index and print out each package
    for architecture in index:
        print hline(architecture, "=", spack.spec.architecture_color)
        for compiler in index[architecture]:
            print hline(compiler, "-", spack.spec.compiler_color)

            specs = index[architecture][compiler]
            specs.sort()

            abbreviated = [s.format('$_$@$+$#', color=True) for s in specs]

            if args.paths:
                # Print one spec per line along with prefix path
                width = max(len(s) for s in abbreviated)
                width += 2
                format = "    %-{}s%s".format(width)

                for abbrv, spec in zip(abbreviated, specs):
                    print format % (abbrv, spec.package.prefix)

            elif args.full_specs:
                for spec in specs:
                    print spec.tree(indent=4, format='$_$@$+', color=True),
            else:
                for abbrv in abbreviated:
                    print "    %s" % abbrv
