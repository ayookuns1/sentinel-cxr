"""Training entry point. In Phase 0 it only proves that config + reproducibility plumbing works."""

from __future__ import annotations

import logging
from pathlib import Path

import hydra
from omegaconf import DictConfig, OmegaConf

from sentinel.utils.repro import git_commit, seed_everything

log = logging.getLogger(__name__)

# An absolute path, so it works however the script is launched (sentinel-train, python -m, Kaggle).
CONFIG_DIR = str(Path(__file__).resolve().parents[2] / "configs")


@hydra.main(version_base=None, config_path=CONFIG_DIR, config_name="config")
def main(cfg: DictConfig) -> None:
    seed_everything(cfg.seed)
    log.info("git commit: %s", git_commit())
    log.info("resolved config:\n%s", OmegaConf.to_yaml(cfg, resolve=True))
    log.info("Nothing to train yet: this is the Phase 0 skeleton.")


if __name__ == "__main__":
    main()
