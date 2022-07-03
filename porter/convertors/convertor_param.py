"""Pydantic converters."""

import inspect
from jinja2 import Environment, PackageLoader, select_autoescape
from porter.pydantic_to_params_map import PYDANTIC_TO_PARAM_UNIVERSE


class PydanticConverterParam:
    """Pydantic Converter."""

    def convert_to_param(self, cls):
        """Convert the pydantic serializer to param class."""
        env = Environment(
            loader=PackageLoader(package_name="porter.convertors"),
            autoescape=select_autoescape(),
        )
        template = env.get_template("params_template.tmpl")
        return template.render(
            schema=cls.schema(),
            inspect=inspect,
            isinstance=isinstance,
            type=type,
            mapping=PYDANTIC_TO_PARAM_UNIVERSE,
        )

    def convert_from_param(self, cls):
        """Convert the serializer from param to a pydantic serialzer."""
        raise NotImplementedError
