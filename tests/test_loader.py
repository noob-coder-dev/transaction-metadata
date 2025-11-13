import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from transaction_metadata.loader import get_schema

def test_get_schema():
    schema = get_schema("transaction", "v1")
    assert schema["name"] == "Transaction"
    assert any(f["name"] == "transaction_id" for f in schema["fields"])