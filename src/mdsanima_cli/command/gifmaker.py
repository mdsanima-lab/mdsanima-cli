# Copyright © 2023 Marcin Różewski MDSANIMA


"""Generating pixel art animation GIF. It operates within a specified folder and can process all
images at once.
"""


from __future__ import annotations

import glob
import os

from PIL import Image

from mdsanima_cli.command.check import directory_statistic
from mdsanima_cli.command.pixelart import generate_pixelart
from mdsanima_cli.command.resize import generate_resize
from mdsanima_cli.parser import GIFMAKER_COMMAND
from mdsanima_cli.parser import GIFMAKER_HELP
from mdsanima_cli.utils.ascii import ascii_title
from mdsanima_cli.utils.exif import get_exif_bytes
from mdsanima_cli.utils.print import print_cli_comp
from mdsanima_cli.utils.print import print_cli_done
from mdsanima_cli.utils.print import print_cli_proc
from mdsanima_cli.utils.timer import timer


TMP_PATH = os.path.expanduser("~/.mdsanima-cli/tmp/gifmaker")


@timer
def generate_tmp_images(image_path: str) -> None:
    """Generate temporary images in tmp cli path. Resizing image to 512px width and generate pixel
    art resolutions. This images is for generating GIF animation. Printing color info.
    """

    # Create tmp folder for images.
    if not os.path.exists(TMP_PATH):
        os.makedirs(TMP_PATH)

    # Resizing original image to 512px width.
    count = 1
    resized_name = f"{TMP_PATH}/{str(count).zfill(2)}_resized.jpg"
    time_taken = generate_resize(image_path, resized_name, 512)
    print_cli_proc("computing", count, image_path, "512px", time_taken)

    # List of pixel art resolutions to generate.
    resolutions = [256, 128, 64, 32, 16, 8, 4]

    # Generate pixel art resolutions.
    for resolution in resolutions:
        count += 1
        pixelart_name = f"{TMP_PATH}/{str(count).zfill(2)}_pixelart.jpg"
        time_taken = generate_pixelart(resized_name, pixelart_name, resolution)
        print_cli_proc("computing", count, image_path, f"{resolution}px".ljust(5), time_taken)


@timer
def generate_gifmaker(image_path: str, gif_name: str, gif_duration: int, count: int) -> None:
    """Generate one pixel art animation GIF from temporary images, then save the result with a new
    name and exif data. Original image is resized to 512px width. Printing color info.
    """

    # Generate temporary images.
    time_taken = generate_tmp_images(image_path)
    print_cli_comp("computing", count, image_path, str("tmp").ljust(5), time_taken)

    # List of tmp images file names.
    tmp_images = glob.glob(f"{TMP_PATH}/*.jpg")

    # Sorted and reversed list.
    tmp_images.sort()
    tmp_reversed = tmp_images[::-1]

    # Open first tmp image file.
    image = Image.open(tmp_images[0])

    # Create list of tmp images file.
    len_tmp = len(TMP_PATH) + 2
    count_img = 1
    images = []
    for tmp_img in tmp_images:
        images.append(Image.open(tmp_img))
        print_cli_proc("appending", count_img, str(tmp_img)[len_tmp:].ljust(14), gif_name, 0.001)
        count_img += 1
    for tmp_rev in tmp_reversed:
        images.append(Image.open(tmp_rev))
        print_cli_proc("appending", count_img, str(tmp_rev)[len_tmp:].ljust(14), gif_name, 0.001)
        count_img += 1

    # Set the duration for each image.
    durations = [gif_duration] * len(images)

    # Add exif data.
    exif_bytes = get_exif_bytes(GIFMAKER_HELP)

    # Save the result.
    image.save(
        gif_name,
        save_all=True,
        append_images=images[1:],
        duration=durations,
        loop=0,
        exif=exif_bytes,
    )


@timer
def compute_gifmaker() -> None:
    """Computing pixel art animation GIF for all images in the directory. GIF durations is 100ms."""

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
            gif_name = file[:-4] + suffix + gif
            time_taken = generate_gifmaker(file, gif_name, 100, count)
            print_cli_comp("computing", count, file, gif_name, time_taken)
            print_cli_done(time_taken)
            count += 1
        if file.endswith(jpg) and not file.endswith(suffix + jpg):
            gif_name = file[:-4] + suffix + gif
            time_taken = generate_gifmaker(file, gif_name, 100, count)
            print_cli_comp("computing", count, file, gif_name, time_taken)
            print_cli_done(time_taken)
            count += 1
        if file.endswith(webp) and not file.endswith(suffix + webp):
            gif_name = file[:-5] + suffix + gif
            time_taken = generate_gifmaker(file, gif_name, 100, count)
            print_cli_comp("computing", count, file, gif_name, time_taken)
            print_cli_done(time_taken)
            count += 1


def cli_gifmaker() -> None:
    """Main function for `gifmaker` command."""
    directory_statistic(GIFMAKER_COMMAND, GIFMAKER_HELP)
    ascii_title("processing")
    time_taken = compute_gifmaker()
    ascii_title("completed")
    print_cli_done(time_taken)
