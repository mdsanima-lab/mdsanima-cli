# Copyright (c) 2023 MDSANIMA

"""Convert image to PNG format. It operates within a specified folder and can process all images at once."""


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
def convert_to_png(image_path: str, new_name: str) -> None:
    """Convert a image to PNG format, and then save the result with a new name and exif data."""

    # Open image file.
    image = Image.open(image_path)

    # Add exif data.
    exif_bytes = get_exif_bytes(f"{Command.PNG.help}")

    # Save the result.
    image.save(new_name, "PNG", exif=exif_bytes)


@timer
def compute_png() -> None:
    """Computing all images in the current directory to PNG format."""

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
            time_taken = convert_to_png(file, new_name)
            print_cli_proc("converting", count, file, new_name, time_taken)
            count += 1
        if file.endswith(jpg) and not file.endswith(suffix + png):
            new_name = file[:-4] + suffix + png
            time_taken = convert_to_png(file, new_name)
            print_cli_proc("converting", count, file, new_name, time_taken)
            count += 1
        if file.endswith(webp) and not file.endswith(suffix + png):
            new_name = file[:-5] + suffix + png
            time_taken = convert_to_png(file, new_name)
            print_cli_proc("converting", count, file, new_name, time_taken)
            count += 1


def png() -> None:
    """The main functionality for the `png` command."""
    directory_statistic(f"{Command.PNG.cmd}", f"{Command.PNG.help}")
    ascii_title("processing")
    time_taken = compute_png()
    ascii_title("completed")
    print_cli_done(time_taken)
