# Copyright © 2023 Marcin Różewski MDSANIMA


"""Initial main functionality for command-line tools."""


from __future__ import annotations

from .ascii import ascii_title
from .parser import create_argument_parser

from .cli_check import cli_check
from .cli_number import cli_number
from .cli_pixelart import cli_pixelart
from .cli_uuid import cli_uuid


def main_cli():
    """The main command-line function responsible for sub-functions and
    allocation separation.
    """

    # Argument parser and color print.
    parser = create_argument_parser()
    args = parser.parse_args()

    # Print nice asci text.
    ascii_title("mdsanima cli")

    try:
        # Check argument parser and execute function for it.
        if args.command == "check":
            cli_check()
        if args.command == "pixelart":
            cli_pixelart()
        if args.command == "uuid":
            cli_uuid()
        if args.command == "number":
            cli_number()
        if args.command == "logo":
            print("hello from logo")
    except AttributeError:
        parser.print_help()
