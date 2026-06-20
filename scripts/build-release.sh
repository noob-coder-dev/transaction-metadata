#!/usr/bin/env bash
set -euo pipefail

rm -rf dist build

python - <<'PY'
from pathlib import Path
from transaction_metadata.version import __version__

readme = Path('README.md')
text = readme.read_text(encoding='utf-8')
text = text.replace('Latest Version: `__version__`', f'Latest Version: `{__version__}`')
text = text.replace(
    'Please refer to: https://pypi.org/project/transaction-metadata/__version__/',
    f'Please refer to: https://pypi.org/project/transaction-metadata/{__version__}/'
)
readme.write_text(text, encoding='utf-8')
print(f'Updated README.md with version {__version__}')
PY

python -m build
python -m twine upload dist/*
