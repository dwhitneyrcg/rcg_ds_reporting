# MDM Merge Recommendation Engine

A merge recommendation engine for Master Data Management, executed on Databricks via Databricks Connect.

## Setup

### Install dependencies

```bash
pip install -e ".[dev]"
```

### Configure Databricks Connect

Update your Databricks connection in `.databricks/config` or via environment variables for your workspace.

## Running locally

```bash
# Dev (default)
python -m mdm_merge_recommendation_engine.main

# QA
ENV=qa python -m mdm_merge_recommendation_engine.main

# Prod
ENV=prod python -m mdm_merge_recommendation_engine.main
```

## Environment configuration

- **dev**: Development cluster (2 workers, DEBUG logging)
- **qa**: QA cluster (4 workers, INFO logging)
- **prod**: Production cluster (8 workers, WARNING logging)

Edit `config/{dev,qa,prod}.yaml` to update cluster and workspace settings.

## Development

Format and lint code:

```bash
black src/
ruff check src/
```

Run tests:

```bash
pytest tests/
```
