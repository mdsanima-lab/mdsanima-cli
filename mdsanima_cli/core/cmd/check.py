# Copyright (c) 2023 MDSANIMA

"""Checking and displaying statistic information about images."""


from __future__ import annotations

from mdsanima_cli.core.cli import Command
from mdsanima_cli.utils.print import print_cli_data
from mdsanima_cli.utils.print import print_cli_info
from mdsanima_cli.utils.stats import get_directory_statistic


def directory_statistic(cli_command: str, cli_help: str) -> str:
    """Printing info about all image files inside the current directory."""

    # Get directory stats info and color print.
    info = get_directory_statistic()

    # Printing color information statistics for image files.
    print_cli_info("mdsanima cli", cli_command, 40, 34, 12)
    print_cli_info("info cli", cli_help, 40, 34, 5)
    print_cli_data("path", info["path"], 34, 26, 38)
    print_cli_data("total", info["total"], 34, 24, 52)
    print_cli_data("folders", info["folders"], 34, 24, 52)
    print_cli_data("files", info["files"], 34, 24, 52)
    print_cli_data("images", info["images"], 34, 24, 52)
    print_cli_data("png", info["png"], 34, 24, 52)
    print_cli_data("jpg", info["jpg"], 34, 24, 52)
    print_cli_data("webp", info["webp"], 34, 24, 52)
    print_cli_data("gif", info["gif"], 34, 24, 52)
    print_cli_data("other", info["other"], 34, 24, 52)


def check() -> None:
    """The main functionality for the `check` command."""
    directory_statistic(f"{Command.CHECK.cmd}", f"{Command.CHECK.help}")
