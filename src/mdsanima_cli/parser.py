# Copyright © 2023 Marcin Różewski MDSANIMA


"""This is a functionality for parsing arguments in command-line tools."""


from __future__ import annotations

import argparse

from mdsanima_cli._version import __version__


PROG = "mdsanima"
DESCRIPTION = "MDSANIMA CLI is a command-line interface for image processing."
EPILOG = "Copyright \U000000A9 2023 Marcin Różewski MDSANIMA"

ALL_IMAGES = "all images file inside the current directory."
SUBPERSER_DESCRIPTION = f"All commands execute on {ALL_IMAGES}"

CHECK_NAME = "check"
CHECK_DESCRIPTION = f"Print statistic info about {ALL_IMAGES}"
CHECK_HELP = "print directory info"

UUID_NAME = "uuid"
UUID_DESCRIPTION = f"Rename to UUID {ALL_IMAGES}"
UUID_HELP = "rename to UUID"

NUMBER_NAME = "number"
NUMBER_DESCRIPTION = f"Rename to sequential numbers {ALL_IMAGES}"
NUMBER_HELP = "rename to seq numbers"

LOGO_NAME = "logo"
LOGO_DESCRIPTION = f"Append a logo to {ALL_IMAGES}"
LOGO_HELP = "append a logo"

WATERMARK_NAME = "watermark"
WATERMARK_DESCRIPTION = f"Append a watermark to {ALL_IMAGES}"
WATERMARK_HELP = "append a watermark"

JPG_NAME = "jpg"
JPG_DESCRIPTION = f"Convert to JPG format {ALL_IMAGES}"
JPG_HELP = "convert to JPG"

PNG_NAME = "png"
PNG_DESCRIPTION = f"Convert to PNG format {ALL_IMAGES}"
PNG_HELP = "convert to PNG"

WEBP_NAME = "webp"
WEBP_DESCRIPTION = f"Convert to WebP format {ALL_IMAGES}"
WEBP_HELP = "convert to WebP"

PIXELART_NAME = "pixelart"
PIXELART_DESCRIPTION = f"Generate pixel art from {ALL_IMAGES}"
PIXELART_HELP = "generate pixel art"

GRID_NAME = "grid"
GRID_DESCRIPTION = f"Generate grid 2x2 from {ALL_IMAGES}"
GRID_HELP = "generate grid 2x2"


def create_parser() -> None:
    """This function creates an argument parser for all available functions in this package, which
    can be used in command-line tools.
    """

    # Create top level parser for mdsanima command.
    parser = argparse.ArgumentParser(
        prog=PROG,
        description=DESCRIPTION,
        epilog=EPILOG,
        formatter_class=argparse.RawTextHelpFormatter,
    )
    parser.add_argument(
        "-v",
        "--version",
        action="version",
        version="%(prog)s-cli " + __version__,
    )
    subparser = parser.add_subparsers(title="commands", description=SUBPERSER_DESCRIPTION)

    # Create subparser for check command.
    check_parser = subparser.add_parser(
        name=CHECK_NAME,
        description=CHECK_DESCRIPTION,
        help=CHECK_HELP,
        epilog=EPILOG,
    )
    check_parser.set_defaults(command=CHECK_NAME)

    # Create subparser for uuid command.
    uuid_parser = subparser.add_parser(
        name=UUID_NAME,
        description=UUID_DESCRIPTION,
        help=UUID_HELP,
        epilog=EPILOG,
    )
    uuid_parser.set_defaults(command=UUID_NAME)

    # Create subparser for number command.
    number_parser = subparser.add_parser(
        name=NUMBER_NAME,
        description=NUMBER_DESCRIPTION,
        help=NUMBER_HELP,
        epilog=EPILOG,
    )
    number_parser.set_defaults(command=NUMBER_NAME)

    # Create subparser for logo command.
    logo_parser = subparser.add_parser(
        name=LOGO_NAME,
        description=LOGO_DESCRIPTION,
        help=LOGO_HELP,
        epilog=EPILOG,
    )
    logo_parser.set_defaults(command=LOGO_NAME)

    # Create subparser for watermark command.
    watermark_parser = subparser.add_parser(
        name=WATERMARK_NAME,
        description=WATERMARK_DESCRIPTION,
        help=WATERMARK_HELP,
        epilog=EPILOG,
    )
    watermark_parser.set_defaults(command=WATERMARK_NAME)

    # Create subparser for jpg command.
    jpg_parser = subparser.add_parser(
        name=JPG_NAME,
        description=JPG_DESCRIPTION,
        help=JPG_HELP,
        epilog=EPILOG,
    )
    jpg_parser.set_defaults(command=JPG_NAME)

    # Create subparser for png command.
    png_parser = subparser.add_parser(
        name=PNG_NAME,
        description=PNG_DESCRIPTION,
        help=PNG_HELP,
        epilog=EPILOG,
    )
    png_parser.set_defaults(command=PNG_NAME)

    # Create subparser for webp command.
    webp_parser = subparser.add_parser(
        name=WEBP_NAME,
        description=WEBP_DESCRIPTION,
        help=WEBP_HELP,
        epilog=EPILOG,
    )
    webp_parser.set_defaults(command=WEBP_NAME)

    # Create subparser for pixelart command.
    pixelart_parser = subparser.add_parser(
        name=PIXELART_NAME,
        description=PIXELART_DESCRIPTION,
        help=PIXELART_HELP,
        epilog=EPILOG,
    )
    pixelart_parser.set_defaults(command=PIXELART_NAME)

    # Create subparser for grid command.
    grid_parser = subparser.add_parser(
        name=GRID_NAME,
        description=GRID_DESCRIPTION,
        help=GRID_HELP,
        epilog=EPILOG,
    )
    grid_parser.set_defaults(command=GRID_NAME)

    return parser
