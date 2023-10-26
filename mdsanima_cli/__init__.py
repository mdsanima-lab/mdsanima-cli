# Copyright (c) 2023 MDSANIMA


"""Initial main functionality for command-line tools."""


from __future__ import annotations

from mdsanima_cli.commands.check import cli_check
from mdsanima_cli.commands.gifmaker import cli_gifmaker
from mdsanima_cli.commands.grid import cli_grid
from mdsanima_cli.commands.jpg import cli_jpg
from mdsanima_cli.commands.logo import cli_logo
from mdsanima_cli.commands.number import cli_number
from mdsanima_cli.commands.pixelart import cli_pixelart
from mdsanima_cli.commands.png import cli_png
from mdsanima_cli.commands.resize import cli_resize
from mdsanima_cli.commands.thumbnail import cli_thumbnail
from mdsanima_cli.commands.uuids import cli_uuid
from mdsanima_cli.commands.watermark import cli_watermark
from mdsanima_cli.commands.webp import cli_webp
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
        if args.command == "gifmaker":
            cli_gifmaker()
        if args.command == "resize":
            cli_resize()
    except AttributeError:
        parser.print_help()
