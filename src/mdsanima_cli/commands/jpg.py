# Copyright (c) 2023 MDSANIMA


"""Converting images to JPG format from all images in the curreny directory. It operates within a specified folder and
can process all images at once.
"""


from __future__ import annotations

import os

from PIL import Image

from mdsanima_cli.commands.check import directory_statistic
from mdsanima_cli.parser import JPG_COMD
from mdsanima_cli.parser import JPG_HELP
from mdsanima_cli.utils.ascii import ascii_title
from mdsanima_cli.utils.exif import get_exif_bytes
from mdsanima_cli.utils.print import print_cli_done
from mdsanima_cli.utils.print import print_cli_proc
from mdsanima_cli.utils.timer import timer


@timer
def convert_to_jpg(image_path: str, new_name: str) -> None:
    """Convert a image to JPG format, and then save the result with a new name and exif data."""

    # Open image file.
    image = Image.open(image_path)

    # Add exif data.
    exif_bytes = get_exif_bytes(JPG_HELP)

    # Save the result.
    image.save(new_name, "JPEG", exif=exif_bytes)


@timer
def compute_jpg() -> None:
    """Computing all images in the current directory to JPG format."""

    # Get directory stats info.
    directory = os.listdir()
    count = 1

    # New file name suffix for generated files.
    suffix = "_converted"
    png = ".png"
    jpg = ".jpg"
    webp = ".webp"

    # Checking extension and compute convert jpg from all images in directory.
    for file in directory:
        if file.endswith(png) and not file.endswith(suffix + jpg):
            new_name = file[:-4] + suffix + jpg
            time_taken = convert_to_jpg(file, new_name)
            print_cli_proc("converting", count, file, new_name, time_taken)
            count += 1
        if file.endswith(jpg) and not file.endswith(suffix + jpg):
            new_name = file[:-4] + suffix + jpg
            time_taken = convert_to_jpg(file, new_name)
            print_cli_proc("converting", count, file, new_name, time_taken)
            count += 1
        if file.endswith(webp) and not file.endswith(suffix + jpg):
            new_name = file[:-5] + suffix + jpg
            time_taken = convert_to_jpg(file, new_name)
            print_cli_proc("converting", count, file, new_name, time_taken)
            count += 1


def cli_jpg() -> None:
    """Main function for `jpg` command."""
    directory_statistic(JPG_COMD, JPG_HELP)
    ascii_title("processing")
    time_taken = compute_jpg()
    ascii_title("completed")
    print_cli_done(time_taken)
