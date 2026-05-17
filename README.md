# base-python-data-science

A multi-language data science monorepo for learning and reuse.

This repository serves two purposes:

1. **Learning platform**: understand core data science ideas by implementing them directly.
2. **Engineering platform**: reuse the libraries, APIs, specs, containers, and deployment assets in real projects.

The project started from the ideas in *Data Science from Scratch* and has grown into a monorepo with Python, Node.js, C++, and Rust components.

## Who this repository is for

### Users (learners and integrators)
Use this repo if you want to:
- study data science algorithms without heavy abstractions
- run examples locally
- call algorithms through REST, AMQP, or MQTT interfaces

### Developers (contributors and extenders)
Use this repo if you want to:
- add algorithms or examples
- extend APIs and generated clients/servers
- maintain multi-language ports

### Administrators / Operators
Use this repo if you want to:
- build and run containerized services
- deploy Node REST components with Helm
- understand CI/CD and release flow

## Monorepo layout

Top-level directories:

| Path | Purpose |
| --- | --- |
| `src/` | All implementation modules and services |
| `docs/` | Documentation site content and posts |
| `.github/workflows/` | CI/CD workflows |
| `data/` | Input/reference data files |

Key modules inside `src/`:

| Module | Type | Notes |
| --- | --- | --- |
| `data-scratch-library` | Python package (`dsl`) | Core data science algorithms from scratch |
| `data-scratch-matplotlib` | Python package | Visualization examples |
| `data-scratch-scrape` | Python package | Data collection and scraping examples |
| `data-scratch-amqp` | Python service | AMQP strategy execution service |
| `data-scratch-mqtt` | Python service | MQTT strategy execution service |
| `data-scratch-node-library` | Node/TypeScript library | JavaScript/TypeScript implementations |
| `data-scratch-cpp-library` | C++ library | C++ implementations and tests |
| `rest-scratch-flask` | Python REST API | Flask implementation + OpenAPI docs |
| `rest-scratch-node-express` | OpenAPI-driven Node REST server | Includes Helm chart and Docker assets |
| `rest-scratch-pistache` | OpenAPI-driven C++ REST server | Generator-based workflow |
| `rest-scratch-rust` | OpenAPI-driven Rust REST server | Generator-based workflow |
| `rest-client-ts-node` | OpenAPI-driven TypeScript client | Generated client workflow |

## Quick start (new to this repo)

### 1) Clone and install base dependencies

```bash
git clone https://github.com/wilsonify/base-python-data-science.git
cd base-python-data-science
python -m pip install -r test-requirements.txt
python -m pip install -r requirements.txt
```

### 2) Install the core library in editable mode

```bash
python -m pip install -e src/data-scratch-library
```

### 3) Run the core test suite

```bash
cd src/data-scratch-library
python -m pytest tests/ --cov=dsl --cov-report=term-missing --cov-report=html --cov-branch --cov-fail-under=90
```

### 4) Try the Python package

```bash
python -c "from dsl.c05_statistics.e0501_central_tendancy import mean; print(mean([1,2,3,4]))"
```

## Common workflows

### Run the Flask REST API

```bash
cd src/rest-scratch-flask
python -m pip install -r requirements.txt
python run.py
```

API endpoint: `http://127.0.0.1:5000`

Useful docs:
- `src/rest-scratch-flask/README.md`
- `src/rest-scratch-flask/OPENAPI_SUMMARY.md`
- `src/rest-scratch-flask/OPENAPI_GUIDE.md`

### Run the MQTT strategy service

```bash
cd src/data-scratch-mqtt
python -m pip install -r requirements.txt
python -m pip install -e ../data-scratch-library
python -m pip install -e .
python -m data_scratch_mqtt
```

### Run the AMQP strategy service

```bash
cd src/data-scratch-amqp
python -m pip install -r requirements.txt
python -m pip install -e ../data-scratch-library
python -m pip install -e .
python -m data_scratch_amqp
```

### Generate OpenAPI-based artifacts

Each OpenAPI module contains `openapi/openapi.yaml` and a generator script.

Examples:

```bash
cd src/rest-client-ts-node && ./generate.sh
cd src/rest-scratch-node-express && ./generate.sh
cd src/rest-scratch-rust && ./generate.sh
cd src/rest-scratch-pistache && ./generate.sh
```

> Generated folders are intentionally not committed in this repository. Regenerate them locally as needed.

## Developer guide

### How to add work safely

1. Identify the target module in `src/`.
2. Read that module's local README (if present).
3. Install dependencies for that module.
4. Run tests for that module before and after your change.
5. If your change affects OpenAPI, regenerate the related artifacts.

### Build orchestration script

A repository-level build pipeline exists:

```bash
python build.py --help
```

It builds the shared library first, then dependent services in sequence.

## Operator guide

### Docker assets

- Root `Dockerfile` builds a runtime image with the core `dsl` package installed.
- Several modules include dedicated Dockerfiles (base/builder/run patterns in some services).

### Helm chart

A Helm chart is available for the Node Express REST service:

- `src/rest-scratch-node-express/chart/node/Chart.yaml`
- `src/rest-scratch-node-express/chart/node/values.yaml`

### CI/CD workflow

Main workflow:
- `.github/workflows/ci-cd.yaml`

Current pipeline responsibilities:
- build and smoke-test container image
- run SonarQube scan and quality gate
- publish tagged images to GHCR on release tags

## Documentation map

- Monorepo landing page: `README.md` (this file)
- Docs site home: `docs/index.md`
- Project docs specification: `docs/spec.md`
- Module-level docs: `src/**/README.md`
- Educational posts/content: `docs/content/post/`

## Philosophy

When contributing documentation and code in this repository:

- Prefer explainability over brevity.
- Prefer explicit instructions over clever shortcuts.
- Assume readers are technically capable but unfamiliar with this structure.
- Treat this repository as both a learning platform and a reusable engineering platform.
