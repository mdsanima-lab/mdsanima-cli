# Copyright © 2023 Marcin Różewski MDSANIMA


"""This module is designed to adding a watermark to all images in the current directory. It operates
within a specified folder and can process all images at once.
"""


from __future__ import annotations

import os

from PIL import Image

from mdsanima_cli.command.check import directory_statistic
from mdsanima_cli.parser import WATERMARK_COMMAND
from mdsanima_cli.parser import WATERMARK_HELP
from mdsanima_cli.utils.ascii import ascii_title
from mdsanima_cli.utils.exif import get_exif_bytes
from mdsanima_cli.utils.print import print_cli_data
from mdsanima_cli.utils.print import print_cli_done
from mdsanima_cli.utils.print import print_cli_proc
from mdsanima_cli.utils.timer import timer


WATERMARK_PATH = os.path.expanduser("~/.mdsanima-cli/config/img/watermark.png")


@timer
def append_watermark(image_path: str, waterm_path: str, new_name: str) -> None:
    """Append a watermark to one image, and then save the result with a new name and exif data.
    The watermark is a rotated on 45 degrees and shifted.
    """

    # Open image and watermark file.
    image = Image.open(image_path)
    watermark = Image.open(waterm_path)

    # Image and watermark size.
    image_width, _image_height = image.size
    watermark_width, watermark_height = watermark.size

    # Calculating size for watermark.
    resize_ratio = 0.25
    new_watermark_width = int(image_width * resize_ratio)
    new_watermark_height = int(watermark_height * new_watermark_width / watermark_width)

    # Resizing and rotating watermark.
    watermark = watermark.resize((new_watermark_width, new_watermark_height)).rotate(45, expand=1)

    # Rotate watermark size.
    rotate_watermark_width, rotate_watermark_height = watermark.size

    # Background helper size.
    bg_size = int(image_width * resize_ratio)
    bg_half = int(bg_size / 2)

    # Calculating position for background helper.
    position_x = int(bg_half - rotate_watermark_width / 2)
    position_y = int(bg_half - rotate_watermark_height / 2)

    # New background helper for watermark position.
    watermark_bg = Image.new("RGBA", (bg_size, bg_size), (0, 0, 0, 0))
    watermark_bg.paste(watermark, (position_x, position_y), watermark)

    # Append and shift rotated watermakr to image.
    for row in range(10):
        for col in range(10):
            width = int(-bg_half + bg_size * row)
            height = int(-bg_half + bg_size * col)
            image.paste(watermark_bg, (width, height), watermark_bg)

    # Add exif data.
    exif_bytes = get_exif_bytes(WATERMARK_HELP)

    # Save the result.
    image.save(new_name, exif=exif_bytes)


@timer
def compute_watermark() -> None:
    """Add a watermark to all images in the current directory that includes the watermark."""

    # Get directory stats info.
    directory = os.listdir()
    count = 1

    # New file name suffix for generated files.
    suffix = "_watermark"
    png = ".png"
    jpg = ".jpg"
    webp = ".webp"

    # Checking extension and appending watermark to all images in directory.
    for file in directory:
        if file.endswith(png) and not file.endswith(suffix + png):
            new_name = file[:-4] + suffix + png
            time_taken = append_watermark(file, WATERMARK_PATH, new_name)
            print_cli_proc("computing", count, file, new_name, time_taken)
            count += 1
        if file.endswith(jpg) and not file.endswith(suffix + jpg):
            new_name = file[:-4] + suffix + jpg
            time_taken = append_watermark(file, WATERMARK_PATH, new_name)
            print_cli_proc("computing", count, file, new_name, time_taken)
            count += 1
        if file.endswith(webp) and not file.endswith(suffix + webp):
            new_name = file[:-5] + suffix + webp
            time_taken = append_watermark(file, WATERMARK_PATH, new_name)
            print_cli_proc("computing", count, file, new_name, time_taken)
            count += 1


def cli_watermark() -> None:
    """Main function for `watermark` command."""
    directory_statistic(WATERMARK_COMMAND, WATERMARK_HELP)

    try:
        ascii_title("processing")
        time_taken = compute_watermark()
        ascii_title("completed")
        print_cli_done(time_taken)
    except FileNotFoundError:
        ascii_title("config error")
        warning = "Put your watermark here '" + WATERMARK_PATH + "' to continue!"
        print_cli_data("warning watermark", warning, 197, 209, 38)
