# Copyright © 2023 Marcin Różewski MDSANIMA


"""Generating pixel art animation GIF. It operates within a specified folder and can process all
images at once.
"""


from __future__ import annotations

import os

from PIL import Image

from mdsanima_cli.command.check import directory_statistic
from mdsanima_cli.parser import GIFMAKER_COMMAND
from mdsanima_cli.parser import GIFMAKER_HELP
from mdsanima_cli.utils.ascii import ascii_title
from mdsanima_cli.utils.exif import get_exif_bytes
from mdsanima_cli.utils.print import print_cli_done
from mdsanima_cli.utils.print import print_cli_proc
from mdsanima_cli.utils.timer import timer


@timer
def generate_gifmaker(image_path: str, gif_name: str) -> None:
    """Generate pixel art animation GIF for one image, then save the result with a new name and
    exif data. Image is resize to 1024px.
    """

    # Open image file.
    image = Image.open(image_path)

    # Image size.
    image_width, image_height = image.size

    # List of pixelart resolutions.
    resolutions = [1024, 512, 256, 128, 64, 32, 16, 8, 8, 16, 32, 64, 128, 256, 512, 1024]

    # Calculating resolution for gif.
    gif_ratio = int(image_width / resolutions[0])
    gif_width = int(image_width / gif_ratio)
    gif_height = int(image_height / gif_ratio)
    gif_size = (gif_width, gif_height)

    # New size for animation.
    animation = image.resize(gif_size)

    # Generate pixel arts resolution.
    images = []
    for resolution in resolutions:
        # Calculation resolution for pixelart.
        pixelart_ratio = int(image_width / resolution)
        pixelart_width = int(image_width / pixelart_ratio)
        pixelart_height = int(image_height / pixelart_ratio)
        pixealrt_size = (pixelart_width, pixelart_height)

        # Generate pixel art resolution.
        small_image = image.resize(pixealrt_size, resample=Image.Resampling.BILINEAR)
        result = small_image.resize(gif_size, Image.Resampling.NEAREST)
        images.append(result)

    # Set the duration for each image.
    durations = [100] * len(images)

    # Add exif data.
    exif_bytes = get_exif_bytes(GIFMAKER_HELP)

    # Save the result.
    animation.save(
        gif_name,
        save_all=True,
        append_images=images[1:],
        duration=durations,
        loop=0,
        exif=exif_bytes,
    )


@timer
def compute_gifmaker() -> None:
    """Computing pixel art animation GIF for all images in the directory."""

    # Get directory stats info.
    directory = os.listdir()
    count = 1

    # New file name end for generated files.
    suffix = "_gifmaker"
    png = ".png"
    jpg = ".jpg"
    webp = ".webp"
    gif = ".gif"

    # Checking extension and generate pixel art for all images in directory.
    for file in directory:
        if file.endswith(png) and not file.endswith(suffix + png):
            new_name = file[:-4] + suffix + gif
            time_taken = generate_gifmaker(file, new_name)
            print_cli_proc("computing", count, file, new_name, time_taken)
            count += 1
        if file.endswith(jpg) and not file.endswith(suffix + jpg):
            new_name = file[:-4] + suffix + gif
            time_taken = generate_gifmaker(file, new_name)
            print_cli_proc("computing", count, file, new_name, time_taken)
            count += 1
        if file.endswith(webp) and not file.endswith(suffix + webp):
            new_name = file[:-5] + suffix + gif
            time_taken = generate_gifmaker(file, new_name)
            print_cli_proc("computing", count, file, new_name, time_taken)
            count += 1


def cli_gifmaker() -> None:
    """Main function for `gifmaker` command."""
    directory_statistic(GIFMAKER_COMMAND, GIFMAKER_HELP)
    ascii_title("processing")
    time_taken = compute_gifmaker()
    ascii_title("completed")
    print_cli_done(time_taken)
