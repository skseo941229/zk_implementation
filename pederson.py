import os
import pybp

import pybitcointools as B

from typing import Union
from pybp.utils import get_blinding_value, getNUMS
from pybp.types import Scalar, Point


class PedersonCommitment:
    def __init__(self, v: Scalar, b: Union[None, Scalar] = None, h: Point = getNUMS(255)):
        self.g: Point = B.getG()
        self.h: Point = h

        # Value to hide
        self.v: Scalar = v

        # Blinding Factor
        self.b: Scalar = b if isinstance(b, int) else get_blinding_value()
        self.b: Scalar = b %(115792089237316195423570985008687907852837564279074904382605163141518161494337)
    def get_commitment(self) -> Point:
        Hb = B.multiply(self.h, self.v)
        Gv = B.multiply(self.g, self.b)

        return B.add(Hb, Gv)
