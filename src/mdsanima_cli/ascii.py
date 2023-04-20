# Copyright © 2023 Marcin Różewski MDSANIMA


"""This module is for printing ASCII art text with colors."""


from __future__ import annotations

from mdsanima_dev.colors import get_complex_color


def generate_ascii(
    ascii_line_a: str,
    ascii_line_b: str,
    ascii_line_c: str,
    border_color: int,
    ascii_color: int,
    width: int = 50,
) -> None:
    """Generate ASCII art text in color and with a border. Printing ASCI art
    in 5 lines. You can adjust a width and color.
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
    mprint(ascii_line_a.center(width), ascii_color, "")
    mprint(border_vertical, border_color)

    # Line 3.
    mprint(border_vertical, border_color, "")
    mprint(ascii_line_b.center(width), ascii_color, "")
    mprint(border_vertical, border_color)

    # Line 4.
    mprint(border_vertical, border_color, "")
    mprint(ascii_line_c.center(width), ascii_color, "")
    mprint(border_vertical, border_color)

    # Line 5.
    mprint(border_bot, border_color)


def ascii_title(option: str) -> None:
    """Print ASCII title art text in color and with a border. For now is two
    options you can use.

    Title option 1: `mdsanima cli`
    Title option 2: `processing`
    """

    # Ascii tile option 1.
    ascii_cli_a = "┏┳┓╺┳┓┏━┓┏━┓┏┓╻╻┏┳┓┏━┓   ┏━╸╻  ╻"
    ascii_cli_b = "┃┃┃ ┃┃┗━┓┣━┫┃┗┫┃┃┃┃┣━┫   ┃  ┃  ┃"
    ascii_cli_c = "╹ ╹╺┻┛┗━┛╹ ╹╹ ╹╹╹ ╹╹ ╹   ┗━╸┗━╸╹"

    # Ascii title option 2.
    ascii_proc_a = "┏━┓┏━┓┏━┓┏━╸┏━╸┏━┓┏━┓╻┏┓╻┏━╸"
    ascii_proc_b = "┣━┛┣┳┛┃ ┃┃  ┣╸ ┗━┓┗━┓┃┃┗┫┃╺┓"
    ascii_proc_c = "╹  ╹┗╸┗━┛┗━╸┗━╸┗━┛┗━┛╹╹ ╹┗━┛"

    # Check which option to print.
    if option == "mdsanima cli":
        generate_ascii(ascii_cli_a, ascii_cli_b, ascii_cli_c, 40, 50)
    if option == "processing":
        generate_ascii(ascii_proc_a, ascii_proc_b, ascii_proc_c, 50, 197)
