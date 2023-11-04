# Copyright (c) 2023 MDSANIMA

"""Change the width of image to 512 pixels. It operates within a specified folder and can process all images at once."""


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
def generate_resize(image_path: str, new_name: str, resolution_width: int) -> None:
    """Resize image, and then save the result with a new name and exif data."""

    # Open image file.
    image = Image.open(image_path)

    # Image size.
    image_widht, image_height = image.size

    # Calculating resolution for image.
    resize_ratio = int(image_widht / resolution_width)
    resize_widht = int(image_widht / resize_ratio)
    resize_height = int(image_height / resize_ratio)
    resize_size = (resize_widht, resize_height)

    # New size for image.
    image_resized = image.resize(resize_size)

    # Add exif data.
    exif_bytes = get_exif_bytes(f"{Command.RESIZE.help}")

    # Save the result.
    image_resized.save(new_name, exif=exif_bytes)


@timer
def compute_resize() -> None:
    """Resizing all images in the current directory to 512px width."""

    # Get directory stats info.
    directory = os.listdir()
    count = 1

    # New file name suffix for generated files.
    suffix = "_resized"
    png = ".png"
    jpg = ".jpg"
    webp = ".webp"

    # Checking extension and compute resize from all images in directory.
    for file in directory:
        if file.endswith(png) and not file.endswith(suffix + png):
            new_name = file[:-4] + suffix + png
            time_taken = generate_resize(file, new_name, 512)
            print_cli_proc("resizing", count, file, new_name, time_taken)
            count += 1
        if file.endswith(jpg) and not file.endswith(suffix + jpg):
            new_name = file[:-4] + suffix + jpg
            time_taken = generate_resize(file, new_name, 512)
            print_cli_proc("resizing", count, file, new_name, time_taken)
            count += 1
        if file.endswith(webp) and not file.endswith(suffix + webp):
            new_name = file[:-5] + suffix + webp
            time_taken = generate_resize(file, new_name, 512)
            print_cli_proc("resizing", count, file, new_name, time_taken)
            count += 1


def resize() -> None:
    """The main functionality for the `resize` command."""
    directory_statistic(f"{Command.RESIZE.cmd}", f"{Command.RESIZE.help}")
    ascii_title("processing")
    time_taken = compute_resize()
    ascii_title("completed")
    print_cli_done(time_taken)
