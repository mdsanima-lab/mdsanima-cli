# Copyright © 2023 Marcin Różewski MDSANIMA


"""Initial main functionality for command-line tools."""


from __future__ import annotations

from .ascii import ascii_title
from .parser import create_argument_parser

from .cli_check import cli_check
from .cli_grid import cli_grid
from .cli_jpg import cli_jpg
from .cli_logo import cli_logo
from .cli_number import cli_number
from .cli_pixelart import cli_pixelart
from .cli_png import cli_png
from .cli_uuid import cli_uuid
from .cli_watermark import cli_watermark
from .cli_webp import cli_webp


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
            cli_logo()
        if args.command == "watermark":
            cli_watermark()
        if args.command == "grid":
            cli_grid()
        if args.command == "jpg":
            cli_jpg()
        if args.command == "png":
            cli_png()
        if args.command == "webp":
            cli_webp()
    except AttributeError:
        parser.print_help()
