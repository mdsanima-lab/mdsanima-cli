# Copyright (c) 2023 MDSANIMA

"""Append a watermark to image. It operates within a specified folder and can process all images at once."""


from __future__ import annotations

import os

from PIL import Image

from mdsanima_cli.core.cli import Command
from mdsanima_cli.core.cmd.check import directory_statistic
from mdsanima_cli.core.utils.ascii import ascii_title
from mdsanima_cli.core.utils.exif import get_exif_bytes
from mdsanima_cli.core.utils.print import print_cli_data
from mdsanima_cli.core.utils.print import print_cli_done
from mdsanima_cli.core.utils.print import print_cli_proc
from mdsanima_cli.core.utils.timer import timer


WATERMARK_PATH = os.path.expanduser("~/.mdsanima-cli/config/img/watermark.png")


@timer
def append_watermark(image_path: str, waterm_path: str, new_name: str) -> None:
    """Append a watermark to one image. The watermark is a rotated on 45 degrees and shifted."""

    # open image and watermark file
    image = Image.open(image_path)
    _watermark = Image.open(waterm_path)

    # image and watermark size
    image_width, _image_height = image.size
    watermark_width, watermark_height = _watermark.size

    # calculating size for watermark
    resize_ratio = 0.25
    new_watermark_width = int(image_width * resize_ratio)
    new_watermark_height = int(watermark_height * new_watermark_width / watermark_width)

    # resizing and rotating watermark
    _watermark = _watermark.resize((new_watermark_width, new_watermark_height)).rotate(45, expand=1)

    # rotate watermark size
    rotate_watermark_width, rotate_watermark_height = _watermark.size

    # background helper size
    bg_size = int(image_width * resize_ratio)
    bg_half = int(bg_size / 2)

    # calculating position for background helper
    position_x = int(bg_half - rotate_watermark_width / 2)
    position_y = int(bg_half - rotate_watermark_height / 2)

    # new background helper for watermark position
    watermark_bg = Image.new("RGBA", (bg_size, bg_size), (0, 0, 0, 0))
    watermark_bg.paste(_watermark, (position_x, position_y), _watermark)

    # append and shift rotated watermakr to image
    for row in range(10):
        for col in range(10):
            width = int(-bg_half + bg_size * row)
            height = int(-bg_half + bg_size * col)
            image.paste(watermark_bg, (width, height), watermark_bg)

    # add exif data and save
    exif_bytes = get_exif_bytes(f"{Command.WATERMARK.help}")
    image.save(new_name, exif=exif_bytes)


@timer
def compute_watermark() -> None:
    """Add a watermark to all images in the current directory that includes the watermark."""

    directory = os.listdir()
    count = 1

    _suffix = "_watermark"
    _png = ".png"
    _jpg = ".jpg"
    _webp = ".webp"

    for file in directory:
        if file.endswith(_png) and not file.endswith(_suffix + _png):
            new_name = file[:-4] + _suffix + _png
            time_taken = append_watermark(file, WATERMARK_PATH, new_name)
            print_cli_proc("computing", count, file, new_name, time_taken)
            count += 1
        if file.endswith(_jpg) and not file.endswith(_suffix + _jpg):
            new_name = file[:-4] + _suffix + _jpg
            time_taken = append_watermark(file, WATERMARK_PATH, new_name)
            print_cli_proc("computing", count, file, new_name, time_taken)
            count += 1
        if file.endswith(_webp) and not file.endswith(_suffix + _webp):
            new_name = file[:-5] + _suffix + _webp
            time_taken = append_watermark(file, WATERMARK_PATH, new_name)
            print_cli_proc("computing", count, file, new_name, time_taken)
            count += 1


def watermark() -> None:
    """The main functionality for the `watermark` command."""

    directory_statistic(f"{Command.WATERMARK.cmd}", f"{Command.WATERMARK.help}")

    try:
        ascii_title("processing")
        time_taken = compute_watermark()
        ascii_title("completed")
        print_cli_done(time_taken)
    except FileNotFoundError:
        ascii_title("config error")
        warning = "Put your watermark here '" + WATERMARK_PATH + "' to continue!"
        print_cli_data("warning watermark", warning, 197, 209, 38)
