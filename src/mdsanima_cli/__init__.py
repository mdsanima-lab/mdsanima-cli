# Copyright © 2023 Marcin Różewski MDSANIMA


"""Initial main functionality for command-line tools."""


from __future__ import annotations

from .parser import create_argument_parser
from .utils import check_system_dependencies
from .utils import asci_metal_border_text

from .cli_check import cli_check
from .cli_pixelart import cli_pixelart


def main_cli():
    """The main command-line function responsible for sub-functions and
    allocation separation.
    """

    # Argument parser and color print.
    parser = create_argument_parser()
    args = parser.parse_args()

    # Checking system dependencies.
    check_system_dependencies("figlet")
    check_system_dependencies("toilet")

    # Print nice asci text.
    asci_metal_border_text("mdsanima cli")

    try:
        # Check argument parser and execute function for it.
        if args.command == "check":
            cli_check()
        if args.command == "pixelart":
            cli_pixelart()
        if args.command == "gif":
            print("hello from gif", 12)
    except AttributeError:
        parser.print_help()
