# Copyright © 2023 Marcin Różewski MDSANIMA


"""This module is designed for checking and displaying info about all images in
the current directory.
"""


from __future__ import annotations

from .mprints import print_cli_info
from .mprints import print_cli_data
from .utils import get_directory_info


def print_directory_check(cli_command: str, cli_info: str) -> None:
    """Printing info about all images inside the current directory."""

    # Get directory stats info and color print.
    info = get_directory_info()

    # Print color info stats.
    print_cli_info("MDSANIMA CLI", cli_command, 40, 34, 12)
    print_cli_info("INFO CLI", cli_info, 40, 34, 5)
    print_cli_data("PATH", info["path"], 34, 26, 38)
    print_cli_data("TOTAL", info["total"], 34, 24, 52)
    print_cli_data("FOLDERS", info["folders"], 34, 24, 52)
    print_cli_data("FILES", info["files"], 34, 24, 52)
    print_cli_data("IMAGES", info["images"], 34, 24, 52)
    print_cli_data("PNG", info["png"], 34, 24, 52)
    print_cli_data("JPG", info["jpg"], 34, 24, 52)
    print_cli_data("WEBP", info["webp"], 34, 24, 52)
    print_cli_data("GIF", info["gif"], 34, 24, 52)
    print_cli_data("OTHER", info["other"], 34, 24, 52)


def cli_check() -> None:
    """Main function for `check` command."""
    print_directory_check("CHECK", "DIRECTORY STATISTIC")
