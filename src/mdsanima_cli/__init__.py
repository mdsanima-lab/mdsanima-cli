# Copyright © 2023 Marcin Różewski MDSANIMA


"""Initial main functionality for command-line tools."""


from __future__ import annotations

from mdsanima_dev.colors import get_complex_color

from .parser import create_parser
from .utils import check_system_dependencies
from .utils import asci_metal_border_text

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

    # Checking system dependencies.
    check_system_dependencies("figlet")
    check_system_dependencies("toilet")

    # Print nice asci text.
    asci_metal_border_text("mdsanima-cli")

    try:
        # Check argument parser and execute function for it.
        if args.command == "check":
            print_directory_check("DIRECTORY INFO STATS")
        if args.command == "pixelart":
            print_directory_check("COMPUTE PIXEL ART 32PX")
            compute_pixelart()
        if args.command == "gif":
            mprint("hello from gif", 12)
    except AttributeError:
        parser.print_help()
