# Copyright © 2023 Marcin Różewski MDSANIMA


"""Renaming all images file in current directory to UUID v4 name."""


from __future__ import annotations

import os
import shutil
import uuid

from .ascii import ascii_title
from .cli_check import print_directory_check
from .mprints import print_cli_proc


COMMAND = "uuid"
INFO = "renaming image files to uuid"


def rename_to_uuid() -> None:
    """Renaming all images file to UUID in the current directory.

    Example file name: `9c569045-a69f-4a26-b0b5-c3b06dd9052c.jpg`
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
        uuidv4 = str(uuid.uuid4())
        if file.endswith(png):
            new_name = uuidv4 + png
            shutil.move(file, new_name)
            print_cli_proc("renaming", count, file, new_name)
        if file.endswith(jpg):
            new_name = uuidv4 + jpg
            shutil.move(file, new_name)
            print_cli_proc("renaming", count, file, new_name)
        if file.endswith(webp):
            new_name = uuidv4 + webp
            shutil.move(file, new_name)
            print_cli_proc("renaming", count, file, new_name)
        count += 1


def cli_uuid() -> None:
    """Main function for `uuid` command."""
    print_directory_check(COMMAND, INFO)
    ascii_title("processing")
    rename_to_uuid()
