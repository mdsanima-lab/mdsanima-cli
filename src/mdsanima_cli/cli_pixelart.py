# Copyright © 2023 Marcin Różewski MDSANIMA


"""This module is designed to convert photos into pixel art. It operates within
a specified folder and can process all images at once. The first step is to
open the original photo, scale it to 32x32 pixels, scale it back to its
original size, and then save it. The pixel size is a parameter that can be
modified.
"""


from __future__ import annotations

import os
from PIL import Image

from .mprints import print_cli_proc
from .utils import asci_metal_border_text

from .cli_check import print_directory_check


def generate_pixelart(image_path: str, new_name: str, res: int) -> None:
    """Generate pixel art for one image, then save the result with a new
    filename.
    """

    # Generate one pixel art.
    image = Image.open(image_path)
    image_small = image.resize((res, res), resample=Image.Resampling.BILINEAR)
    result = image_small.resize(image.size, Image.Resampling.NEAREST)
    result.save(new_name)


def compute_pixelart() -> None:
    """Compute pixel art for all images in the directory and save them with
    a new appended filename.
    """

    # Get directory stats info.
    directory = os.listdir()
    count = 1

    # Checking extension and generate pixel art for all images in directory.
    for filename in directory:
        if filename.endswith(".png"):
            new_name = filename[:-4] + "_pixelart.png"
            generate_pixelart(filename, new_name, 32)
            print_cli_proc("COMPUTE", str(count).zfill(4), filename, new_name)
            count += 1
        if filename.endswith(".jpg"):
            new_name = filename[:-4] + "_pixelart.jpg"
            generate_pixelart(filename, new_name, 32)
            print_cli_proc("COMPUTE", str(count).zfill(4), filename, new_name)
            count += 1
        if filename.endswith(".webp"):
            new_name = filename[:-5] + "_pixelart.webp"
            generate_pixelart(filename, new_name, 32)
            print_cli_proc("COMPUTE", str(count).zfill(4), filename, new_name)
            count += 1


def cli_pixelart() -> None:
    """Main function for `pixelart` command."""
    print_directory_check("PIXELART", "COMPUTE PIXEL ART 32PX")
    asci_metal_border_text("processing")
    compute_pixelart()
