# Copyright © 2023 Marcin Różewski MDSANIMA


"""Generating JPEG thumbnails from all images in the curreny directory. It operates within
a specified folder and can process all images at once.
"""


from __future__ import annotations

import os

from PIL import Image

from mdsanima_cli.command.check import directory_statistic
from mdsanima_cli.parser import THUMBNAIL_COMMAND
from mdsanima_cli.parser import THUMBNAIL_HELP
from mdsanima_cli.utils.ascii import ascii_title
from mdsanima_cli.utils.exif import get_exif_bytes
from mdsanima_cli.utils.print import print_cli_done
from mdsanima_cli.utils.print import print_cli_proc
from mdsanima_cli.utils.timer import timer


@timer
def generate_jpeg_thumbnail(image_path: str, new_name: str) -> None:
    """Generate JPEG thumbnail 128, and then save the result with a new name and exif data."""

    # Open image file.
    image = Image.open(image_path)

    # Image size.
    image_width, image_height = image.size

    # Calculating size for thumbnail.
    size = 128
    resize_ratio = int(image_width / size)
    thumbnail_width = int(image_width / resize_ratio)
    thumbnail_height = int(image_height / resize_ratio)
    thumbnail_size = (thumbnail_width, thumbnail_height)

    # Add exif data.
    exif_bytes = get_exif_bytes(THUMBNAIL_HELP)

    # Create JPEG thumbnail and save the result.
    image.thumbnail(thumbnail_size)
    image.save(new_name, "JPEG", exif=exif_bytes)


@timer
def compute_thumbnail() -> None:
    """Generating JPEG thumbnails 128 from all images in the current directory."""

    # Get directory stats info.
    directory = os.listdir()
    count = 1

    # New file name suffix for generated files.
    suffix = "_thumbnail"
    png = ".png"
    jpg = ".jpg"
    webp = ".webp"

    # Checking extension and compute thumbnail from all images in directory.
    for file in directory:
        if file.endswith(png) and not file.endswith(suffix + jpg):
            new_name = file[:-4] + suffix + jpg
            time_teken = generate_jpeg_thumbnail(file, new_name)
            print_cli_proc("computing", count, file, new_name, time_teken)
            count += 1
        if file.endswith(jpg) and not file.endswith(suffix + jpg):
            new_name = file[:-4] + suffix + jpg
            time_teken = generate_jpeg_thumbnail(file, new_name)
            print_cli_proc("computing", count, file, new_name, time_teken)
            count += 1
        if file.endswith(webp) and not file.endswith(suffix + jpg):
            new_name = file[:-5] + suffix + jpg
            time_teken = generate_jpeg_thumbnail(file, new_name)
            print_cli_proc("computing", count, file, new_name, time_teken)
            count += 1


def cli_thumbnail() -> None:
    """Main function for `thumbnail` command."""
    directory_statistic(THUMBNAIL_COMMAND, THUMBNAIL_HELP)
    ascii_title("processing")
    time_taken = compute_thumbnail()
    ascii_title("completed")
    print_cli_done(time_taken)
