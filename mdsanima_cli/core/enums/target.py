# Copyright (c) 2023 MDSANIMA

"""Target values that share between a group of enumerations."""


from __future__ import annotations

from enum import auto
from enum import unique

from mdsanima_cli.core.enums import AutoName


@unique
class Target(AutoName):
    """The default target datasets."""

    CLI = auto()
    CMD = auto()
    MDSANIMA = auto()
    COMMAND = auto()
    OPTIONS = auto()
    CONFIG = auto()
    USAGE = auto()
    SHOW = auto()
    LIST = auto()
    HELP = auto()
    PRINT = auto()
    RENAME = auto()
    APEND = auto()
    CONVERT = auto()
    GENERATE = auto()
    RESIZE = auto()

    def __str__(self):
        return f"{self.name}"

    def __format__(self, spec):
        return f"{self.name}"
