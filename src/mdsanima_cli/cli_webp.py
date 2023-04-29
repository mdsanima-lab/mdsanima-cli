# Copyright © 2023 Marcin Różewski MDSANIMA


"""This module is designed to converting images to WebP format from all images
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


COMMAND = "webp"
INFO = "converting to webp format"


def convert_webp(image_path: str, new_name: str) -> None:
    """Converting a image to WebP format, and then save the result with a new
    file name. Adding exif data.
    """

    # Open image file.
    image = Image.open(image_path)

    # Add exif data.
    exif_bytes = get_exif_bytes(INFO)

    # Save the result.
    image.save(new_name, exif=exif_bytes)


def compute_webp() -> None:
    """Computing all images in the current directory to WebP format and save
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

    # Checking extension and compute convert webp from all images in directory.
    for file in directory:
        if file.endswith(png) and not file.endswith(suffix + webp):
            new_name = file[:-4] + suffix + webp
            convert_webp(file, new_name)
            print_cli_proc("converting", count, file, new_name)
            count += 1
        if file.endswith(jpg) and not file.endswith(suffix + webp):
            new_name = file[:-4] + suffix + webp
            convert_webp(file, new_name)
            print_cli_proc("converting", count, file, new_name)
            count += 1
        if file.endswith(webp) and not file.endswith(suffix + webp):
            new_name = file[:-5] + suffix + webp
            convert_webp(file, new_name)
            print_cli_proc("converting", count, file, new_name)
            count += 1


def cli_webp() -> None:
    """Main function for `webp` command."""
    print_directory_check(COMMAND, INFO)
    ascii_title("processing")
    compute_webp()
