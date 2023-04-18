# Copyright © 2023 Marcin Różewski MDSANIMA


"""This module provides various utilities that can be used for command-line
tools. The module is intended for use in development.
"""


from __future__ import annotations

import os
import subprocess
import sys

from mdsanima_dev.colors import get_complex_color


def get_directory_info() -> dict:
    """Checking the current directory and returning details info about it."""

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

    # Loop for checking each files in direcotry..
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

    # Dictionary for directory info.
    directory_info = {
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

    return directory_info


def get_images_count() -> dict:
    """This function is intended for counting only the images in the current
    directory. Instead of using a loop, we will use a Linux command for this
    and pipe it to another command.
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


def check_system_dependencies(dpkg_package: str) -> None:
    """Checking system dependencies packages is already installed, if not print
    the warning info and exit the program.
    """

    # Color print variable.
    mprint = get_complex_color

    try:
        # Check if package is already installed.
        subprocess.check_output([dpkg_package, "-v"])
    except FileNotFoundError:
        # If not print color info and exit program.
        mprint("[", 197, "")
        mprint("MDSANIMA CLI", 161, "")
        mprint("]", 197, " -> ")
        mprint("SYSTEM DEPENDENCIES WARNING", 209)
        mprint("[", 197, "")
        mprint("WARNING", 161, "")
        mprint("]", 197, " ")
        mprint("To use", 255, " ")
        mprint("mdsanima-cli", 46, " ")
        mprint("properly, you need to install the", 255, " ")
        mprint(dpkg_package, 12, " ")
        mprint("package on your system.", 255)
        mprint("[", 197, "")
        mprint("WARNING", 161, "")
        mprint("]", 197, " ")
        mprint("Run", 255, " ")
        mprint(f"sudo apt install {dpkg_package}", 42, " ")
        mprint("to install the package!", 255)
        sys.exit()


def asci_metal_border_text(text: str) -> None:
    """Print ASCII text in color and with a border from the toilet package."""
    os.system("toilet -f future -F metal -F border '   '" + text + "'   '")
