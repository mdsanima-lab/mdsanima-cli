# Copyright (c) 2023 MDSANIMA

"""The default values for the arguments parser."""


from __future__ import annotations

from enum import Enum
from enum import unique

from mdsanima_cli._version import __version__
from mdsanima_cli.core.enums.target import Target


@unique
class Config(Enum):
    """The top-level parser that is displayed in command-line help."""

    CLI_NAME = str(Target.MDSANIMA).lower()
    """The program name."""

    CLI_USAGE = f"{CLI_NAME} <{str(Target.COMMAND).lower()}> [{str(Target.OPTIONS).lower()}]"
    """A usage message."""

    CLI_RUN = f"Run '{CLI_NAME} <{str(Target.COMMAND).lower()}> --help' for more information on a command."
    """The information how to use a help."""

    CLI_DESCRIPTION = "A command-line tool for image processing."
    """The description of what the program does."""

    CLI_EPILOG = f"Copyright (c) 2023 {Target.MDSANIMA}"
    """The text at the bottom of CLI program."""

    CLI_VERSION = f"{CLI_NAME}-cli v{__version__}"
    """The CLI name and the version of the program."""

    OPT_INFO_VERSION = "Show version"
    """The help information thats is show on version action."""

    OPT_INFO_HELP = "Show help"
    """The help information thats is show on help action."""

    TITLE_CMD = "Commands"
    """The title for command thats is show on positional arguments group."""

    TITLE_OPT = "Options"
    """The title for option thats is show on optional arguments group."""

    def __str__(self):
        return self.value
