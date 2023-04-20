# Copyright © 2023 Marcin Różewski MDSANIMA


"""This module is designed to renaming all images file in current directory to
UUID name.
"""


from __future__ import annotations

import os
import shutil
import uuid

from .ascii import ascii_title
from .mprints import print_cli_proc

from .cli_check import print_directory_check


def rename_uuid() -> None:
    """Renaming all images file to UUID in the current directory."""

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
            print_cli_proc("RENAME", str(count).zfill(4), file, new_name)
            count += 1
        if file.endswith(jpg):
            new_name = uuidv4 + jpg
            shutil.move(file, new_name)
            print_cli_proc("RENAME", str(count).zfill(4), file, new_name)
            count += 1
        if file.endswith(webp):
            new_name = uuidv4 + webp
            shutil.move(file, new_name)
            print_cli_proc("RENAME", str(count).zfill(4), file, new_name)
            count += 1


def cli_uuid() -> None:
    """Main function for `uuid` command."""
    print_directory_check("UUID", "RENAME IMAGE FILES TO UUID")
    ascii_title("processing")
    rename_uuid()
