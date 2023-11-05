# Copyright (c) 2023 MDSANIMA

"""Generating images into pixel art. It operates within a specified folder and can process all images at once. The first
step is to open the original image, scale it to 32 pixels, scale it back to its original size, and then save it.
"""


from __future__ import annotations

import os

from PIL import Image

from mdsanima_cli.core.cli import Command
from mdsanima_cli.core.cmd.check import directory_statistic
from mdsanima_cli.core.utils.ascii import ascii_title
from mdsanima_cli.core.utils.exif import get_exif_bytes
from mdsanima_cli.core.utils.print import print_cli_done
from mdsanima_cli.core.utils.print import print_cli_proc
from mdsanima_cli.core.utils.timer import timer


@timer
def generate_pixelart(image_path: str, new_name: str, resolution: int) -> None:
    """Generate pixel art for one image, then save the result with a new name and exif data."""

    image = Image.open(image_path)

    image_width, image_height = image.size

    resize_ratio = int(image_width / resolution)
    pixelart_width = int(image_width / resize_ratio)
    pixelart_height = int(image_height / resize_ratio)
    pixelart_size = (pixelart_width, pixelart_height)

    small_image = image.resize(pixelart_size, resample=Image.Resampling.BILINEAR)
    result = small_image.resize(image.size, Image.Resampling.NEAREST)

    exif_bytes = get_exif_bytes(f"{Command.PIXELART.help}")
    result.save(new_name, exif=exif_bytes)


@timer
def compute_pixelart() -> None:
    """Computing pixel art for all images in the directory."""

    directory = os.listdir()
    count = 1

    _suffix = "_pixelart"
    _png = ".png"
    _jpg = ".jpg"
    _webp = ".webp"

    for file in directory:
        if file.endswith(_png) and not file.endswith(_suffix + _png):
            new_name = file[:-4] + _suffix + _png
            time_taken = generate_pixelart(file, new_name, 32)
            print_cli_proc("computing", count, file, new_name, time_taken)
            count += 1
        if file.endswith(_jpg) and not file.endswith(_suffix + _jpg):
            new_name = file[:-4] + _suffix + _jpg
            time_taken = generate_pixelart(file, new_name, 32)
            print_cli_proc("computing", count, file, new_name, time_taken)
            count += 1
        if file.endswith(_webp) and not file.endswith(_suffix + _webp):
            new_name = file[:-5] + _suffix + _webp
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
