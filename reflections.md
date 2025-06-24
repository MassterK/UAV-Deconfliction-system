# Reflection & Justification Document

## Design Decisions and Architectural Choices

This project was structured with modularity, clarity, and extensibility in mind. The codebase is split into distinct files based on their responsibilities:

- `main.py` acts as the entry point, responsible for I/O and invoking all logic.
- `interface.py` provides a clean abstraction over the checking system.
- `conflict_checker.py` handles core spatial and temporal conflict logic.
- `flight_schedule_loader.py` simulates external drone schedules.
- `utils.py` provides shared utilities like Euclidean distance and path interpolation.
- `visualizer.py` handles both 2D and 4D (3D space + time) plotting.

This separation ensures testability and future adaptability-for example, we can swap out static loading with real-time data ingestion with minimal disruption.

## Spatial and Temporal Conflict Implementation

**Spatial Check**:
- Each drone path is interpolated between waypoints to create dense coordinate samples.
- At each sampled time step, Euclidean distance between the primary and other drones' positions is compared against a safety buffer (default: 5 meters).

**Temporal Check**:
- Each interpolated point includes a time value.
- Conflict is flagged only if the distance check passes **and** the timestamps between the drones are within a ±1 second window.

This effectively captures both instantaneous and near-miss collisions during overlapping flight schedules.

## Use of AI-Assisted Tools

- **ChatGPT**: Used extensively for iterative code development, modular refactoring, and debugging logic.
- **Cursor AI**: Used as a VS Code assistant to improve syntax, catch unused imports, and apply docstring suggestions.

AI was not used to blindly generate code but to accelerate development by assisting with decisions, debugging, formatting, and corner-case thinking.

## Testing Strategy and Edge Cases

### Testing Strategy:
- Manual test cases were executed using controlled drone paths and time windows.
- Conflict edge cases like:
  - Same location but different times (no conflict)
  - Close proximity but outside time window (no conflict)
  - Overlapping space and time (should raise conflict)

### Edge Cases Considered:
- Duplicates in detected conflict points (resolved via key hashing in visualizer).
- Minimum path density for time-aligned comparisons (solved by `steps=20`).
- Conflict labeling clutter (handled by deduplication logic and optional time rounding).

Though unit tests aren't included in code, the structure supports future test harness development using `unittest` or `pytest`.

## Scalability for Real-World Deployment

To handle **tens of thousands of drones** in a real-world scenario, the following upgrades would be essential:

### 1. Real-time Data Ingestion
- Replace hardcoded flight paths with Kafka, MQTT, or REST-based ingestion from fleet telemetry systems.

### 2. Parallel Conflict Checking
- Use distributed task queues (e.g., Celery, Dask, or Ray) to parallelize conflict detection.
- Partition airspace into grids using spatial indexing (e.g., KD-trees, R-trees) to reduce computation scope.

### 3. Temporal Binning
- Assign drones to time buckets to avoid comparing all combinations unnecessarily.

### 4. Fault Tolerance & Monitoring
- Deploy microservices on Kubernetes with circuit breakers, logging, and retry logic.
- Integrate Prometheus/Grafana for real-time monitoring of drone conflict rates.

### 5. Visualization at Scale
- For live dashboards, switch from Matplotlib to Plotly Dash or WebGL-based systems to render 3D + time with WebSocket support.

## Summary

This project successfully meets the assesment requirements using a clean, modular Python implementation. It clearly demonstrates spatial-temporal deconfliction logic, conflict explanations, and both 2D and 4D visualization. The architecture is scalable, adaptable, and backed by thoughtful design choices.