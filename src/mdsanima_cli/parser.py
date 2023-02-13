# Copyritht © 2023 Marcin Różewski MDSANIMA


"""This is a arguments parser functionality for command line tools."""


from __future__ import annotations

from ._version import __version__

import argparse


def create_parser() -> None:
    """This function is for creating arguments parser for all the function on
    this package that's available in command line tools.
    """
    AP_DESCRIPTION = "Command line tools for images processing."
    AP_EPILOG = "Copyritht \U000000A9 2023 Marcin Różewski MDSANIMA"

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
