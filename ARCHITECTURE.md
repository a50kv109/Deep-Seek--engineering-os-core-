# E-OS Core V2.20 Architecture

Core layers:

- `src/core`: primitives (`SOL`, `ISA`, `EIR`, `EEL`)
- `src/runtime`: event validation and processing
- `src/domain`: domain model and lifecycle
- `src/nav`: navigation adapters

The runtime receives `EIR` events, validates them, and routes to the engine.
