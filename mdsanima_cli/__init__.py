# Copyright (c) 2023 MDSANIMA

"""A command-line tool for image processing, generating pixel art, adding logos to images, and much more."""


from __future__ import annotations

from mdsanima_cli.core import cmd
from mdsanima_cli.core.cli import Command
from mdsanima_cli.core.cli import create_parser
from mdsanima_cli.core.utils.ascii import ascii_title


def cli():
    """The main command-line functionality responsible for sub-functions and allocation separation."""

    # Creating argument parser.
    parser = create_parser()
    args = parser.parse_args()

    # Printing nice color ascii title.
    ascii_title("mdsanima cli")

    try:
        if args.COMMAND is None:
            parser.print_help()
        if args.COMMAND == f"{Command.CHECK.cmd}":
            cmd.check()
        if args.COMMAND == f"{Command.LOGO.cmd}":
            cmd.logo()
        if args.COMMAND == f"{Command.WATERMARK.cmd}":
            cmd.watermark()
        if args.COMMAND == f"{Command.NUMBER.cmd}":
            cmd.number()
        if args.COMMAND == f"{Command.UUID.cmd}":
            cmd.uuid()
        if args.COMMAND == f"{Command.RESIZE.cmd}":
            cmd.resize()
        if args.COMMAND == f"{Command.JPG.cmd}":
            cmd.jpg()
        if args.COMMAND == f"{Command.PNG.cmd}":
            cmd.png()
        if args.COMMAND == f"{Command.WEBP.cmd}":
            cmd.webp()
        if args.COMMAND == f"{Command.GRID.cmd}":
            cmd.grid()
        if args.COMMAND == f"{Command.PIXELART.cmd}":
            cmd.pixelart()
        if args.COMMAND == f"{Command.GIFMAKER.cmd}":
            cmd.gifmaker()
        if args.COMMAND == f"{Command.THUMBNAIL.cmd}":
            cmd.thumbnail()
    except AttributeError:
        parser.print_help()
