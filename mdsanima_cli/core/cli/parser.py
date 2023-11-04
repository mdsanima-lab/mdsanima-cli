# Copyright (c) 2023 MDSANIMA

"""This module is used for parsing arguments in the command-line interface."""


from __future__ import annotations

import argparse

from mdsanima_cli.core.cli import Command
from mdsanima_cli.core.cli import Config
from mdsanima_cli.core.cli import PrettyHelpFormatter
from mdsanima_cli.core.enums import Target


def create_parser() -> argparse.ArgumentParser:
    """Create an argument parser for all available commands."""

    # The initial variables.
    _version = f"{Config.CLI_VERSION}"
    _info_version = f"{Config.OPT_INFO_VERSION}"
    _info_help = f"{Config.OPT_INFO_HELP}"
    _metavar = f"{Config.TITLE_CMD}"

    # Create the top-level parser.
    parser = argparse.ArgumentParser(formatter_class=PrettyHelpFormatter, add_help=False, allow_abbrev=False)
    subparsers = parser.add_subparsers(dest=f"{Target.COMMAND}", metavar=f"\r{_metavar}:")

    # The new titles for the parser.
    parser._subparsers.title = None
    parser._optionals.title = f"{Config.TITLE_OPT}"

    # The configuration for the parser.
    parser.prog = f"{Config.CLI_NAME}"
    parser.usage = f"{Config.CLI_USAGE}"
    parser.description = f"{Config.CLI_DESCRIPTION}"
    parser.epilog = f"{Config.CLI_RUN}"

    # Adding the optionals artument with the new config.
    parser.add_argument("-v", "--version", action="version", help=_info_version, version=_version)
    parser.add_argument("-h", "--help", action="help", help=_info_help)

    # Create the parsers for the commands.
    for cmd in list(Command):
        parser_cmd = cmd.add_parser(subparsers)
        parser_cmd.formatter_class = PrettyHelpFormatter
        parser_cmd.set_defaults(command=cmd.show_cli)
        parser_cmd.add_argument("--help", action="help", help=argparse.SUPPRESS)

    return parser
