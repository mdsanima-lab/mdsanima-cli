# Copyright © 2023 Marcin Różewski MDSANIMA


"""Initial main functionality for command-line tools."""


from __future__ import annotations

from mdsanima_cli.command.check import cli_check
from mdsanima_cli.command.grid import cli_grid
from mdsanima_cli.command.jpg import cli_jpg
from mdsanima_cli.command.logo import cli_logo
from mdsanima_cli.command.number import cli_number
from mdsanima_cli.command.pixelart import cli_pixelart
from mdsanima_cli.command.png import cli_png
from mdsanima_cli.command.thumbnail import cli_thumbnail
from mdsanima_cli.command.uuids import cli_uuid
from mdsanima_cli.command.watermark import cli_watermark
from mdsanima_cli.command.webp import cli_webp
from mdsanima_cli.parser import create_parser
from mdsanima_cli.utils.ascii import ascii_title


def main_cli():
    """The main command-line function responsible for sub-functions and allocation separation."""

    # Argument parser and color print.
    parser = create_parser()
    args = parser.parse_args()

    # Print nice asci text.
    ascii_title("mdsanima cli")

    try:
        if args.command == "check":
            cli_check()
        if args.command == "uuid":
            cli_uuid()
        if args.command == "number":
            cli_number()
        if args.command == "logo":
            cli_logo()
        if args.command == "watermark":
            cli_watermark()
        if args.command == "jpg":
            cli_jpg()
        if args.command == "png":
            cli_png()
        if args.command == "webp":
            cli_webp()
        if args.command == "pixelart":
            cli_pixelart()
        if args.command == "grid":
            cli_grid()
        if args.command == "thumbnail":
            cli_thumbnail()
    except AttributeError:
        parser.print_help()
