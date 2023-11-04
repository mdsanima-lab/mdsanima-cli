# Copyright (c) 2023 MDSANIMA

"""A command-line tool for image processing, generating pixel art, adding logos to images, and much more."""


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
from mdsanima_cli.core.cli import create_parser
from mdsanima_cli.utils.ascii import ascii_title


def main_cli():
    """The main command-line functionality responsible for sub-functions and allocation separation."""

    # Creating argument parser.
    parser = create_parser()
    args = parser.parse_args()

    # Printing nice color ascii title.
    ascii_title("mdsanima cli")

    try:
        if args.COMMAND is None:
            parser.print_help()
        if args.COMMAND == "check":
            cli_check()
        if args.COMMAND == "logo":
            cli_logo()
        if args.COMMAND == "watermark":
            cli_watermark()
        if args.COMMAND == "number":
            cli_number()
        if args.COMMAND == "uuid":
            cli_uuid()
        if args.COMMAND == "resize":
            cli_resize()
        if args.COMMAND == "jpg":
            cli_jpg()
        if args.COMMAND == "png":
            cli_png()
        if args.COMMAND == "webp":
            cli_webp()
        if args.COMMAND == "grid":
            cli_grid()
        if args.COMMAND == "pixelart":
            cli_pixelart()
        if args.COMMAND == "gifmaker":
            cli_gifmaker()
        if args.COMMAND == "thumbnail":
            cli_thumbnail()
    except AttributeError:
        parser.print_help()
