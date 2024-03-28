"""
Additional tools.

AUTHORS:

- Andreas Pieper 2023 initial implementation

"""

# *****************************************************************************
#       Copyright (C) 2023 Andreas Pieper <andreas.pieper@univ-rennes1.fr>
#
#  Distributed under the terms of the GNU General Public License (GPL)
#  as published by the Free Software Foundation; either version 3 of
#  the License, or (at your option) any later version.
#                  https://www.gnu.org/licenses/
# *****************************************************************************

from sage.algebras.quatalg.quaternion_algebra import QuaternionAlgebraFactory
from sage.misc.constant_function import ConstantFunction
from sage.rings.all import ZZ, Integer, Zmod
from sage.structure.coerce_maps import CallableConvertMap
from sage.structure.richcmp import richcmp_method


@richcmp_method
class SupersingularEndomorphismStructure:
    """
    Constructor for a point on a variety with theta structure.

    INPUT:

    - ``X`` -- a variety with theta structure
    - ``v`` -- data determining a point (another point or a tuple of coordinates)
    """

    def __init__(self, E, B, indep, indepB):
        self.E = E
        self.B = B
        self.indep = indep
        self.indepB = indepB

    def asPoint(E, E1, phi):
        K = E.affine_patch(2).coordinate_ring().fraction_field()
        E1_ = E1.change_ring(K)
        return E1_(
            phi.rational_maps()[0](K.zero(), K.one()),
            phi.rational_maps()[1](K.zero(), K.one()),
        )

    # def Endomorphism(self, r):
    #     return asMap(Str.E, sum(Integers()![x[1][i]] * asPoint(self.indep[i], E_) for i in range(4)))

    def enumerateDeuring(self):
        return
