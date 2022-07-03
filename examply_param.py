"""Some example usage."""

import pydantic
import typing
from porter.convertors.convertor_param import PydanticConverterParam
from datetime import date
from typing import List


class Period(pydantic.BaseModel):
    """Period Object"""

    strike: int = None
    trade_date: int = None


class Leg(pydantic.BaseModel):
    """Leg Object"""

    strike: int
    period: List[Period]


class Trade(pydantic.BaseModel):
    """Trade Object."""

    trade_date: date
    strike: float = 2.0
    name: str
    number: int
    legs: List[Leg]
    periods: tuple


if __name__ == "__main__":
    conv = PydanticConverterParam()
    rendered_template = conv.convert_to_param(cls=Trade)
    with open(f"{Trade.__name__.lower()}_generated_paramclass.py", "w") as f:
        f.write(rendered_template)
