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
    """Helper for printing multiple colors info in one line. Aligning the last
    bracket to the right within a maximum width of 14 characters. You can
    choose individual colors for the bracket, text inside the bracket, and the
    last text.

    Example look: `[MDSANIMA CLI] -> CHECK`
    """

    # Calculating align spaces.
    align = len(key) + 1

    # Print multiple colors in one line.
    mprint("[".rjust(14 - align), bracket_color, "")
    mprint(str(key), key_color, "")
    mprint("]", bracket_color, " -> ")
    mprint(str(info), info_color)


def print_cli_data(
    key: str, data: str, bracket_color: int, key_color: int, data_color: int
) -> None:
    """Helper for printing multiple colors data in one line. Aligning the last
    bracket to the right within a maximum width of 14 characters. You can
    choose individual colors for the bracket, text inside the bracket, and the
    last text.

    Example look: `[REAL PATH] /home/mdsanima/dev/mdsanima-cli`
    """

    # Calculating align spaces.
    align = len(key) + 1

    # Print multiple colors in one line.
    mprint("[".rjust(14 - align), bracket_color, "")
    mprint(str(key), key_color, "")
    mprint("]", bracket_color, " ")
    mprint(str(data), data_color)


def print_cli_proc(process: str, count: str, old: str, new: str) -> None:
    """Helper for printing multiple colors processing info in one line. The
    colors have already been selected, you can configure only the text without
    changing the colors.

    Example look: `[COMPUTING 0001] image.png -> image_pixelart.png`
    """

    # Print multiple colors in one line.
    mprint("[", 50, "")
    mprint(str(process), 37, " ")
    mprint(str(count), 24, "")
    mprint("]", 50, " ")
    mprint(str(old), 40, "")
    mprint(" -> ", 49, "")
    mprint(str(new), 34)
