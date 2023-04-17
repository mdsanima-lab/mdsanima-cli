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
    real_path = os.path.realpath(os.curdir)
    directory = os.listdir()

    # Directory stats count variables.
    all_files_count = len(directory)
    folders_count = 0
    files_count = 0
    images_count = 0
    png_count = 0
    jpg_count = 0
    webp_count = 0
    others_count = 0

    # Loop for checking stats.
    for filename in directory:
        if os.path.isdir(os.path.join(real_path, filename)):
            folders_count += 1
        elif filename.endswith(".png"):
            png_count += 1
            files_count += 1
            images_count += 1
        elif filename.endswith(".jpg"):
            jpg_count += 1
            files_count += 1
            images_count += 1
        elif filename.endswith(".webp"):
            webp_count += 1
            files_count += 1
            images_count += 1
        else:
            files_count += 1
            others_count += 1

    # Dictionary stats info.
    directory_info = {
        "real_path": real_path,
        "all_files_count": all_files_count,
        "folders_count": folders_count,
        "files_count": files_count,
        "images_count": images_count,
        "png_count": png_count,
        "jpg_count": jpg_count,
        "webp_count": webp_count,
        "others_count": others_count,
    }

    return directory_info


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
        mprint("MDSANIMA-CLI", 161, "")
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
