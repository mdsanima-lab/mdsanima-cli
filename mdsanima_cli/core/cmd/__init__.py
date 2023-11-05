# Copyright (c) 2023 MDSANIMA

"""This module holds the all commands functionality on the `CLI` interface."""


from mdsanima_cli.core.cmd.check import check
from mdsanima_cli.core.cmd.gifmaker import gifmaker
from mdsanima_cli.core.cmd.grid import grid
from mdsanima_cli.core.cmd.ico import ico
from mdsanima_cli.core.cmd.jpg import jpg
from mdsanima_cli.core.cmd.logo import logo
from mdsanima_cli.core.cmd.number import number
from mdsanima_cli.core.cmd.pixelart import pixelart
from mdsanima_cli.core.cmd.png import png
from mdsanima_cli.core.cmd.resize import resize
from mdsanima_cli.core.cmd.thumbnail import thumbnail
from mdsanima_cli.core.cmd.uuid import uuid
from mdsanima_cli.core.cmd.watermark import watermark
from mdsanima_cli.core.cmd.webp import webp


__all__ = [
    "check",
    "gifmaker",
    "grid",
    "ico",
    "jpg",
    "logo",
    "number",
    "pixelart",
    "png",
    "resize",
    "thumbnail",
    "uuid",
    "watermark",
    "webp",
]
