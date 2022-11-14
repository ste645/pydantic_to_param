"""Pydantic converters."""

import inspect
from jinja2 import Environment, PackageLoader, select_autoescape
from pydantic import BaseModel
from typing import List, Dict

class TableForMap(BaseModel):
    name: str
    data: List[Dict]

class RustConverterHashMap:
    """Pydantic Converter."""

    def convert_to_hashmap(self, cls):
        """Convert the json file and dataclass to hashmap."""
        env = Environment(
            loader=PackageLoader(package_name="porter.convertors"),
            autoescape=select_autoescape(),
        )
        template = env.get_template("rust_map_template.tmpl")
        return template.render(
            cls=cls, inspect=inspect, isinstance=isinstance, type=type, str=str
        )

