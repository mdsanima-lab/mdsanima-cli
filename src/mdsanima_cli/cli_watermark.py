# Copyright © 2023 Marcin Różewski MDSANIMA


"""This module is designed to adding a watermark to all images in the current
directory. It operates within a specified folder and can process all images at
once.
"""


from __future__ import annotations

import os
from PIL import Image

from .ascii import ascii_title
from .mprints import print_cli_data
from .mprints import print_cli_proc

from .cli_check import print_directory_check


WATERMARK = os.path.expanduser("~/.mdsanima-cli/config/img/watermark.png")


def append_watermark(image_path: str, waterm_path: str, new_name: str) -> None:
    """Append a watermark to one image, and then save the result with a new
    file name. The watermark is a rotated on 45 degrees and shifted.
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
    new_watermark_height = int(
        watermark_height * new_watermark_width / watermark_width
    )

    # Resizing and rotating watermark.
    watermark = watermark.resize(
        (new_watermark_width, new_watermark_height)
    ).rotate(45, expand=1)

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

    # Save the result.
    image.save(new_name)


def compute_watermark() -> None:
    """Add a watermark to all images in the current directory and save them
    with a new file name that includes the watermark.
    """

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
            append_watermark(file, WATERMARK, new_name)
            print_cli_proc("COMPUTE", count, file, new_name)
            count += 1
        if file.endswith(jpg) and not file.endswith(suffix + jpg):
            new_name = file[:-4] + suffix + jpg
            append_watermark(file, WATERMARK, new_name)
            print_cli_proc("COMPUTE", count, file, new_name)
            count += 1
        if file.endswith(webp) and not file.endswith(suffix + webp):
            new_name = file[:-5] + suffix + webp
            append_watermark(file, WATERMARK, new_name)
            print_cli_proc("COMPUTE", count, file, new_name)
            count += 1


def cli_watermark() -> None:
    """Main function for `watermark` command."""
    print_directory_check("WATERMARK", "APPENDING A WATERMARK")
    ascii_title("processing")

    try:
        compute_watermark()
    except FileNotFoundError:
        warning = "Put your watermakr here '" + WATERMARK + "' to continue!"
        print_cli_data("WARNING WATE", warning, 197, 209, 38)
