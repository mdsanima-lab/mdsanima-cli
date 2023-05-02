# Copyright © 2023 Marcin Różewski MDSANIMA


"""Aadding a exif meta data to images."""


from __future__ import annotations

import piexif
import piexif.helper

from mdsanima_cli._version import __version__


def get_exif_bytes(user_comment: str) -> bytes:
    """Adding a `Software` and `UserComment` exif tags. Returning bytes."""

    # Add new exif data.
    software = f"MDSANIMA-CLI {__version__}"
    comment = piexif.helper.UserComment.dump(f"{user_comment} by mdsanima-cli")

    # Dump exif bytes software and user comment.
    exif_bytes = piexif.dump(
        {
            "0th": {piexif.ImageIFD.Software: software},
            "Exif": {piexif.ExifIFD.UserComment: comment},
        },
    )

    return exif_bytes
