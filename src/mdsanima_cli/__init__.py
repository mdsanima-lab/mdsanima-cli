# Copyritht © 2023 Marcin Różewski MDSANIMA


"""Initial main functionality for command line tools."""


from __future__ import annotations

import argparse
from mdsanima_dev.colors import get_complex_color


def create_parser():
    parser = argparse.ArgumentParser(prog="mdsanima")
    subparsers = parser.add_subparsers()

    pixelart_parser = subparsers.add_parser("pixelart")
    pixelart_parser.set_defaults(command="pixelart")

    gifmaker_parser = subparsers.add_parser("gifmaker")
    gifmaker_parser.set_defaults(command="gifmaker")

    return parser


def main_cli():
    parser = create_parser()
    args = parser.parse_args()
    mprint = get_complex_color

    if args.command == "pixelart":
        mprint("Hello from pixelart", 46)
    elif args.command == "gifmaker":
        mprint("Hello from gifmaker", 46)
