# Copyright © 2023 Marcin Różewski MDSANIMA


"""This is a functionality for parsing arguments in command-line tools."""


from __future__ import annotations

import argparse

from ._version import __version__


AP_TOP_PROG = "mdsanima"
AP_TOP_DESC = "Command-line tools for image processing."
AP_TOP_EPIL = "Copyright \U000000A9 2023 Marcin Różewski MDSANIMA"

CP_PROG = "check"
CP_DESC = "Displaying info about all images in the current directory."
CP_HELP = "printing info about all images inside the current directory"

PP_PROG = "pixelart"
PP_DESC = "Generating pixel art from all images in the current directory."
PP_HELP = "generate pixel art from all images in the current directory"

GP_PROG = "gif"
GP_DESC = "Generating GIF from pixel art images in the current directory."
GP_HELP = "generate gif from all pixel art images in the current directory"


def create_parser() -> None:
    """This function creates an argument parser for all available functions in
    this package, which can be used in command-line tools.
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
        CP_PROG,
        description=CP_DESC,
        help=CP_HELP,
        epilog=AP_TOP_EPIL,
    )
    check_parser.set_defaults(command=CP_PROG)

    # Create subparser for pixelart command.
    pixelart_parser = subparsers.add_parser(
        PP_PROG,
        description=PP_DESC,
        help=PP_HELP,
        epilog=AP_TOP_EPIL,
    )
    pixelart_parser.set_defaults(command=PP_PROG)

    # Create subparser for gif command.
    gif_parser = subparsers.add_parser(
        GP_PROG,
        description=GP_DESC,
        help=GP_HELP,
        epilog=AP_TOP_EPIL,
    )
    gif_parser.set_defaults(command=GP_PROG)

    return parser
