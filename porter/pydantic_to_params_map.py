import param
from enum import Enum
import datetime


class SIMPLE_CONVERSIONS(Enum):
    string = "String"
    str = "String"
    int = "Integer"
    integer = "Integer"
    bool = "Boolean"
    boolean = "Boolean"
    float = "Number"
    number = "Number"


class FORMATED_CONVERSION(Enum):
    date = "Date"


class NESTED_CONVERSION(Enum):
    List = "List"
    array = "List"
    tuple = "Tuple"


class PYDANTIC_TO_PARAM_UNIVERSE(Enum):
    simple = SIMPLE_CONVERSIONS
    formated = FORMATED_CONVERSION
    nested = NESTED_CONVERSION
    package_params = None
