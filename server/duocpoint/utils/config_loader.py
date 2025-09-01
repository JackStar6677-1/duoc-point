"""Helpers to load YAML configuration files.

The project keeps non-sensitive configuration in the top-level
``config/`` directory (feature flags, email senders, push keys, etc.).
This module exposes :func:`load_config` to read those YAML files and
return them as Python dictionaries.

Usage:
    from duocpoint.utils.config_loader import load_config
    app_cfg = load_config("app.yaml")

Files are cached after the first read to avoid hitting disk multiple
times within the same process.
"""

from __future__ import annotations

import yaml
from functools import lru_cache
from pathlib import Path
from typing import Any, Dict

# Locate the repository root and the shared ``config`` directory.
# This file lives at ``server/duocpoint/utils/config_loader.py`` so
# ``parents[2]`` points to ``server/`` and ``parent`` to the repo root.
BASE_DIR = Path(__file__).resolve().parents[2]
CONFIG_DIR = BASE_DIR.parent / "config"


@lru_cache(maxsize=None)
def load_config(name: str) -> Dict[str, Any]:
    """Return the parsed content of a YAML config file.

    Parameters
    ----------
    name:
        Filename of the YAML file relative to ``config/`` (e.g. ``"app.yaml"``).

    Returns
    -------
    dict
        Dictionary with the parsed content. If the file does not exist or is
        empty, an empty dict is returned so callers can safely use ``.get``.
    """

    file_path = CONFIG_DIR / name
    if not file_path.exists():
        return {}

    with file_path.open("r", encoding="utf-8") as fh:
        data = yaml.safe_load(fh) or {}

    return data
