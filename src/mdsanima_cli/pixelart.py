# Copyritht © 2023 Marcin Różewski MDSANIMA


"""This module is for converting photos into pixelart. Works in the given
folder and compute all images as once. First step is open the original photo,
scales it to 64x64 pixels then scales back to original size and saves.
The pixels size is a parameter may be change.
"""


from __future__ import annotations

import os
from PIL import Image

from mdsanima_dev.colors import get_complex_color

from .utils import get_directory_info


mprint = get_complex_color


def generate_pixelart(image_path: str, new_name: str, res: int) -> None:
    """Generate pixelart for one image then save result with new name."""
    image = Image.open(image_path)
    image_small = image.resize((res, res), resample=Image.Resampling.BILINEAR)
    result = image_small.resize(image.size, Image.Resampling.NEAREST)
    result.save(new_name)


def compute_pixelart() -> None:
    """Compute all images in folder and save with new append name."""
    info = get_directory_info()
    directory = os.listdir()

    mprint(f"[MDSANIMA-CLI] -> compute pixelart 32px", 12)
    mprint(f"[DIRECTORY PATH] -> {info['real_path']}", 40)
    mprint(f"   [FILES COUNT] -> {info['files_count']}", 40)
    mprint(f"     [IMAGE PNG] -> {info['image_png_count']}", 40)
    mprint(f"     [IMAGE JPG] -> {info['image_jpg_count']}", 40)
    mprint(f"         [OTHER] -> {info['other_file_count']}", 40)

    for image_file in directory:
        extension = os.path.splitext(image_file)[-1].lower()
        if extension == ".png":
            image_new_name = image_file[:-4] + "_pixelart.png"
            generate_pixelart(image_file, image_new_name, 32)
            mprint(f"{image_file} -> {image_new_name}", 25)
        if extension == ".jpg":
            image_new_name = image_file[:-4] + "_pixelart.jpg"
            generate_pixelart(image_file, image_new_name, 32)
            mprint(f"{image_file} -> {image_new_name}", 25)
