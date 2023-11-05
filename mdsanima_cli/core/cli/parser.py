# Copyright (c) 2023 MDSANIMA

"""This module is used for parsing arguments in the command-line interface."""


from __future__ import annotations

import argparse

from mdsanima_cli.core.cli import Command
from mdsanima_cli.core.cli import Config
from mdsanima_cli.core.cli import PrettyHelp
from mdsanima_cli.core.enums import Target


def create_parser() -> argparse.ArgumentParser:
    """Create an argument parser for all available commands."""

    parser = argparse.ArgumentParser(formatter_class=PrettyHelp, add_help=False, allow_abbrev=False)
    subparsers = parser.add_subparsers(dest=f"{Target.COMMAND}", metavar=f"\r{Config.TITLE_CMD}:")

    parser._subparsers.title = None  # pylint: disable=W0212
    parser._optionals.title = f"{Config.TITLE_OPT}"  # pylint: disable=W0212

    parser.prog = f"{Config.CLI_NAME}"
    parser.usage = f"{Config.CLI_USAGE}"
    parser.description = f"{Config.CLI_DESCRIPTION}"
    parser.epilog = f"{Config.CLI_RUN}"

    for cmd in list(Command):
        parser_cmd = cmd.add_parser(subparsers)
        parser_cmd.formatter_class = PrettyHelp
        parser_cmd.set_defaults(command=cmd.show)
        parser_cmd.add_argument("--help", action="help", help=argparse.SUPPRESS)

    parser.add_argument("-v", "--version", action="version", help=f"{Config.OPT_INFO}", version=f"{Config.CLI_VERSION}")
    parser.add_argument("-h", "--help", action="help", help=f"{Config.OPT_HELP}")

    return parser
