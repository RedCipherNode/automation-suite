# Automation Suite

A collection of desktop productivity applications built with Python.

The project focuses on solving repetitive daily tasks through standalone desktop applications while sharing reusable components across the suite.

---

## Overview

Automation Suite is designed as a modular collection of desktop applications.

Each application solves a specific problem independently while sharing common infrastructure such as configuration management, logging, utilities, and user interface components.

The goal is to build maintainable software that can evolve without unnecessary duplication.

---

## Applications

| Application | Status | Description |
|-------------|--------|-------------|
| File Organizer | 🚧 | Automatically organize files into categories. |
| Excel Processor | 🚧 | Process, filter, clean, and export Excel or CSV data. |
| Invoice Automation | 🚧 | Generate invoices from structured datasets. |
| Backup Utility | 🚧 | Create local backup jobs with verification and logging. |
| Web Extractor | 🚧 | Extract structured information from websites into CSV or JSON. |

---

## Shared Modules

Shared components reduce duplicated code across applications.

```

shared/
├── config/
├── filesystem/
├── logging/
├── ui/
└── utils/

```

---

## Architecture

```

Desktop UI

↓

Business Logic

↓

Shared Modules

↓

Operating System

↓

Output

```

---

## Technology

- Python
- CustomTkinter
- SQLite (if required)
- OpenPyXL
- Pandas
- Requests
- BeautifulSoup

---

## Design Principles

- Modular architecture
- Separation of concerns
- Reusable components
- Single responsibility
- Consistent user experience
- Minimal external dependencies

---

## Project Structure

```

automation-suite/

apps/
shared/
docs/
assets/

README.md
LICENSE

```

---

## Roadmap

### Phase 1

- Repository setup
- Documentation
- Shared modules
- Design system

### Phase 2

- File Organizer

### Phase 3

- Excel Processor

### Phase 4

- Invoice Automation

### Phase 5

- Backup Utility

### Phase 6

- Web Extractor

---

## License

MIT License
