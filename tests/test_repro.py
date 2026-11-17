import random
import numpy as np

import sentinel
from sentinel.utils.repro import git_commit, seed_everything

def test_package_imports():
    assert sentinel.__version__

def test_seed_everything_makes_randomness_repeatable():
    seed_everything(123)
    first = (random.random(), np.random.rand())
    seed_everything(123)
    second = (random.random(), np.random.rand())
    assert first == second

def test_git_commit_returns_a_string():
    assert isinstance(git_commit(), str)