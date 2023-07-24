# circleci-webhook-manager

[![Validation Workflow](https://github.com/mbeacom/circleci-webhook-manager/actions/workflows/validate.yaml/badge.svg?branch=main&event=push)](https://github.com/mbeacom/circleci-webhook-manager/actions/workflows/validate.yaml)
[![Pre-Commit Checks Workflow](https://github.com/mbeacom/circleci-webhook-manager/actions/workflows/pre-commit.yaml/badge.svg?branch=main&event=push)](https://github.com/mbeacom/circleci-webhook-manager/actions/workflows/pre-commit.yaml)
[![Coverage Status](https://codecov.io/github/mbeacom/circleci-webhook-manager/coverage.svg?branch=main)](https://codecov.io/github/mbeacom/circleci-webhook-manager?branch=main)
[![PyPi](https://img.shields.io/pypi/v/circleci-webhook-manager)](https://pypi.org/project/circleci-webhook-manager/)

This project aims to provide a simple way to manage CircleCI webhooks.
It aims to provide a way to manage webhooks for multiple projects (e.g., organization-wide).

This project is not affiliated with CircleCI and is not an official CircleCI project.
But it is an open-source project that is free to use and modify.

Work in process, YMMV...

## Usage

This project uses:

- [poetry](https://python-poetry.org/) for dependency management and packaging.
- [poethepoet](https://poethepoet.natn.io/) for task running.
- [pytest](https://docs.pytest.org/en/stable/) for testing.
- [black](https://black.readthedocs.io/en/stable/) for auto-formatting.
- [mypy](https://mypy.readthedocs.io/en/stable/) for static type checking.
- [pre-commit](https://pre-commit.com/) for git hooks.
- [ruff](https://beta.ruff.rs/docs/) for linting.
- [mkdocs](https://www.mkdocs.org/) for documentation.

Ensure you have installed the relevant dependencies before continuing.

### Install dependencies

```bash
poetry install
```

### Run tests

```bash
poetry poe test
# or: poetry run poe test
```
