# Coding Style

Version: 0.1.0

---

# Philosophy

Readable code is preferred over clever code.

Consistency is more important than personal preference.

Code should communicate intent clearly.

---

# Python Version

Python 3.12+

---

# Naming Convention

## Classes

PascalCase

Examples

```python
class FileOrganizer:

class BackupManager:

class ExportService:
```

---

## Functions

snake_case

```python
def organize_files():

def export_data():

def create_backup():
```

---

## Variables

snake_case

```python
source_folder

output_directory

selected_files
```

---

## Constants

UPPER_CASE

```python
APP_NAME

DEFAULT_THEME

MAX_FILE_SIZE
```

---

## Modules

snake_case

```
file_system.py

logger.py

theme.py
```

---

## Folders

kebab-case

```
invoice-automation/

backup-utility/

excel-processor/
```

---

# Imports

Standard Library

↓

Third Party

↓

Internal Modules

Example

```python
import json
from pathlib import Path

import pandas as pd

from shared.logging.logger import Logger
```

---

# Quotes

Use double quotes by default.

```python
name = "Automation Suite"
```

Use single quotes only when it improves readability.

```python
"It's finished."
```

---

# Line Length

Maximum

100 characters

---

# Functions

Functions should perform one responsibility.

Avoid extremely long functions.

Prefer decomposition.

---

# Classes

Classes should model one responsibility.

Avoid "God Objects."

---

# Comments

Write comments to explain "why."

Avoid explaining obvious code.

Good

```python
# Prevent accidental overwrite of existing files.
```

Avoid

```python
# Increment i.
```

---

# Error Handling

Expected errors should be handled gracefully.

Unexpected errors should be logged.

Applications should avoid crashing silently.

---

# Logging

Do not use print() for application logging.

Use the shared logging module.

---

# Configuration

Avoid hardcoded values.

Configuration belongs inside the config module.

---

# File Paths

Prefer pathlib over os.path.

Example

```python
from pathlib import Path
```

---

# Type Hints

Use type hints whenever practical.

Example

```python
def export_csv(path: Path) -> bool:
```

---

# Docstrings

Public classes and functions should include docstrings.

Example

```python
def organize_files() -> None:
    """Organize files into predefined categories."""
```

---

# Formatting

Use Black-compatible formatting whenever possible.

Avoid manual alignment.

---

# Future Improvements

- Ruff
- Black
- mypy
- pytest
- pre-commit

---

# Coding Philosophy

Simple.

Predictable.

Maintainable.

Readable.

Reusable.