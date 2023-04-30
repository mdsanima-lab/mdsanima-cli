# Copyright © 2023 Marcin Różewski MDSANIMA


"""This is a functionality for parsing arguments in command-line tools."""


from __future__ import annotations

import argparse

from ._version import __version__  # pylint: disable=E0401


AP_TOP_PROG = "mdsanima"
AP_TOP_DESC = "MDSANIMA CLI is a command-line interface for image processing."
AP_TOP_EPIL = "Copyright \U000000A9 2023 Marcin Różewski MDSANIMA"

CHE_AP_PROG = "check"
CHE_AP_DESC = "Displaying info about all images in the current directory."
CHE_AP_HELP = "printing info about all images inside the current dir"

PIX_AP_PROG = "pixelart"
PIX_AP_DESC = "Generate pixel art from all images in the current directory."
PIX_AP_HELP = "generating pixel art from all images in the current dir"

UUI_AP_PROG = "uuid"
UUI_AP_DESC = "Rename image files to UUID in the current directory."
UUI_AP_HELP = "renaming all images file to UUID in the current dir"

NUM_AP_PROG = "number"
NUM_AP_DESC = "Rename image files to sequential numbers in current directory."
NUM_AP_HELP = "renaming all images file to seq numbers in the current dir"

LOG_AP_PROG = "logo"
LOG_AP_DESC = "Append a logo to all images in the current directory."
LOG_AP_HELP = "appending a logo to all images in the current dir"

WAT_AP_PROG = "watermark"
WAT_AP_DESC = "Append a watermark to all images in the current directory."
WAT_AP_HELP = "appending a watermark to all images in the current dir"

GRI_AP_PROG = "grid"
GRI_AP_DESC = "Generate a grid 2x2 from all images in the current directory."
GRI_AP_HELP = "generating a grid 2x2 from all images in the current dir"

JPG_AP_PROG = "jpg"
JPG_AP_DESC = "Convert image files to JPG format in the current directory."
JPG_AP_HELP = "converting image files to JPG format in the current dir"

PNG_AP_PROG = "png"
PNG_AP_DESC = "Convert image files to PNG format in the current directory."
PNG_AP_HELP = "converting image files to PNG format in the current dir"

WEB_AP_PROG = "webp"
WEB_AP_DESC = "Convert image files to WEBP format in the current directory."
WEB_AP_HELP = "converting image files to WEBP format in the current dir"


def create_argument_parser() -> None:
    """This function creates an argument parser for all available functions in this package, which
    can be used in command-line tools.
    """

    # Create top level parser for mdsanima command.
    parser = argparse.ArgumentParser(
        prog=AP_TOP_PROG,
        description=AP_TOP_DESC,
        epilog=AP_TOP_EPIL,
        formatter_class=argparse.RawTextHelpFormatter,
    )
    parser.add_argument(
        "-v",
        "--version",
        action="version",
        version="%(prog)s-cli " + __version__,
    )
    subparsers = parser.add_subparsers()

    # Create subparser for check command.
    check_parser = subparsers.add_parser(
        CHE_AP_PROG,
        description=CHE_AP_DESC,
        help=CHE_AP_HELP,
        epilog=AP_TOP_EPIL,
    )
    check_parser.set_defaults(command=CHE_AP_PROG)

    # Create subparser for pixelart command.
    pixelart_parser = subparsers.add_parser(
        PIX_AP_PROG,
        description=PIX_AP_DESC,
        help=PIX_AP_HELP,
        epilog=AP_TOP_EPIL,
    )
    pixelart_parser.set_defaults(command=PIX_AP_PROG)

    # Create subparser for uuid command.
    uuid_parser = subparsers.add_parser(
        UUI_AP_PROG,
        description=UUI_AP_DESC,
        help=UUI_AP_HELP,
        epilog=AP_TOP_EPIL,
    )
    uuid_parser.set_defaults(command=UUI_AP_PROG)

    # Create subparser for number command.
    number_parser = subparsers.add_parser(
        NUM_AP_PROG,
        description=NUM_AP_DESC,
        help=NUM_AP_HELP,
        epilog=AP_TOP_EPIL,
    )
    number_parser.set_defaults(command=NUM_AP_PROG)

    # Create subparser for logo command.
    logo_parser = subparsers.add_parser(
        LOG_AP_PROG,
        description=LOG_AP_DESC,
        help=LOG_AP_HELP,
        epilog=AP_TOP_EPIL,
    )
    logo_parser.set_defaults(command=LOG_AP_PROG)

    # Create subparser for watermark command.
    watermark_parser = subparsers.add_parser(
        WAT_AP_PROG,
        description=WAT_AP_DESC,
        help=WAT_AP_HELP,
        epilog=AP_TOP_EPIL,
    )
    watermark_parser.set_defaults(command=WAT_AP_PROG)

    # Create subparser for grid command.
    grid_parser = subparsers.add_parser(
        GRI_AP_PROG,
        description=GRI_AP_DESC,
        help=GRI_AP_HELP,
        epilog=AP_TOP_EPIL,
    )
    grid_parser.set_defaults(command=GRI_AP_PROG)

    # Create subparser for jpg command.
    jpg_parser = subparsers.add_parser(
        JPG_AP_PROG,
        description=JPG_AP_DESC,
        help=JPG_AP_HELP,
        epilog=AP_TOP_EPIL,
    )
    jpg_parser.set_defaults(command=JPG_AP_PROG)

    # Create subparser for png command.
    png_parser = subparsers.add_parser(
        PNG_AP_PROG,
        description=PNG_AP_DESC,
        help=PNG_AP_HELP,
        epilog=AP_TOP_EPIL,
    )
    png_parser.set_defaults(command=PNG_AP_PROG)

    # Create subparser for webp command.
    webp_parser = subparsers.add_parser(
        WEB_AP_PROG,
        description=WEB_AP_DESC,
        help=WEB_AP_HELP,
        epilog=AP_TOP_EPIL,
    )
    webp_parser.set_defaults(command=WEB_AP_PROG)

    return parser
