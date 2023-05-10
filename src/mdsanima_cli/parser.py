# Copyright © 2023 Marcin Różewski MDSANIMA


"""This is a functionality for parsing arguments in command-line tools."""


from __future__ import annotations

import argparse
from typing import Final

from mdsanima_cli._version import __version__


PROG: Final[str] = "mdsanima"
DESC: Final[str] = "MDSANIMA CLI is a command-line interface for image processing."
EPIL: Final[str] = "Copyright \U000000A9 2023 Marcin Różewski MDSANIMA"

ALL_IMAGES_DIR: Final[str] = "all images file inside the current directory."
SUBPERSER_DESC: Final[str] = f"All commands execute on {ALL_IMAGES_DIR}"

CHECK_COMD: Final[str] = "check"
CHECK_DESC: Final[str] = f"Print statistic info about {ALL_IMAGES_DIR}"
CHECK_HELP: Final[str] = "print directory info"

UUID_COMD: Final[str] = "uuid"
UUID_DESC: Final[str] = f"Rename to UUID {ALL_IMAGES_DIR}"
UUID_HELP: Final[str] = "rename to uuid"

NUMBER_COMD: Final[str] = "number"
NUMBER_DESC: Final[str] = f"Rename to sequential numbers {ALL_IMAGES_DIR}"
NUMBER_HELP: Final[str] = "rename to seq numbers"

LOGO_COMD: Final[str] = "logo"
LOGO_DESC: Final[str] = f"Append a logo to {ALL_IMAGES_DIR}"
LOGO_HELP: Final[str] = "append a logo"

WATERMARK_COMD: Final[str] = "watermark"
WATERMARK_DESC: Final[str] = f"Append a watermark to {ALL_IMAGES_DIR}"
WATERMARK_HELP: Final[str] = "append a watermark"

JPG_COMD: Final[str] = "jpg"
JPG_DESC: Final[str] = f"Convert to JPG format {ALL_IMAGES_DIR}"
JPG_HELP: Final[str] = "convert to jpg"

PNG_COMD: Final[str] = "png"
PNG_DESC: Final[str] = f"Convert to PNG format {ALL_IMAGES_DIR}"
PNG_HELP: Final[str] = "convert to png"

WEBP_COMD: Final[str] = "webp"
WEBP_DESC: Final[str] = f"Convert to WebP format {ALL_IMAGES_DIR}"
WEBP_HELP: Final[str] = "convert to webp"

PIXELART_COMD: Final[str] = "pixelart"
PIXELART_DESC: Final[str] = f"Generate pixel art 32px from {ALL_IMAGES_DIR}"
PIXELART_HELP: Final[str] = "generate pixel art 32px"

GRID_COMD: Final[str] = "grid"
GRID_DESC: Final[str] = f"Generate grid 2x2 from {ALL_IMAGES_DIR}"
GRID_HELP: Final[str] = "generate grid 2x2"

THUMBNAIL_COMD: Final[str] = "thumbnail"
THUMBNAIL_DESC: Final[str] = f"Generate JPEG thumbnails 128px from {ALL_IMAGES_DIR}"
THUMBNAIL_HELP: Final[str] = "generate jpeg thumbnail 128px"

GIFMAKER_COMD: Final[str] = "gifmaker"
GIFMAKER_DESC: Final[str] = f"Generate GIF animation pixel art from {ALL_IMAGES_DIR}"
GIFMAKER_HELP: Final[str] = "generate gif animation pixel art"

RESIZE_COMD: Final[str] = "resize"
RESIZE_DESC: Final[str] = f"Resizing to 512px width from {ALL_IMAGES_DIR}"
RESIZE_HELP: Final[str] = "resizing to 512px width"


def create_parser() -> None:
    """Creates an argument parser for all available functions in this package."""

    # Create top level parser for mdsanima command.
    help_formatter = argparse.RawTextHelpFormatter
    parser = argparse.ArgumentParser(prog=PROG, description=DESC, epilog=EPIL, formatter_class=help_formatter)
    parser.add_argument("-v", "--version", action="version", version="%(prog)s-cli " + __version__)
    subparser = parser.add_subparsers(title="commands", description=SUBPERSER_DESC)

    # Create subparser for check command.
    check = subparser.add_parser(name=CHECK_COMD, description=CHECK_DESC, help=CHECK_HELP, epilog=EPIL)
    check.set_defaults(command=CHECK_COMD)

    # Create subparser for uuid command.
    uuid = subparser.add_parser(name=UUID_COMD, description=UUID_DESC, help=UUID_HELP, epilog=EPIL)
    uuid.set_defaults(command=UUID_COMD)

    # Create subparser for number command.
    number = subparser.add_parser(name=NUMBER_COMD, description=NUMBER_DESC, help=NUMBER_HELP, epilog=EPIL)
    number.set_defaults(command=NUMBER_COMD)

    # Create subparser for logo command.
    logo = subparser.add_parser(name=LOGO_COMD, description=LOGO_DESC, help=LOGO_HELP, epilog=EPIL)
    logo.set_defaults(command=LOGO_COMD)

    # Create subparser for watermark command.
    watermark = subparser.add_parser(name=WATERMARK_COMD, description=WATERMARK_DESC, help=WATERMARK_HELP, epilog=EPIL)
    watermark.set_defaults(command=WATERMARK_COMD)

    # Create subparser for jpg command.
    jpg = subparser.add_parser(name=JPG_COMD, description=JPG_DESC, help=JPG_HELP, epilog=EPIL)
    jpg.set_defaults(command=JPG_COMD)

    # Create subparser for png command.
    png = subparser.add_parser(name=PNG_COMD, description=PNG_DESC, help=PNG_HELP, epilog=EPIL)
    png.set_defaults(command=PNG_COMD)

    # Create subparser for webp command.
    webp = subparser.add_parser(name=WEBP_COMD, description=WEBP_DESC, help=WEBP_HELP, epilog=EPIL)
    webp.set_defaults(command=WEBP_COMD)

    # Create subparser for pixelart command.
    pixelart = subparser.add_parser(name=PIXELART_COMD, description=PIXELART_DESC, help=PIXELART_HELP, epilog=EPIL)
    pixelart.set_defaults(command=PIXELART_COMD)

    # Create subparser for grid command.
    grid = subparser.add_parser(name=GRID_COMD, description=GRID_DESC, help=GRID_HELP, epilog=EPIL)
    grid.set_defaults(command=GRID_COMD)

    # Create subparser for thumbnail command.
    thumbnail = subparser.add_parser(name=THUMBNAIL_COMD, description=THUMBNAIL_DESC, help=THUMBNAIL_HELP, epilog=EPIL)
    thumbnail.set_defaults(command=THUMBNAIL_COMD)

    # Create subparser for gifmaker command.
    gifmaker = subparser.add_parser(name=GIFMAKER_COMD, description=GIFMAKER_DESC, help=GIFMAKER_HELP, epilog=EPIL)
    gifmaker.set_defaults(command=GIFMAKER_COMD)

    # Create subparser for resize command.
    resize = subparser.add_parser(name=RESIZE_COMD, description=RESIZE_DESC, help=RESIZE_HELP, epilog=EPIL)
    resize.set_defaults(command=RESIZE_COMD)

    return parser
