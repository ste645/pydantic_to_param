"""Some example usage."""

import pydantic
import typing
from porter.convertors.convertor_rust import TableForMap, RustConverterHashMap
import json


json_file = "underlyings_map.json"

with open(json_file) as f:
    json_blob = json.load(f)

table = TableForMap(
    name="underlyings_tickers",
    data=json_blob,
    rust_template = "rust_map_template.tmpl"
)

if __name__ == "__main__":
    conv = RustConverterHashMap()
    rendered_template = conv.convert_to_hashmap(cls=table)
    with open(f"{table.name.lower()}_generated_rust_map.rs", "w") as f:
        f.write(rendered_template)
