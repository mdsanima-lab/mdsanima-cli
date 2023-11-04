# Copyright (c) 2023 MDSANIMA

"""Rename image files to universally unique identifiers UUID v4 name."""


from __future__ import annotations

import os
import shutil
import uuid as unique

from mdsanima_cli.core.cli import Command
from mdsanima_cli.core.cmd.check import directory_statistic
from mdsanima_cli.core.utils.ascii import ascii_title
from mdsanima_cli.core.utils.print import print_cli_done
from mdsanima_cli.core.utils.print import print_cli_proc
from mdsanima_cli.core.utils.timer import timer


@timer
def rename_to_uuid(image_path: str, new_name: str) -> None:
    """Rename image file to UUID."""

    # Renaming.
    shutil.move(image_path, new_name)


@timer
def compute_uuid() -> None:
    """Renaming all image files to UUID v4 name inside the current directory.

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
        uuidv4 = str(unique.uuid4())
        if file.endswith(png):
            new_name = uuidv4 + png
            time_taken = rename_to_uuid(file, new_name)
            print_cli_proc("renaming", count, file, new_name, time_taken)
        if file.endswith(jpg):
            new_name = uuidv4 + jpg
            time_taken = rename_to_uuid(file, new_name)
            print_cli_proc("renaming", count, file, new_name, time_taken)
        if file.endswith(webp):
            new_name = uuidv4 + webp
            time_taken = rename_to_uuid(file, new_name)
            print_cli_proc("renaming", count, file, new_name, time_taken)
        count += 1


def uuid() -> None:
    """The main functionality for the `uuid` command."""
    directory_statistic(f"{Command.UUID.cmd}", f"{Command.UUID.help}")
    ascii_title("processing")
    time_taken = compute_uuid()
    ascii_title("completed")
    print_cli_done(time_taken)
