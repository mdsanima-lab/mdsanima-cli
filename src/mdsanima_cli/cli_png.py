# Copyright © 2023 Marcin Różewski MDSANIMA


"""This module is designed to converting images to PNG format from all images
in the curreny directory. It operates within a specified folder and can process
all images at once.
"""


from __future__ import annotations

import os

from PIL import Image

from .ascii import ascii_title
from .exif import get_exif_bytes
from .mprints import print_cli_proc

from .cli_check import print_directory_check


def convert_png(image_path: str, new_name: str) -> None:
    """Converting a image to PNG format, and then save the result with a new
    file name. Adding exif data.
    """

    # Open image file.
    image = Image.open(image_path)

    # Add exif data.
    exif_bytes = get_exif_bytes("with png")

    # Save the result.
    image.save(new_name, "PNG", exif=exif_bytes)


def compute_png() -> None:
    """Computing all images in the current directory to PNG format and save
    them with a new file name.
    """

    # Get directory stats info.
    directory = os.listdir()
    count = 1

    # New file name suffix for generated files.
    suffix = "_converted"
    png = ".png"
    jpg = ".jpg"
    webp = ".webp"

    # Checking extension and compute convert png from all images in directory.
    for file in directory:
        if file.endswith(png) and not file.endswith(suffix + png):
            new_name = file[:-4] + suffix + png
            convert_png(file, new_name)
            print_cli_proc("CONVERTING", count, file, new_name)
            count += 1
        if file.endswith(jpg) and not file.endswith(suffix + png):
            new_name = file[:-4] + suffix + png
            convert_png(file, new_name)
            print_cli_proc("CONVERTING", count, file, new_name)
            count += 1
        if file.endswith(webp) and not file.endswith(suffix + png):
            new_name = file[:-5] + suffix + png
            convert_png(file, new_name)
            print_cli_proc("CONVERTING", count, file, new_name)
            count += 1


def cli_png() -> None:
    """Main function for `png` command."""
    print_directory_check("PNG", "CONVERTING TO PNG")
    ascii_title("processing")
    compute_png()
