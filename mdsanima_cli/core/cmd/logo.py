# Copyright (c) 2023 MDSANIMA

"""Append a logo to image. It operates within a specified folder and can process all images at once."""


from __future__ import annotations

import os

from PIL import Image

from mdsanima_cli.core.cli import Command
from mdsanima_cli.core.cmd.check import directory_statistic
from mdsanima_cli.core.utils.ascii import ascii_title
from mdsanima_cli.core.utils.exif import get_exif_bytes
from mdsanima_cli.core.utils.print import print_cli_data
from mdsanima_cli.core.utils.print import print_cli_done
from mdsanima_cli.core.utils.print import print_cli_proc
from mdsanima_cli.core.utils.timer import timer


LOGO_PATH = os.path.expanduser("~/.mdsanima-cli/config/img/logo.png")


@timer
def append_logo(image_path: str, logo_path: str, new_name: str) -> None:
    """Append a logo to one image in the bottom right position, then save the result with a new name and exif data."""

    image = Image.open(image_path)
    _logo = Image.open(logo_path)

    image_width, image_height = image.size
    logo_width, logo_height = _logo.size

    resize_ratio = 0.05
    new_logo_width = int(image_width * resize_ratio)
    new_logo_height = int(logo_height * new_logo_width / logo_width)
    _logo = _logo.resize((new_logo_width, new_logo_height))

    position_x = image_width - new_logo_width
    position_y = image_height - new_logo_height

    exif_bytes = get_exif_bytes(f"{Command.LOGO.help}")
    image.paste(_logo, (position_x, position_y), _logo)
    image.save(new_name, exif=exif_bytes)


@timer
def compute_logo() -> None:
    """Computing all images in the current directory with appending a logo."""

    directory = os.listdir()
    count = 1

    _suffix = "_logo"
    _png = ".png"
    _jpg = ".jpg"
    _webp = ".webp"

    for file in directory:
        if file.endswith(_png) and not file.endswith(_suffix + _png):
            new_name = file[:-4] + _suffix + _png
            time_taken = append_logo(file, LOGO_PATH, new_name)
            print_cli_proc("computing", count, file, new_name, time_taken)
            count += 1
        if file.endswith(_jpg) and not file.endswith(_suffix + _jpg):
            new_name = file[:-4] + _suffix + _jpg
            time_taken = append_logo(file, LOGO_PATH, new_name)
            print_cli_proc("computing", count, file, new_name, time_taken)
            count += 1
        if file.endswith(_webp) and not file.endswith(_suffix + _webp):
            new_name = file[:-5] + _suffix + _webp
            time_taken = append_logo(file, LOGO_PATH, new_name)
            print_cli_proc("computing", count, file, new_name, time_taken)
            count += 1


def logo() -> None:
    """The main functionality for the `logo` command."""

    directory_statistic(f"{Command.LOGO.cmd}", f"{Command.LOGO.help}")

    try:
        ascii_title("processing")
        time_taken = compute_logo()
        ascii_title("completed")
        print_cli_done(time_taken)
    except FileNotFoundError:
        ascii_title("config error")
        warning = "Put your logo here '" + LOGO_PATH + "' to continue!"
        print_cli_data("warning logo", warning, 197, 209, 38)
