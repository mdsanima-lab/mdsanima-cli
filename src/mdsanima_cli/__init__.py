# Copyritht © 2023 Marcin Różewski MDSANIMA


"""Initial main functionality for command line tools."""


from __future__ import annotations

from ._version import __version__

import argparse
from mdsanima_dev.colors import get_complex_color


AP_DESCRIPTION = "Command line tools for images processing."
AP_EPILOG = "Copyritht \U000000A9 2023 Marcin Różewski MDSANIMA"


def create_parser() -> None:
    # Create top level argument parser.
    parser = argparse.ArgumentParser(
        prog="mdsanima",
        description=AP_DESCRIPTION,
        epilog=AP_EPILOG,
        formatter_class=argparse.RawTextHelpFormatter,
    )
    parser.add_argument(
        "-v",
        "--version",
        action="version",
        version="%(prog)s-cli " + __version__,
    )
    subparsers = parser.add_subparsers()

    # Create subparser for pixelart.
    pixelart_parser = subparsers.add_parser(
        "pixelart",
        description="Generating pixelart from images.",
        help="computing all images in folder",
        epilog=AP_EPILOG,
    )
    pixelart_parser.set_defaults(command="pixelart")

    # Create subparser for gifmaker.
    gifmaker_parser = subparsers.add_parser(
        "gifmaker",
        description="Generating gif from pixelart images.",
        help="computing gif from one pixelart image",
        epilog=AP_EPILOG,
    )
    gifmaker_parser.set_defaults(command="gifmaker")

    return parser


def main_cli():
    parser = create_parser()
    args = parser.parse_args()
    mprint = get_complex_color

    try:
        if args.command == "pixelart":
            mprint("Hello from pixelart", 46)
        elif args.command == "gifmaker":
            mprint("Hello from gifmaker", 46)
    except AttributeError:
        parser.print_help()
