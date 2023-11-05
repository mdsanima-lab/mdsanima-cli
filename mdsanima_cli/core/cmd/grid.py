# Copyright (c) 2023 MDSANIMA

"""Generate 2x2 grid from four images. It operates within a specified folder and can process all images at once."""


from __future__ import annotations

import os

from PIL import Image

from mdsanima_cli.core.cli import Command
from mdsanima_cli.core.cmd.check import directory_statistic
from mdsanima_cli.core.utils.ascii import ascii_title
from mdsanima_cli.core.utils.exif import get_exif_bytes
from mdsanima_cli.core.utils.print import print_cli_comp
from mdsanima_cli.core.utils.print import print_cli_done
from mdsanima_cli.core.utils.print import print_cli_proc
from mdsanima_cli.core.utils.timer import timer


@timer
def generate_grid(image_1_path: str, image_2_path: str, image_3_path: str, image_4_path: str, grid_name: str) -> None:
    """Generating a grid 2x2 from four images. Images must be the same size. Adding exif data."""

    # open four images file
    image_1 = Image.open(image_1_path)
    image_2 = Image.open(image_2_path)
    image_3 = Image.open(image_3_path)
    image_4 = Image.open(image_4_path)

    # helper for generate grid
    grid_size = (image_1.size[0] * 2, image_1.size[1] * 2)
    grid_image = Image.new("RGB", grid_size)

    # adding four images into 2x2 grid
    grid_image.paste(image_1, (0, 0))
    grid_image.paste(image_2, (image_1.size[0], 0))
    grid_image.paste(image_3, (0, image_1.size[1]))
    grid_image.paste(image_4, (image_1.size[0], image_1.size[1]))

    # add exif data and save
    exif_bytes = get_exif_bytes(f"{Command.GRID.help}")
    grid_image.save(grid_name, exif=exif_bytes)


@timer
def compute_grid() -> None:
    """Computing grid 2x2 from all images in the current directory and save them with a new name."""

    directory = os.listdir()
    images = []
    count = 1
    _grid = 1

    _prefix = "grid_"
    _png = ".png"
    _jpg = ".jpg"
    _webp = ".webp"

    for file in directory:
        if file.endswith(_png):
            grid_name = _prefix + str(_grid).zfill(5) + _png
            images.append(file)
            print_cli_proc("appending", count, file, grid_name, 0.000)
            if len(images) == 4:
                images_clean = "images x4"
                time_taken = generate_grid(images[0], images[1], images[2], images[3], grid_name)
                print_cli_comp("computing", _grid, images_clean, grid_name, time_taken)
                _grid += 1
                images = []
            count += 1
        if file.endswith(_jpg):
            grid_name = _prefix + str(_grid).zfill(5) + _jpg
            images.append(file)
            print_cli_proc("appending", count, file, grid_name, 0.000)
            if len(images) == 4:
                images_clean = "images x4"
                time_taken = generate_grid(images[0], images[1], images[2], images[3], grid_name)
                print_cli_comp("computing", _grid, images_clean, grid_name, time_taken)
                _grid += 1
                images = []
            count += 1
        if file.endswith(_webp):
            grid_name = _prefix + str(_grid).zfill(5) + _webp
            images.append(file)
            print_cli_proc("appending", count, file, grid_name, 0.000)
            if len(images) == 4:
                images_clean = "images x4"
                time_taken = generate_grid(images[0], images[1], images[2], images[3], grid_name)
                print_cli_comp("computing", _grid, images_clean, grid_name, time_taken)
                _grid += 1
                images = []
            count += 1


def grid() -> None:
    """The main functionality for the `grid` command."""

    directory_statistic(f"{Command.GRID.cmd}", f"{Command.GRID.help}")

    ascii_title("processing")
    time_taken = compute_grid()
    ascii_title("completed")
    print_cli_done(time_taken)
