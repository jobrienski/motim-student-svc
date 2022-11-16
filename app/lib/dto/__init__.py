# app/lib/dto/__init__.py

from pydantic import ConstrainedFloat, ConstrainedInt


class NonNegativeInt(ConstrainedInt):
    ge = 0


class NonNegativeFloat(ConstrainedFloat):
    ge = 0.0
