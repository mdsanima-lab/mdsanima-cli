# Copyright © 2023 Marcin Różewski MDSANIMA


"""This module is designed for checking and displaying info about all images in
the current directory.
"""


from __future__ import annotations

from mdsanima_dev.colors import get_complex_color

from .utils import get_directory_info


def print_directory_check(cli_cmd_info: str) -> None:
    """Printing info about all images inside the current directory."""

    # Get directory stats info and color print.
    info = get_directory_info()
    mprint = get_complex_color

    # Print color info stats.
    mprint(f"[MDSANIMA-CLI] -> {cli_cmd_info}", 12)
    mprint(f"[DIRECTORY PATH] -> {info['real_path']}", 40)
    mprint(f"     [ALL FILES] -> {info['all_files_count']}", 40)
    mprint(f"       [FOLDERS] -> {info['folders_count']}", 40)
    mprint(f"         [FILES] -> {info['files_count']}", 40)
    mprint(f"        [IMAGES] -> {info['images_count']}", 40)
    mprint(f"           [PNG] -> {info['png_count']}", 40)
    mprint(f"           [JPG] -> {info['jpg_count']}", 40)
    mprint(f"          [WEBP] -> {info['webp_count']}", 40)
    mprint(f"        [OTHERS] -> {info['others_count']}", 40)
