"""Pydantic converters."""

import inspect
from jinja2 import Environment, PackageLoader, select_autoescape


class PydanticConverterDataClass:
    """Pydantic Converter."""

    def convert_to_dataclass(self, cls):
        """Convert the pydantic serializer to dataclass."""
        env = Environment(
            loader=PackageLoader(package_name="porter.convertors"),
            autoescape=select_autoescape(),
        )
        template = env.get_template("dataclass_template.tmpl")
        return template.render(
            cls=cls, inspect=inspect, isinstance=isinstance, type=type, str=str
        )

    def convert_from_dataclass(self, cls):
        """Convert the serializer from dataclass to a pydantic serialzer."""
