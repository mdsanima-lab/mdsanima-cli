# Copyright (c) 2023 MDSANIMA

"""Generating the name automatically for enumeration next value."""


from __future__ import annotations

from enum import Enum


class AutoName(Enum):
    """Generate next value the name automatically."""

    @staticmethod
    def _generate_next_value_(name, start, count, last_values):
        return name


class AutoNameLower(Enum):
    """Generate next value the name automatically and converting to lowercase."""

    @staticmethod
    def _generate_next_value_(name, start, count, last_values):
        return name.lower()


class AutoNameUpper(Enum):
    """Generate next value the name automatically and converting to uppercase."""

    @staticmethod
    def _generate_next_value_(name, start, count, last_values):
        return name.upper()
