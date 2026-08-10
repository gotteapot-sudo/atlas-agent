# Atlas

Atlas is intended to become a system for discovering, evaluating, and prioritizing opportunities for AI automation and digital products.

This repository currently contains only the initial technical foundation for the project. It intentionally avoids application features, external services, databases, web frameworks, LLM integrations, Docker, frontend code, and other architecture that is not needed for the bootstrap stage.

## Development setup

Create and activate a virtual environment, then install the project with its development dependencies:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -e '.[dev]'
```

## Running tests

Run the test suite with:

```bash
pytest
```
