# Copyright © 2023 Marcin Różewski MDSANIMA


"""Generating a grid from all images in the current directory. It operates within a specified folder
and can process all images at once.
"""


from __future__ import annotations

import os

from PIL import Image

from .ascii import ascii_title
from .cli_check import print_directory_check
from .exif import get_exif_bytes
from .mprints import print_cli_comp
from .mprints import print_cli_proc


COMMAND = "grid"
INFO = "generating grid 2x2"


def generate_grid(
    image_1_path: str, image_2_path: str, image_3_path: str, image_4_path: str, grid_name: str
) -> None:
    """Generating a grid 2x2 from four images, and then save the result with a new file name.
    Images must be the same size. Adding exif data.
    """

    # Open four images file.
    image_1 = Image.open(image_1_path)
    image_2 = Image.open(image_2_path)
    image_3 = Image.open(image_3_path)
    image_4 = Image.open(image_4_path)

    # New image helper for generate grid.
    grid_size = (image_1.size[0] * 2, image_1.size[1] * 2)
    grid_image = Image.new("RGB", grid_size)

    # Adding four images into grid 2x2.
    grid_image.paste(image_1, (0, 0))
    grid_image.paste(image_2, (image_1.size[0], 0))
    grid_image.paste(image_3, (0, image_1.size[1]))
    grid_image.paste(image_4, (image_1.size[0], image_1.size[1]))

    # Add exif data.
    exif_bytes = get_exif_bytes(INFO)

    # Save the result.
    grid_image.save(grid_name, exif=exif_bytes)


def compute_grid() -> None:
    """Computing grid 2x2 from all images in the current directory and save them with a new name."""

    # Get directory stats info.
    directory = os.listdir()
    images = []
    count = 1
    grid = 1

    # New file name prefix for generated files.
    prefix = "grid_"
    png = ".png"
    jpg = ".jpg"
    webp = ".webp"

    # Checking extension and compute grid from all images in directory.
    for file in directory:
        if file.endswith(png):
            grid_name = prefix + str(grid).zfill(5) + png
            images.append(file)
            print_cli_proc("appending", count, file, grid_name)
            if len(images) == 4:
                images_clean = str(images).replace(",", "").replace("'", "")[1:-1]
                print_cli_comp("computing", grid, images_clean, grid_name)
                generate_grid(images[0], images[1], images[2], images[3], grid_name)
                grid += 1
                images = []
            count += 1
        if file.endswith(jpg):
            grid_name = prefix + str(grid).zfill(5) + jpg
            images.append(file)
            print_cli_proc("appending", count, file, grid_name)
            if len(images) == 4:
                images_clean = str(images).replace(",", "").replace("'", "")[1:-1]
                print_cli_comp("computing", grid, images_clean, grid_name)
                generate_grid(images[0], images[1], images[2], images[3], grid_name)
                grid += 1
                images = []
            count += 1
        if file.endswith(webp):
            grid_name = prefix + str(grid).zfill(5) + webp
            images.append(file)
            print_cli_proc("appending", count, file, grid_name)
            if len(images) == 4:
                images_clean = str(images).replace(",", "").replace("'", "")[1:-1]
                print_cli_comp("computing", grid, images_clean, grid_name)
                generate_grid(images[0], images[1], images[2], images[3], grid_name)
                grid += 1
                images = []
            count += 1


def cli_grid() -> None:
    """Main function for `grid` command."""
    print_directory_check(COMMAND, INFO)
    ascii_title("processing")
    compute_grid()
