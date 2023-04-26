# Copyright © 2023 Marcin Różewski MDSANIMA


"""This module is designed to adding a logo to all images in the current
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


LOGO = os.path.expanduser("~/.mdsanima-cli/config/img/logo.png")


def append_logo(image_path: str, logo_path: str, new_name: str) -> None:
    """Append a logo to one image in the bottom right position, and then save
    the result with a new file name.
    """

    # Open image and logo file.
    image = Image.open(image_path)
    logo = Image.open(logo_path)

    # Image and logo size.
    image_width, image_height = image.size
    logo_width, logo_height = logo.size

    # Calculating size for logo.
    resize_ratio = 0.05
    new_logo_width = int(image_width * resize_ratio)
    new_logo_height = int(logo_height * new_logo_width / logo_width)
    logo = logo.resize((new_logo_width, new_logo_height))

    # Calculating position for appending logo.
    position_x = image_width - new_logo_width
    position_y = image_height - new_logo_height

    # Append logo to image and save.
    image.paste(logo, (position_x, position_y), logo)
    image.save(new_name)


def compute_logo() -> None:
    """Add a logo to all images in the current directory and save them with a
    new file name that includes the logo.
    """

    # Get directory stats info.
    directory = os.listdir()
    count = 1

    # New file name suffix for generated files.
    suffix = "_logo"
    png = ".png"
    jpg = ".jpg"
    webp = ".webp"

    # Checking extension and appending logo to all images in directory.
    for file in directory:
        if file.endswith(png) and not file.endswith(suffix + png):
            new_name = file[:-4] + suffix + png
            append_logo(file, LOGO, new_name)
            print_cli_proc("COMPUTE", count, file, new_name)
            count += 1
        if file.endswith(jpg) and not file.endswith(suffix + jpg):
            new_name = file[:-4] + suffix + jpg
            append_logo(file, LOGO, new_name)
            print_cli_proc("COMPUTE", count, file, new_name)
            count += 1
        if file.endswith(webp) and not file.endswith(suffix + webp):
            new_name = file[:-5] + suffix + webp
            append_logo(file, LOGO, new_name)
            print_cli_proc("COMPUTE", count, file, new_name)
            count += 1


def cli_logo() -> None:
    """Main function for `logo` command."""
    print_directory_check("LOGO", "APPENDING A LOGO")
    ascii_title("processing")

    try:
        compute_logo()
    except FileNotFoundError:
        warning = "Put your logo here '" + LOGO + "' to continue!"
        print_cli_data("WARNING LOGO", warning, 197, 209, 38)
