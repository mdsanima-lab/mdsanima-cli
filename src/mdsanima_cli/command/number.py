# Copyright © 2023 Marcin Różewski MDSANIMA


"""Renaming all images file in current directory to sequential number name."""


from __future__ import annotations

import os
import shutil

from mdsanima_cli.command.check import directory_statistic
from mdsanima_cli.parser import NUMBER_COMMAND
from mdsanima_cli.parser import NUMBER_HELP
from mdsanima_cli.utils.ascii import ascii_title
from mdsanima_cli.utils.print import print_cli_done
from mdsanima_cli.utils.print import print_cli_proc
from mdsanima_cli.utils.timer import timer


@timer
def rename_to_seq_number(image_path: str, new_name: str) -> None:
    """Rename image file to sequential number."""

    # Renaming.
    shutil.move(image_path, new_name)


@timer
def compute_seq_number() -> None:
    """Renaming all images file to sequential number in the current directory. Starting from 1.

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
            time_taken = rename_to_seq_number(file, new_name)
            print_cli_proc("renaming", count, file, new_name, time_taken)
        if file.endswith(jpg):
            new_name = str(count).zfill(5) + jpg
            time_taken = rename_to_seq_number(file, new_name)
            print_cli_proc("renaming", count, file, new_name, time_taken)
        if file.endswith(webp):
            new_name = str(count).zfill(5) + webp
            time_taken = rename_to_seq_number(file, new_name)
            print_cli_proc("renaming", count, file, new_name, time_taken)
        count += 1


def cli_number() -> None:
    """Main function for `number` command."""
    directory_statistic(NUMBER_COMMAND, NUMBER_HELP)
    ascii_title("processing")
    time_taken = compute_seq_number()
    ascii_title("completed")
    print_cli_done(time_taken)
