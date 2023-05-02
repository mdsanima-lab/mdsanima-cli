# Copyright © 2023 Marcin Różewski MDSANIMA


"""This module provides various utilities that can be used for command-line tools.
The module is intended for use in development.
"""


from __future__ import annotations

import os


def get_directory_statistic() -> dict:
    """Checking the current directory and returning statistic details about it."""

    # Real path of directory.
    path = os.path.realpath(os.curdir)
    directory = os.listdir()

    # Directory stats count variables.
    total = len(directory)
    folders = 0
    files = 0
    images = 0
    png = 0
    jpg = 0
    webp = 0
    gif = 0
    other = 0

    # Loop for checking each files in direcotry.
    for filename in directory:
        if os.path.isdir(os.path.join(path, filename)):
            folders += 1
        elif filename.endswith(".png"):
            png += 1
            files += 1
            images += 1
        elif filename.endswith(".jpg"):
            jpg += 1
            files += 1
            images += 1
        elif filename.endswith(".webp"):
            webp += 1
            files += 1
            images += 1
        elif filename.endswith(".gif"):
            gif += 1
            files += 1
        else:
            files += 1
            other += 1

    # Dictionary for directory stats.
    directory_statistic = {
        "path": path,
        "total": total,
        "folders": folders,
        "files": files,
        "images": images,
        "png": png,
        "jpg": jpg,
        "webp": webp,
        "gif": gif,
        "other": other,
    }

    return directory_statistic


def get_images_count() -> dict:
    """This function is intended for counting only the images in the current directory. Instead of
    using a loop, we will use a Linux command for this and pipe it to another command.
    """

    # Linux terminal commands variable for counting.
    cmd_png = "ls -i *.png | wc -l"
    cmd_jpg = "ls -i *.jpg | wc -l"
    cmd_webp = "ls -i *.webp | wc -l"

    # Run the command and read the value.
    png = int(os.popen(cmd_png).read())
    jpg = int(os.popen(cmd_jpg).read())
    webp = int(os.popen(cmd_webp).read())

    # Calculating total images in directory.
    total = png + jpg + webp

    # Dictionary images count.
    images_count = {
        "total": total,
        "png": png,
        "jpg": jpg,
        "webp": webp,
    }

    return images_count
