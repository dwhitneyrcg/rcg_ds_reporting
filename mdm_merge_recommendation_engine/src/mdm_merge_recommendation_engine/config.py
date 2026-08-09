import os
from pathlib import Path
from dataclasses import dataclass

import yaml


@dataclass
class Config:
    environment: str
    cluster_id: str
    workspace_url: str
    num_workers: int
    log_level: str


def load_config(env: str = None) -> Config:
    env = env or os.getenv("ENV", "dev")
    config_path = Path(__file__).parent.parent.parent / "config" / f"{env}.yaml"

    if not config_path.exists():
        raise FileNotFoundError(f"Config file not found: {config_path}")

    with open(config_path) as f:
        data = yaml.safe_load(f)

    return Config(**data)
