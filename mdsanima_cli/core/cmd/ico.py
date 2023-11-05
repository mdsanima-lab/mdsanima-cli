# Copyright (c) 2023 MDSANIMA

"""Convert image to ICO format that is used to store icons on Windows."""


from __future__ import annotations

import os

from PIL import Image

from mdsanima_cli.core.cli import Command
from mdsanima_cli.core.cmd.check import directory_statistic
from mdsanima_cli.core.utils.ascii import ascii_title
from mdsanima_cli.core.utils.print import print_cli_done
from mdsanima_cli.core.utils.print import print_cli_proc
from mdsanima_cli.core.utils.timer import timer


@timer
def convert_to_ico(image_path: str, new_name: str) -> None:
    """Convert an image to ICO format, ensuring its square, and then save the result."""
    image = Image.open(image_path)

    if image.width != image.height:
        size = max(image.width, image.height)
        new_image = Image.new("RGBA", (size, size), (255, 255, 255, 0))
        x_offset = (size - image.width) // 2
        y_offset = (size - image.height) // 2
        new_image.paste(image, (x_offset, y_offset))
        image = new_image

    icon_sizes = [(16, 16), (24, 24), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)]
    icon_images = [image.resize(size) for size in icon_sizes]
    icon_images[6].save(new_name, "ICO", append_images=icon_images[0:], bitmap_format="bmp")


@timer
def compute_ico() -> None:
    """Computing all image files in the current directory to ICO format."""
    directory = os.listdir()
    count = 1

    _suffix = "_converted"
    _ico = ".ico"
    _png = ".png"
    _jpg = ".jpg"
    _webp = ".webp"

    for file in directory:
        if file.endswith(_png) and not file.endswith(_suffix + _ico):
            new_name = file[:-4] + _ico
            time_taken = convert_to_ico(file, new_name)
            print_cli_proc("converting", count, file, new_name, time_taken)
            count += 1
        if file.endswith(_jpg) and not file.endswith(_suffix + _ico):
            new_name = file[:-4] + _ico
            time_taken = convert_to_ico(file, new_name)
            print_cli_proc("converting", count, file, new_name, time_taken)
            count += 1
        if file.endswith(_webp) and not file.endswith(_suffix + _ico):
            new_name = file[:-5] + _ico
            time_taken = convert_to_ico(file, new_name)
            print_cli_proc("converting", count, file, new_name, time_taken)
            count += 1


def ico() -> None:
    """The main functionality for the `ico` command."""
    directory_statistic(f"{Command.ICO.cmd}", f"{Command.ICO.help}")
    ascii_title("processing")
    time_taken = compute_ico()
    ascii_title("completed")
    print_cli_done(time_taken)
