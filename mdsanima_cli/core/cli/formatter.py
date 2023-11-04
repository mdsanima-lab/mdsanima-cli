# Copyright (c) 2023 MDSANIMA

"""This module is for custom argparse help formatter."""


from __future__ import annotations

import argparse


class PrettyHelpFormatter(argparse.HelpFormatter):
    """Custom help formatter for adjusting help strings that are generated on argparse."""

    def _format_usage(self, usage, actions, groups, prefix):
        if prefix is None:
            prefix = "Usage: "
        return super()._format_usage(usage, actions, groups, prefix)

    def _format_action_invocation(self, action):
        self._indent_increment = 2
        if not action.option_strings:
            if not self._current_section.heading:
                self._indent_increment = 0
        return super()._format_action_invocation(action)

    def _split_lines(self, text, width):
        return text.splitlines()

    def _fill_text(self, text, width, indent):
        return "".join(indent + line for line in text.splitlines(keepends=True))
