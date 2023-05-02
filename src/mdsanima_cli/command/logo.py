# Copyright © 2023 Marcin Różewski MDSANIMA


"""Appendign a logo to all images in the current directory. It operates within a specified folder
and can process all images at once.
"""


from __future__ import annotations

import os

from PIL import Image

from mdsanima_cli.command.check import directory_statistic
from mdsanima_cli.parser import LOGO_COMMAND
from mdsanima_cli.parser import LOGO_HELP
from mdsanima_cli.utils.ascii import ascii_title
from mdsanima_cli.utils.exif import get_exif_bytes
from mdsanima_cli.utils.print import print_cli_data
from mdsanima_cli.utils.print import print_cli_done
from mdsanima_cli.utils.print import print_cli_proc
from mdsanima_cli.utils.timer import timer


LOGO_PATH = os.path.expanduser("~/.mdsanima-cli/config/img/logo.png")


@timer
def append_logo(image_path: str, logo_path: str, new_name: str) -> None:
    """Append a logo to one image in the bottom right position, and then save the result with a new
    name and exif data.
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

    # Add exif data.
    exif_bytes = get_exif_bytes(LOGO_HELP)

    # Append logo to image and save.
    image.paste(logo, (position_x, position_y), logo)
    image.save(new_name, exif=exif_bytes)


@timer
def compute_logo() -> None:
    """Computing all images in the current directory with appending a logo."""

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
            time_taken = append_logo(file, LOGO_PATH, new_name)
            print_cli_proc("computing", count, file, new_name, time_taken)
            count += 1
        if file.endswith(jpg) and not file.endswith(suffix + jpg):
            new_name = file[:-4] + suffix + jpg
            time_taken = append_logo(file, LOGO_PATH, new_name)
            print_cli_proc("computing", count, file, new_name, time_taken)
            count += 1
        if file.endswith(webp) and not file.endswith(suffix + webp):
            new_name = file[:-5] + suffix + webp
            time_taken = append_logo(file, LOGO_PATH, new_name)
            print_cli_proc("computing", count, file, new_name, time_taken)
            count += 1


def cli_logo() -> None:
    """Main function for `logo` command."""
    directory_statistic(LOGO_COMMAND, LOGO_HELP)

    try:
        ascii_title("processing")
        time_taken = compute_logo()
        ascii_title("completed")
        print_cli_done(time_taken)
    except FileNotFoundError:
        ascii_title("config error")
        warning = "Put your logo here '" + LOGO_PATH + "' to continue!"
        print_cli_data("warning logo", warning, 197, 209, 38)
