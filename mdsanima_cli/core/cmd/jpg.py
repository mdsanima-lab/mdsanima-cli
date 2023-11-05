# Copyright (c) 2023 MDSANIMA

"""Convert images to JPG format. It operates within a specified folder and can process all images at once."""


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
def convert_to_jpg(image_path: str, new_name: str) -> None:
    """Convert a image to JPG format, and then save the result with a new name and exif data."""

    image = Image.open(image_path)
    exif_bytes = get_exif_bytes(f"{Command.JPG.help}")
    image.save(new_name, "JPEG", exif=exif_bytes)


@timer
def compute_jpg() -> None:
    """Computing all images in the current directory to JPG format."""

    directory = os.listdir()
    count = 1

    _suffix = "_converted"
    _png = ".png"
    _jpg = ".jpg"
    _webp = ".webp"

    for file in directory:
        if file.endswith(_png) and not file.endswith(_suffix + _jpg):
            new_name = file[:-4] + _suffix + _jpg
            time_taken = convert_to_jpg(file, new_name)
            print_cli_proc("converting", count, file, new_name, time_taken)
            count += 1
        if file.endswith(_jpg) and not file.endswith(_suffix + _jpg):
            new_name = file[:-4] + _suffix + _jpg
            time_taken = convert_to_jpg(file, new_name)
            print_cli_proc("converting", count, file, new_name, time_taken)
            count += 1
        if file.endswith(_webp) and not file.endswith(_suffix + _jpg):
            new_name = file[:-5] + _suffix + _jpg
            time_taken = convert_to_jpg(file, new_name)
            print_cli_proc("converting", count, file, new_name, time_taken)
            count += 1


def jpg() -> None:
    """The main functionality for the `jpg` command."""

    directory_statistic(f"{Command.JPG.cmd}", f"{Command.JPG.help}")

    ascii_title("processing")
    time_taken = compute_jpg()
    ascii_title("completed")
    print_cli_done(time_taken)
