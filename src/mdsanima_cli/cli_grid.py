# Copyright © 2023 Marcin Różewski MDSANIMA


"""This module is designed to generating a grid from all images in the current
directory. It operates within a specified folder and can process all images at
once.
"""


from __future__ import annotations

import os

from PIL import Image

from .ascii import ascii_title
from .exif import get_exif_bytes
from .mprints import print_cli_comp
from .mprints import print_cli_proc

from .cli_check import print_directory_check


def generate_grid(
    image1_path: str,
    image2_path: str,
    image3_path: str,
    image4_path: str,
    grid_name: str,
) -> None:
    """Generating a grid 2x2 from four images, and then save the result with a
    new file name. Images must be the same size. Adding exif data.
    """

    # Open four images file.
    image1 = Image.open(image1_path)
    image2 = Image.open(image2_path)
    image3 = Image.open(image3_path)
    image4 = Image.open(image4_path)

    # New image helper for generate grid.
    grid_size = (image1.size[0] * 2, image1.size[1] * 2)
    grid_image = Image.new("RGB", grid_size)

    # Adding four images into grid 2x2.
    grid_image.paste(image1, (0, 0))
    grid_image.paste(image2, (image1.size[0], 0))
    grid_image.paste(image3, (0, image1.size[1]))
    grid_image.paste(image4, (image1.size[0], image1.size[1]))

    # Add exif data.
    exif_bytes = get_exif_bytes("with grid 2x2")

    # Save the result.
    grid_image.save(grid_name, exif=exif_bytes)


def compute_grid() -> None:
    """Computing grid 2x2 from all images in the current directory and save
    them with a new file name.
    """

    # Get directory stats info.
    directory = os.listdir()
    count = 1
    grid = 1
    img = []

    # New file name prefix for generated files.
    prefix = "grid_"
    png = ".png"
    jpg = ".jpg"
    webp = ".webp"

    # Checking extension and compute grid from all images in directory.
    for file in directory:
        if file.endswith(png):
            grid_name = prefix + str(grid).zfill(5) + png
            img.append(file)
            print_cli_proc("APPENDING", count, file, grid_name)
            if len(img) == 4:
                images_clean = str(img).replace(",", "").replace("'", "")[1:-1]
                print_cli_comp("COMPUTING", grid, images_clean, grid_name)
                generate_grid(img[0], img[1], img[2], img[3], grid_name)
                grid += 1
                img = []
            count += 1
        if file.endswith(jpg):
            grid_name = prefix + str(grid).zfill(5) + jpg
            img.append(file)
            print_cli_proc("APPENDING", count, file, grid_name)
            if len(img) == 4:
                images_clean = str(img).replace(",", "").replace("'", "")[1:-1]
                print_cli_comp("COMPUTING", grid, images_clean, grid_name)
                generate_grid(img[0], img[1], img[2], img[3], grid_name)
                grid += 1
                img = []
            count += 1
        if file.endswith(webp):
            grid_name = prefix + str(grid).zfill(5) + webp
            img.append(file)
            print_cli_proc("APPENDING", count, file, grid_name)
            if len(img) == 4:
                images_clean = str(img).replace(",", "").replace("'", "")[1:-1]
                print_cli_comp("COMPUTING", grid, images_clean, grid_name)
                generate_grid(img[0], img[1], img[2], img[3], grid_name)
                grid += 1
                img = []
            count += 1


def cli_grid() -> None:
    """Main function for `grid` command."""
    print_directory_check("GRID", "COMPUTE GRID 2x2")
    ascii_title("processing")
    compute_grid()
