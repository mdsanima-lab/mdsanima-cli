# Copyright (c) 2023 MDSANIMA

"""A command configuration for the subparsers."""


from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from enum import auto

from mdsanima_cli.core.enums import AutoNameLower


IMAGES = "all image files inside the current directory"


class _SubCommandAction(Enum):
    """Action for subparsers command."""

    def add_parser(self, subparsers):
        """Create and add a subparser for the command."""
        _desc = self.value.description
        return subparsers.add_parser(name=self.value.cmd, help=self.value.help, description=_desc, add_help=False)

    @property
    def show(self) -> str:
        """Returning the string value of the `cmd` subcommand name as a property."""
        return self.value.cmd


@dataclass
class SubCommandDataMixin:
    """Mixin for subcommand data types used in subparsers, displayed in the command-line interface help."""

    cmd: str
    """The name of the `CLI` command used for dataset processing."""
    help: str
    """The short help text about the `CLI` command that is displayed in the command-line interface help."""
    description: str
    """The long help description text that provides detailed information about the `CLI` command."""


class Command(SubCommandDataMixin, _SubCommandAction, AutoNameLower):
    """A command config for the subparsers parameter. The order indicates current position in the help printing."""

    CHECK = auto(), "Show directory info", f"Show directory statistics information about {IMAGES}."
    LOGO = auto(), "Append a logo", f"Append a logo on the right bottom corner to {IMAGES}."
    WATERMARK = auto(), "Append a watermark", f"Append a watermark multiple times at an angle to {IMAGES}."
    NUMBER = auto(), "Rename to seq numbers", f"Rename to sequential numbers {IMAGES}."
    UUID = auto(), "Rename to UUID", f"Rename to universally unique identifiers UUID {IMAGES}."
    RESIZE = auto(), "Resize to 512px", f"Change the width of {IMAGES} to 512 pixels."
    JPG = auto(), "Convert to JPG", f"Convert to JPG format {IMAGES}."
    PNG = auto(), "Convert to PNG", f"Convert to PNG format {IMAGES}."
    WEBP = auto(), "Convert to WebP", f"Convert to WebP format {IMAGES}."
    GRID = auto(), "Generate 2x2 grid", f"Generate 2x2 grid from {IMAGES}."
    PIXELART = auto(), "Generate pixel art", f"Generate pixel art from {IMAGES} on 32 pixels quality."
    GIFMAKER = auto(), "Generate GIF animation", f"Generate GIF pixel art animation from {IMAGES}."
    THUMBNAIL = auto(), "Generate JPG thumbnail", f"Generate JPG thumbnail 128 pixels width from {IMAGES}."
