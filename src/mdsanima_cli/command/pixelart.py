# Copyright © 2023 Marcin Różewski MDSANIMA


"""Generating images into pixel art. It operates within a specified folder and can process all
images at once. The first step is to open the original image, scale it to 32x32 pixels, scale it
back to its original size, and then save it.
"""


from __future__ import annotations

import os

from PIL import Image

from mdsanima_cli.command.check import directory_statistic
from mdsanima_cli.parser import PIXELART_COMMAND
from mdsanima_cli.parser import PIXELART_HELP
from mdsanima_cli.utils.ascii import ascii_title
from mdsanima_cli.utils.exif import get_exif_bytes
from mdsanima_cli.utils.print import print_cli_proc


def generate_pixelart(image_path: str, new_name: str, res: int) -> None:
    """Generate pixel art for one image, then save the result with a new name and exif data."""

    # Open image file.
    image = Image.open(image_path)

    # Generate one pixel art.
    small_image = image.resize((res, res), resample=Image.Resampling.BILINEAR)
    result = small_image.resize(image.size, Image.Resampling.NEAREST)

    # Add exif data.
    exif_bytes = get_exif_bytes(PIXELART_HELP)

    # Save the result.
    result.save(new_name, exif=exif_bytes)


def compute_pixelart() -> None:
    """Computing pixel art for all images in the directory."""

    # Get directory stats info.
    directory = os.listdir()
    count = 1

    # New file name end for generated files.
    suffix = "_pixelart"
    png = ".png"
    jpg = ".jpg"
    webp = ".webp"

    # Checking extension and generate pixel art for all images in directory.
    for file in directory:
        if file.endswith(png) and not file.endswith(suffix + png):
            new_name = file[:-4] + suffix + png
            generate_pixelart(file, new_name, 32)
            print_cli_proc("computing", count, file, new_name)
            count += 1
        if file.endswith(jpg) and not file.endswith(suffix + jpg):
            new_name = file[:-4] + suffix + jpg
            generate_pixelart(file, new_name, 32)
            print_cli_proc("computing", count, file, new_name)
            count += 1
        if file.endswith(webp) and not file.endswith(suffix + webp):
            new_name = file[:-5] + suffix + webp
            generate_pixelart(file, new_name, 32)
            print_cli_proc("computing", count, file, new_name)
            count += 1


def cli_pixelart() -> None:
    """Main function for `pixelart` command."""
    directory_statistic(PIXELART_COMMAND, PIXELART_HELP)
    ascii_title("processing")
    compute_pixelart()