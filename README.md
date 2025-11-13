# Transaction Metadata

This package provides versioned Avro schemas and configuration utilities 
for simulated transaction and user data used in streaming pipelines 
(Flink + Snowflake + Kafka).

### Structure
```
transaction_metadata/
├── schemas/
│   ├── transaction/v1/transaction.avsc
│   └── user/v1/user.avsc
├── loader.py
└── version.py
```

### Usage

```python
from transaction_metadata.loader import get_schema
schema = get_schema(entity="transaction", version="v1")
print(schema)
```