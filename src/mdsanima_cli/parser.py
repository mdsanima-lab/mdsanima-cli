# Copyright © 2023 Marcin Różewski MDSANIMA


"""This is a functionality for parsing arguments in command-line tools."""


from __future__ import annotations

import argparse

from ._version import __version__


AP_TOP_PROG = "mdsanima"
AP_TOP_DESC = "MDSANIMA CLI is a command-line interface for image processing."
AP_TOP_EPIL = "Copyright \U000000A9 2023 Marcin Różewski MDSANIMA"

CP_PROG = "check"
CP_DESC = "Displaying info about all images in the current directory."
CP_HELP = "printing info about all images inside the current directory"

PP_PROG = "pixelart"
PP_DESC = "Generating pixel art from all images in the current directory."
PP_HELP = "generate pixel art from all images in the current directory"

UP_PROG = "uuid"
UP_DESC = "Rename image files to UUID in the current directory."
UP_HELP = "renaming all images file to UUID in the current directory"

NP_PROG = "number"
NP_DESC = "Rename image files to sequential numbers in current directory."
NP_HELP = "renaming all images file to seq numbers in the current directory"

LP_PROG = "logo"
LP_DESC = "Add a logo to all images in the current directory."
LP_HELP = "adding a logo to all images in the current directory"


def create_argument_parser() -> None:
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

    # Create subparser for uuid command.
    uuid_parser = subparsers.add_parser(
        UP_PROG,
        description=UP_DESC,
        help=UP_HELP,
        epilog=AP_TOP_EPIL,
    )
    uuid_parser.set_defaults(command=UP_PROG)

    # Create subparser for number command.
    number_parser = subparsers.add_parser(
        NP_PROG,
        description=NP_DESC,
        help=NP_HELP,
        epilog=AP_TOP_EPIL,
    )
    number_parser.set_defaults(command=NP_PROG)

    # Create subparser for logo command.
    logo_parser = subparsers.add_parser(
        LP_PROG,
        description=LP_DESC,
        help=LP_HELP,
        epilog=AP_TOP_EPIL,
    )
    logo_parser.set_defaults(command=LP_PROG)

    return parser
