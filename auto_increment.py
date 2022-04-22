"""Imitates auto-increment primary key"""
# pylint: disable=missing-function-docstring
from dataclasses import dataclass, field
from typing import Dict
from collections import Counter


@dataclass
class AutoIncrement:
    """Maintains id progression of each unique table creation"""

    counters: Dict[str, int] = field(default_factory=Counter, init=False)

    def next_id(self, name: str) -> int:
        self.counters[name] += 1
        return self.counters[name]
