# Copyright © 2023 Marcin Różewski MDSANIMA


"""This module provides various utilities helpers that can be used for one line multiple colors
printing. The module is intended for use in development.
"""


from __future__ import annotations

from typing import Literal

from mdsanima_dev.colors import get_complex_color


mprint = get_complex_color


def print_cli_info(
    key: str, info: str, bracket_color: int, key_color: int, info_color: int
) -> None:
    """Helper for printing multiple colors info in one line. Aligning the last bracket to the right
    within a maximum width of 14 characters. You can choose individual colors for the bracket, text
    inside the bracket, and the last text. The string `key` and `info` are always printed in upper
    case.

    Example look: `[MDSANIMA CLI] -> CHECK`
    """

    # Calculating align spaces.
    align = len(key) + 1

    # Print multiple colors in one line.
    mprint("[".rjust(14 - align), bracket_color, "")
    mprint(str(key).upper(), key_color, "")
    mprint("]", bracket_color, "")
    mprint(" -> ", 197, "")
    mprint(str(info).upper(), info_color)


def print_cli_data(
    key: str, data: str, bracket_color: int, key_color: int, data_color: int
) -> None:
    """Helper for printing multiple colors data in one line. Aligning the last bracket to the right
    within a maximum width of 14 characters. You can choose individual colors for the bracket, text
    inside the bracket, and the last text. The string `key` are always printed in upper case.

    Example look: `[REAL PATH] /home/mdsanima/dev/mdsanima-cli`
    """

    # Calculating align spaces.
    align = len(key) + 1

    # Print multiple colors in one line.
    mprint("[".rjust(14 - align), bracket_color, "")
    mprint(str(key).upper(), key_color, "")
    mprint("]", bracket_color, " ")
    mprint(str(data), data_color)


def print_cli_proc(
    process: Literal["appending", "computing", "converting", "renaming"],
    count: int,
    old: str,
    new: str,
    time_taken: float,
) -> None:
    """Helper for printing multiple colors processing info in one line. The colors have already been
    selected, you can configure only the text without changing the colors. The string `process` are
    always printed in upper case. The colors are shades of green and blue.

    Example look: `[APPENDING 00001] image.png -> image_pixelart.png -> ran in 1.337 sec`
    """

    # Print multiple colors in one line.
    mprint("[", 50, "")
    mprint(str(process).upper(), 37, " ")
    mprint(str(count).zfill(5), 24, "")
    mprint("]", 50, " ")
    mprint(str(old), 40, "")
    mprint(" -> ", 49, "")
    mprint(str(new), 34, "")
    mprint(" -> ", 197, "")
    mprint("ran in", 25, " ")
    mprint(str(time_taken), 26, " ")
    mprint("sec", 25)


def print_cli_comp(
    process: Literal["appending", "computing", "converting", "renaming"],
    count: int,
    old: str,
    new: str,
    time_taken: float,
) -> None:
    """Helper for printing multiple colors computing info in one line. The colors have already been
    selected, you can configure only the text without changing the colors. The string `process` are
    always printed in upper case. The colors are shades of red and green.

    Example look: `[COMPUTING 00001] image.png -> image_pixelart.png -> ran in 1.337 sec`
    """

    # Print multiple colors in one line.
    mprint("[", 203, "")
    mprint(str(process).upper(), 197, " ")
    mprint(str(count).zfill(5), 209, "")
    mprint("]", 203, " ")
    mprint(str(old), 3, "")
    mprint(" -> ", 203, "")
    mprint(str(new), 113, "")
    mprint(" -> ", 197, "")
    mprint("ran in", 25, " ")
    mprint(str(time_taken), 26, " ")
    mprint("sec", 25)


def print_cli_done(time_taken: float) -> None:
    """Helper for printing multiple colors done info in one line. The colors and text have already
    been selected, you can onfigure only the time taken without changing the colors. The colors are
    shades of blue and red.

    Configured look: `[DONE] Processing is finished -> ran in 1.337 sec`
    """

    # Print multiple colors in one line.
    mprint("[", 28, "")
    mprint("done".upper(), 40, "")
    mprint("]", 28, " ")
    mprint("Processing is finished", 197, "")
    mprint(" -> ", 155, "")
    mprint("ran in", 25, " ")
    mprint(str(time_taken), 26, " ")
    mprint("sec", 25)
