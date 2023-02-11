# Copyritht © 2023 Marcin Różewski MDSANIMA


"""Initial main functionality for command line tools."""


from __future__ import annotations

import argparse


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

    if args.command == "pixelart":
        print("Hello from pixelart")
    elif args.command == "gifmaker":
        print("Hello from gifmaker")
