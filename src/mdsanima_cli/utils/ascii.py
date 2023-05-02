# Copyright © 2023 Marcin Różewski MDSANIMA


"""This module is for printing ASCII art text with colors."""


from __future__ import annotations

from mdsanima_dev.colors import get_complex_color


def get_ascii_character() -> dict:
    """This function returns a single ASCII character that includes the entire alphabet, numbers,
    and some special characters includes spaces. Each character is displayed on 3 lines, and the
    width is 3 normal-length spaces.

    Usage: `ascii["a"][0]` returns the first line of the character `a` in ASCII format. To obtain
    the entire character, you need to retrieve lines `ascii["a"][1]` and `ascii["a"][2]` as well.

    Return: `dict[str, list[str]]`

    Characters: `ABCDEFGHIJKLMNOPQRSTUVWXYZ`
    Numbers: `0123456789`
    Specials: `()[]{}!?$*-+=_|;:,. `
    """

    # Entire alphabet, numbers and some special characters.
    ascii_character = {
        "a": [
            "┏━┓",
            "┣━┫",
            "╹ ╹",
        ],
        "b": [
            "┏┓ ",
            "┣┻┓",
            "┗━┛",
        ],
        "c": [
            "┏━╸",
            "┃  ",
            "┗━╸",
        ],
        "d": [
            "╺┳┓",
            " ┃┃",
            "╺┻┛",
        ],
        "e": [
            "┏━╸",
            "┣╸ ",
            "┗━╸",
        ],
        "f": [
            "┏━╸",
            "┣╸ ",
            "╹  ",
        ],
        "g": [
            "┏━╸",
            "┃╺┓",
            "┗━┛",
        ],
        "h": [
            "╻ ╻",
            "┣━┫",
            "╹ ╹",
        ],
        "i": [
            "╻",
            "┃",
            "╹",
        ],
        "j": [
            " ┏┓",
            "  ┃",
            "┗━┛",
        ],
        "k": [
            "╻┏ ",
            "┣┻┓",
            "╹ ╹",
        ],
        "l": [
            "╻  ",
            "┃  ",
            "┗━╸",
        ],
        "m": [
            "┏┳┓",
            "┃┃┃",
            "╹ ╹",
        ],
        "n": [
            "┏┓╻",
            "┃┗┫",
            "╹ ╹",
        ],
        "o": [
            "┏━┓",
            "┃ ┃",
            "┗━┛",
        ],
        "p": [
            "┏━┓",
            "┣━┛",
            "╹  ",
        ],
        "q": [
            "┏━┓",
            "┃┓┃",
            "┗┻┛",
        ],
        "r": [
            "┏━┓",
            "┣┳┛",
            "╹┗╸",
        ],
        "s": [
            "┏━┓",
            "┗━┓",
            "┗━┛",
        ],
        "t": [
            "╺┳╸",
            " ┃ ",
            " ╹ ",
        ],
        "u": [
            "╻ ╻",
            "┃ ┃",
            "┗━┛",
        ],
        "v": [
            "╻ ╻",
            "┃┏┛",
            "┗┛ ",
        ],
        "w": [
            "╻ ╻",
            "┃╻┃",
            "┗┻┛",
        ],
        "x": [
            "╻ ╻",
            "┏╋┛",
            "╹ ╹",
        ],
        "y": [
            "╻ ╻",
            "┗┳┛",
            " ╹ ",
        ],
        "z": [
            "╺━┓",
            "┏━┛",
            "┗━╸",
        ],
        "0": [
            "┏━┓",
            "┃┃┃",
            "┗━┛",
        ],
        "1": [
            "╺┓ ",
            " ┃ ",
            "╺┻╸",
        ],
        "2": [
            "┏━┓",
            "┏━┛",
            "┗━╸",
        ],
        "3": [
            "┏━┓",
            "╺━┫",
            "┗━┛",
        ],
        "4": [
            "╻ ╻",
            "┗━┫",
            "  ╹",
        ],
        "5": [
            "┏━╸",
            "┗━┓",
            "┗━┛",
        ],
        "6": [
            "┏━┓",
            "┣━┓",
            "┗━┛",
        ],
        "7": [
            "┏━┓",
            "  ┃",
            "  ╹",
        ],
        "8": [
            "┏━┓",
            "┣━┫",
            "┗━┛",
        ],
        "9": [
            "┏━┓",
            "┗━┫",
            "┗━┛",
        ],
        "(": [
            "┏╸",
            "┃ ",
            "┗╸",
        ],
        ")": [
            "╺┓",
            " ┃",
            "╺┛",
        ],
        "[": [
            "┏━ ",
            "┃  ",
            "┗━ ",
        ],
        "]": [
            " ━┓",
            "  ┃",
            " ━┛",
        ],
        "{": [
            " ┏╸",
            "╺┫ ",
            " ┗╸",
        ],
        "}": [
            "╺┓ ",
            " ┣╸",
            "╺┛ ",
        ],
        "!": [
            "╻",
            "╹",
            "╹",
        ],
        "?": [
            "┏━┓",
            " ╺┛",
            " ╹ ",
        ],
        "$": [
            "┏┳┓",
            "┗╋┓",
            "┗┻┛",
        ],
        "*": [
            "╻ ╻",
            "╺╋╸",
            "╹ ╹",
        ],
        "-": [
            "   ",
            "╺━╸",
            "   ",
        ],
        "+": [
            " ╻ ",
            "╺╋╸",
            " ╹ ",
        ],
        "=": [
            "   ",
            "╺━╸",
            "╺━╸",
        ],
        "_": [
            "   ",
            "   ",
            "╺━╸",
        ],
        "|": [
            "╻",
            "┃",
            "╹",
        ],
        ";": [
            "  ",
            " ╹",
            " ┛",
        ],
        ":": [
            " ",
            "╹",
            "╹",
        ],
        ",": [
            "  ",
            "  ",
            " ┛",
        ],
        ".": [
            " ",
            " ",
            "╹",
        ],
        " ": [
            "   ",
            "   ",
            "   ",
        ],
    }

    return ascii_character


def ascii_border(
    line_1: str, line_2: str, line_3: str, border_color: int, ascii_color: int, width: int = 50
) -> None:
    """Generate ASCII art text in color and with a border. Printing ASCI art in 5 lines. You can
    adjust a width and color.
    """

    # Color print variable.
    mprint = get_complex_color

    # Variables for border.
    border_vertical = "│"
    border_horizontal = "─" * width
    border_top = "┌" + border_horizontal.center(width) + "┐"
    border_bot = "└" + border_horizontal.center(width) + "┘"

    # Line 1.
    mprint(border_top, border_color)

    # Line 2.
    mprint(border_vertical, border_color, "")
    mprint(line_1.center(width), ascii_color, "")
    mprint(border_vertical, border_color)

    # Line 3.
    mprint(border_vertical, border_color, "")
    mprint(line_2.center(width), ascii_color, "")
    mprint(border_vertical, border_color)

    # Line 4.
    mprint(border_vertical, border_color, "")
    mprint(line_3.center(width), ascii_color, "")
    mprint(border_vertical, border_color)

    # Line 5.
    mprint(border_bot, border_color)


def ascii_title(option: str) -> None:
    """Printing ASCII title art text in color and with a border. For now is two options you can use.

    Title option 1: `mdsanima cli`
    Title option 2: `processing`
    """

    # Ascii tile option 1.
    ascii_cli_line_1 = "┏┳┓╺┳┓┏━┓┏━┓┏┓╻╻┏┳┓┏━┓   ┏━╸╻  ╻"
    ascii_cli_line_2 = "┃┃┃ ┃┃┗━┓┣━┫┃┗┫┃┃┃┃┣━┫   ┃  ┃  ┃"
    ascii_cli_line_3 = "╹ ╹╺┻┛┗━┛╹ ╹╹ ╹╹╹ ╹╹ ╹   ┗━╸┗━╸╹"

    # Ascii title option 2.
    ascii_proc_line_1 = "┏━┓┏━┓┏━┓┏━╸┏━╸┏━┓┏━┓╻┏┓╻┏━╸"
    ascii_proc_line_2 = "┣━┛┣┳┛┃ ┃┃  ┣╸ ┗━┓┗━┓┃┃┗┫┃╺┓"
    ascii_proc_line_3 = "╹  ╹┗╸┗━┛┗━╸┗━╸┗━┛┗━┛╹╹ ╹┗━┛"

    # Check which option to print.
    if option == "mdsanima cli":
        ascii_border(ascii_cli_line_1, ascii_cli_line_2, ascii_cli_line_3, 40, 50)
    if option == "processing":
        ascii_border(ascii_proc_line_1, ascii_proc_line_2, ascii_proc_line_3, 50, 197)
