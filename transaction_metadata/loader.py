import json
from importlib import resources
from typing import cast

def get_schema(entity: str, version: str = "v1") -> dict:
    """
    Loads the Avro schema for the specified entity and version.
    Example: get_schema("transaction", "v1")
    """
    try:
        # Guarantee a `str` package to satisfy type-checkers (mypy/pylance)
        pkg = cast(str, __package__ or __name__)
        schema_path = f"schemas/{entity}/{version}/{entity}.avsc"
        with resources.files(pkg).joinpath(schema_path).open("r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        raise FileNotFoundError(f"Schema not found for entity '{entity}' version '{version}'")
