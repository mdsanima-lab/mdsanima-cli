# Copyright (c) 2023 MDSANIMA

"""Generate GIF pixel art animation. It operates within a specified folder and can process all images at once."""


from __future__ import annotations

import glob
import os

from PIL import Image

from mdsanima_cli.core.cli import Command
from mdsanima_cli.core.cmd.check import directory_statistic
from mdsanima_cli.core.cmd.pixelart import generate_pixelart
from mdsanima_cli.core.cmd.resize import generate_resize
from mdsanima_cli.core.utils.ascii import ascii_title
from mdsanima_cli.core.utils.exif import get_exif_bytes
from mdsanima_cli.core.utils.print import print_cli_comp
from mdsanima_cli.core.utils.print import print_cli_done
from mdsanima_cli.core.utils.print import print_cli_proc
from mdsanima_cli.core.utils.timer import timer


TMP_PATH = os.path.expanduser("~/.mdsanima-cli/tmp/gifmaker")


@timer
def generate_tmp_images(image_path: str) -> None:
    """Generate temporary images in tmp cli path. Resizing image to 512px width and generate pixel art resolutions.
    This images is for generating GIF animation. Printing color info.
    """

    # create tmp folder for images
    if not os.path.exists(TMP_PATH):
        os.makedirs(TMP_PATH)

    # resizing original image to 512px width
    count = 1
    resized_name = f"{TMP_PATH}/{str(count).zfill(2)}_resized.jpg"
    time_taken = generate_resize(image_path, resized_name, 512)
    print_cli_proc("computing", count, image_path, "512px", time_taken)

    # list of pixel art resolutions to generate
    resolutions = [256, 128, 64, 32, 16, 8, 4]

    # generate pixel art resolutions
    for resolution in resolutions:
        count += 1
        pixelart_name = f"{TMP_PATH}/{str(count).zfill(2)}_pixelart.jpg"
        time_taken = generate_pixelart(resized_name, pixelart_name, resolution)
        print_cli_proc("computing", count, image_path, f"{resolution}px".ljust(5), time_taken)


@timer
def generate_gifmaker(image_path: str, gif_name: str, gif_duration: int, count: int) -> None:
    """Generate one GIF pixel art animation from temporary images, then save the result with a new name and exif data.
    Original image is resized to 512px width. Printing color info.
    """

    # generate temporary images
    time_taken = generate_tmp_images(image_path)
    print_cli_comp("computing", count, image_path, str("tmp").ljust(5), time_taken)

    # list of tmp images file names
    tmp_images = glob.glob(f"{TMP_PATH}/*.jpg")

    # sorted and reversed list
    tmp_images.sort()
    tmp_reversed = tmp_images[::-1]

    # open first tmp image file
    image = Image.open(tmp_images[0])

    # create list of tmp images file
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

    # set the duration for each image
    durations = [gif_duration] * len(images)
    exif_bytes = get_exif_bytes(f"{Command.GIFMAKER.help}")
    image.save(gif_name, save_all=True, append_images=images[1:], duration=durations, loop=0, exif=exif_bytes)


@timer
def compute_gifmaker() -> None:
    """Computing pixel art animation GIF for all images in the directory. GIF durations is 100 ms."""

    directory = os.listdir()
    count = 1

    _suffix = "_gifmaker"
    _png = ".png"
    _jpg = ".jpg"
    _webp = ".webp"
    _gif = ".gif"

    for file in directory:
        if file.endswith(_png) and not file.endswith(_suffix + _png):
            gif_name = file[:-4] + _suffix + _gif
            time_taken = generate_gifmaker(file, gif_name, 100, count)
            print_cli_comp("computing", count, file, gif_name, time_taken)
            print_cli_done(time_taken)
            count += 1
        if file.endswith(_jpg) and not file.endswith(_suffix + _jpg):
            gif_name = file[:-4] + _suffix + _gif
            time_taken = generate_gifmaker(file, gif_name, 100, count)
            print_cli_comp("computing", count, file, gif_name, time_taken)
            print_cli_done(time_taken)
            count += 1
        if file.endswith(_webp) and not file.endswith(_suffix + _webp):
            gif_name = file[:-5] + _suffix + _gif
            time_taken = generate_gifmaker(file, gif_name, 100, count)
            print_cli_comp("computing", count, file, gif_name, time_taken)
            print_cli_done(time_taken)
            count += 1


def gifmaker() -> None:
    """The main functionality for the `gifmaker` command."""

    directory_statistic(f"{Command.GIFMAKER.cmd}", f"{Command.GIFMAKER.help}")

    ascii_title("processing")
    time_taken = compute_gifmaker()
    ascii_title("completed")
    print_cli_done(time_taken)
