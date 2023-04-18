# Copyright © 2023 Marcin Różewski MDSANIMA


"""This module provides various utilities helpers that can be used for one line
multiple colors printing. The module is intended for use in development.
"""


from __future__ import annotations

from mdsanima_dev.colors import get_complex_color


# Color print variable.
mprint = get_complex_color


def print_cli_info(
    key: str, info: str, bracket_color: int, key_color: int, info_color: int
) -> None:
    """Helper for printing multiple colors info in one line."""

    # Print multiple colors one line.
    mprint("[", bracket_color, "")
    mprint(str(key), key_color, "")
    mprint("]", bracket_color, " -> ")
    mprint(str(info), info_color)


def print_cli_data(
    key: str, data: str, bracket_color: int, key_color: int, data_color: int
) -> None:
    """Helper for printing multiple colors data in one line."""

    # Calculating align spaces.
    align = len(key) + 1

    # Print multiple colors one line.
    mprint("[".rjust(14 - align), bracket_color, "")
    mprint(str(key), key_color, "")
    mprint("]", bracket_color, " ")
    mprint(str(data), data_color)
