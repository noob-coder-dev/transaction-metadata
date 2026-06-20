# Transaction Metadata

`transaction-metadata` is a small Python package that exposes versioned Avro schemas for transaction and user data. It is useful for data pipelines and applications that need a reliable way to fetch schema definitions at runtime.

## Latest Version

Latest Version: `1.0.3`

Please refer to: https://pypi.org/project/transaction-metadata/1.0.3/

## Installation

Install from PyPI:

```bash
pip install transaction-metadata
```

Or, if you are using a virtual environment:

```bash
python -m pip install transaction-metadata
```

## Package Structure

```text
transaction_metadata/
├── schemas/
│   ├── transaction/v1/transaction.avsc
│   └── user/v1/user.avsc
├── loader.py
└── version.py
```

## Usage

### Get a schema for a specific entity

```python
from transaction_metadata.loader import get_schema

schema = get_schema(entity="transaction", version="v1")
print(schema)
```

### Get the schema for a user entity

```python
from transaction_metadata.loader import get_schema

user_schema = get_schema(entity="user", version="v1")
print(user_schema)
```

### Example: inspect a few fields

```python
from transaction_metadata.loader import get_schema

schema = get_schema(entity="transaction", version="v1")
for field in schema.get("fields", []):
    print(field["name"], field.get("type"))
```

## PyPI Package

The package is published on PyPI here:

https://pypi.org/project/transaction-metadata/

## Notes

- The public API exposed by this package is `get_schema(entity, version)`.
- The schema files are stored under the package resources so they can be loaded safely at runtime.
