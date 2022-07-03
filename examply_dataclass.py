"""Some example usage."""

import pydantic
import typing
from porter.convertors.convertor_dataclass import PydanticConverterDataClass


class Something(pydantic.BaseModel):
    """Something."""

    data: int
    list_of_data: typing.List[int]


if __name__ == "__main__":
    conv = PydanticConverterDataClass()
    rendered_template = conv.convert_to_dataclass(cls=Something)
    with open(f"{Something.__name__.lower()}_generated_dataclass.py", "w") as f:
        f.write(rendered_template)
