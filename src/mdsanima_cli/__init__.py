# Copyright © 2023 Marcin Różewski MDSANIMA


"""Initial main functionality for command-line tools."""


from __future__ import annotations

from mdsanima_dev.colors import get_complex_color

from .parser import create_parser
from .cli_check import print_directory_check
from .cli_pixelart import compute_pixelart


def main_cli():
    """The main command-line function responsible for sub-functions and
    allocation separation.
    """

    # Argument parser and color print.
    parser = create_parser()
    args = parser.parse_args()
    mprint = get_complex_color

    # Checking argument parser and execute function for it.
    try:
        if args.command == "check":
            print_directory_check("directory info stats")
        if args.command == "pixelart":
            print_directory_check("compute pixel art 32px")
            compute_pixelart()
        if args.command == "gif":
            mprint("hello from gif", 12)
    except AttributeError:
        parser.print_help()
