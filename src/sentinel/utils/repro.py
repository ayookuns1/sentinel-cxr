"""Reproducibility helpers: seeds and the git commit every run is tied to."""

from __future__ import annotations

import os
import random
import subprocess

import numpy as np


def seed_everything(seed: int) -> None:
    """Seed every random number generator we use, so a run can be repeated."""
    random.seed(seed)
    np.random.seed(seed)
    os.environ["PYTHONHASHSEED"] = str(seed)
    try:
        import torch
    except ImportError:
        return
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)


def git_commit() -> str:
    """Return the current commit hash, with '-dirty' if there are uncommitted changes.

    Return "unknown" if git isn't available or we're not inside a repository.
    """

    try:
        sha = subprocess.check_output(
            ["git", "rev-parse", "HEAD"], text=True, stderr=subprocess.DEVNULL
        ).strip()
        dirty = subprocess.check_output(
            ["git", "status", "--porcelain"], text=True, stderr=subprocess.DEVNULL
        ).strip()
    except (OSError, subprocess.CalledProcessError):
        return "unknown"
    return f"{sha}-dirty" if dirty else sha
