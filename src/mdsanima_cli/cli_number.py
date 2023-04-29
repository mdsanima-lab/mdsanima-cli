# Copyright © 2023 Marcin Różewski MDSANIMA


"""This module is designed to renaming all images file in current directory to
sequential number name.
"""


from __future__ import annotations

import os
import shutil

from .ascii import ascii_title
from .mprints import print_cli_proc

from .cli_check import print_directory_check


COMMAND = "number"
INFO = "renaming image files to sequential number"


def rename_number() -> None:
    """Renaming all images file to sequential number in the current directory.
    Starting from 1.

    Example file name: `00001.jpg`
    """

    # Get directory stats info.
    directory = os.listdir()
    count = 1

    # Files to rename.
    png = ".png"
    jpg = ".jpg"
    webp = ".webp"

    # Checking extension and rename images in directory.
    for file in directory:
        if file.endswith(png):
            new_name = str(count).zfill(5) + png
            shutil.move(file, new_name)
            print_cli_proc("renaming", count, file, new_name)
        if file.endswith(jpg):
            new_name = str(count).zfill(5) + jpg
            shutil.move(file, new_name)
            print_cli_proc("renaming", count, file, new_name)
        if file.endswith(webp):
            new_name = str(count).zfill(5) + webp
            shutil.move(file, new_name)
            print_cli_proc("renaming", count, file, new_name)
        count += 1


def cli_number() -> None:
    """Main function for `number` command."""
    print_directory_check(COMMAND, INFO)
    ascii_title("processing")
    rename_number()
