# Copyright (c) 2023 MDSANIMA

"""Generating images into pixel art. It operates within a specified folder and can process all images at once. The first
step is to open the original image, scale it to 32 pixels, scale it back to its original size, and then save it.
"""


from __future__ import annotations

import os

from PIL import Image

from mdsanima_cli.core.cli import Command
from mdsanima_cli.core.cmd.check import directory_statistic
from mdsanima_cli.utils.ascii import ascii_title
from mdsanima_cli.utils.exif import get_exif_bytes
from mdsanima_cli.utils.print import print_cli_done
from mdsanima_cli.utils.print import print_cli_proc
from mdsanima_cli.utils.timer import timer


@timer
def generate_pixelart(image_path: str, new_name: str, resolution: int) -> None:
    """Generate pixel art for one image, then save the result with a new name and exif data."""

    # Open image file.
    image = Image.open(image_path)

    # Image size.
    image_width, image_height = image.size

    # Calculating resolution for pixelart.
    resize_ratio = int(image_width / resolution)
    pixelart_width = int(image_width / resize_ratio)
    pixelart_height = int(image_height / resize_ratio)
    pixelart_size = (pixelart_width, pixelart_height)

    # Generate one pixel art.
    small_image = image.resize(pixelart_size, resample=Image.Resampling.BILINEAR)
    result = small_image.resize(image.size, Image.Resampling.NEAREST)

    # Add exif data.
    exif_bytes = get_exif_bytes(f"{Command.PIXELART.help}")

    # Save the result.
    result.save(new_name, exif=exif_bytes)


@timer
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
            time_taken = generate_pixelart(file, new_name, 32)
            print_cli_proc("computing", count, file, new_name, time_taken)
            count += 1
        if file.endswith(jpg) and not file.endswith(suffix + jpg):
            new_name = file[:-4] + suffix + jpg
            time_taken = generate_pixelart(file, new_name, 32)
            print_cli_proc("computing", count, file, new_name, time_taken)
            count += 1
        if file.endswith(webp) and not file.endswith(suffix + webp):
            new_name = file[:-5] + suffix + webp
            time_taken = generate_pixelart(file, new_name, 32)
            print_cli_proc("computing", count, file, new_name, time_taken)
            count += 1


def pixelart() -> None:
    """The main functionality for the `pixelart` command."""
    directory_statistic(f"{Command.PIXELART.cmd}", f"{Command.PIXELART.help}")
    ascii_title("processing")
    time_taken = compute_pixelart()
    ascii_title("completed")
    print_cli_done(time_taken)