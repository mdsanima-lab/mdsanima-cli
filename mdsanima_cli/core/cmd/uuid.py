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
    shutil.move(image_path, new_name)


@timer
def compute_uuid() -> None:
    """Rename all image files to UUID v4 name. Example `9c569045-a69f-4a26-b0b5-c3b06dd9052c.jpg` file name."""

    directory = os.listdir()
    count = 1

    _png = ".png"
    _jpg = ".jpg"
    _webp = ".webp"

    for file in directory:
        uuidv4 = str(unique.uuid4())
        if file.endswith(_png):
            new_name = uuidv4 + _png
            time_taken = rename_to_uuid(file, new_name)
            print_cli_proc("renaming", count, file, new_name, time_taken)
        if file.endswith(_jpg):
            new_name = uuidv4 + _jpg
            time_taken = rename_to_uuid(file, new_name)
            print_cli_proc("renaming", count, file, new_name, time_taken)
        if file.endswith(_webp):
            new_name = uuidv4 + _webp
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
