# Copyritht © 2023 Marcin Różewski MDSANIMA


"""Initial main functionality for command line tools."""


from __future__ import annotations

from mdsanima_dev.colors import get_complex_color

from .parser import create_parser
from .pixelart import compute_pixelart


def main_cli():
    parser = create_parser()
    args = parser.parse_args()
    mprint = get_complex_color

    try:
        if args.command == "pixelart":
            mprint("generating pixelart", 40)
            compute_pixelart()
        elif args.command == "gifmaker":
            mprint("hello from gifmaker", 40)
    except AttributeError:
        parser.print_help()
