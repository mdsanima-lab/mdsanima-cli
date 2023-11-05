# Copyright (c) 2023 MDSANIMA


"""Generating JPEG thumbnails from all images in the curreny directory. It operates within a specified folder and can
process all images at once.
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
def generate_jpeg_thumbnail(image_path: str, new_name: str, resolution: int) -> None:
    """Generate JPEG thumbnail, and then save the result with a new name and exif data."""

    image = Image.open(image_path)

    image_width, image_height = image.size

    resize_ratio = int(image_width / resolution)
    thumbnail_width = int(image_width / resize_ratio)
    thumbnail_height = int(image_height / resize_ratio)
    thumbnail_size = (thumbnail_width, thumbnail_height)

    exif_bytes = get_exif_bytes(f"{Command.THUMBNAIL.help}")
    image.thumbnail(thumbnail_size)
    image.save(new_name, "JPEG", exif=exif_bytes)


@timer
def compute_thumbnail() -> None:
    """Generating JPEG thumbnails 128 from all images in the current directory."""

    directory = os.listdir()
    count = 1

    _suffix = "_thumbnail"
    _png = ".png"
    _jpg = ".jpg"
    _webp = ".webp"

    for file in directory:
        if file.endswith(_png) and not file.endswith(_suffix + _jpg):
            new_name = file[:-4] + _suffix + _jpg
            time_teken = generate_jpeg_thumbnail(file, new_name, 128)
            print_cli_proc("computing", count, file, new_name, time_teken)
            count += 1
        if file.endswith(_jpg) and not file.endswith(_suffix + _jpg):
            new_name = file[:-4] + _suffix + _jpg
            time_teken = generate_jpeg_thumbnail(file, new_name, 128)
            print_cli_proc("computing", count, file, new_name, time_teken)
            count += 1
        if file.endswith(_webp) and not file.endswith(_suffix + _jpg):
            new_name = file[:-5] + _suffix + _jpg
            time_teken = generate_jpeg_thumbnail(file, new_name, 128)
            print_cli_proc("computing", count, file, new_name, time_teken)
            count += 1


def thumbnail() -> None:
    """The main functionality for the `thumbnail` command."""

    directory_statistic(f"{Command.THUMBNAIL.cmd}", f"{Command.THUMBNAIL.help}")

    ascii_title("processing")
    time_taken = compute_thumbnail()
    ascii_title("completed")
    print_cli_done(time_taken)
