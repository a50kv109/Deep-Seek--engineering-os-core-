# E-OS Core V2.20 (TOOLKIT EDITION)

Minimal local scaffold for E-OS Core with runtime/event primitives,
navigation adapters, patterns, and CI-ready tests.

Engineering Operating System Core: clean kernel with SOL (ontological primitives),
ISA (type system), EIR (engineering graph), and EEL (exchange language).

## Quick Start

```bash
python -m venv venv
source venv/bin/activate
pip install -e .[pdf,vision,dev]
pytest
```

## Structure

- `src/core`: SOL/ISA/EIR/EEL primitives
- `src/runtime`: engine, validator, handler
- `src/domain`: builder and lifecycle
- `src/nav`: navigation adapters
- `tests`: pytest test suite
- `patterns`: YAML pattern definitions
