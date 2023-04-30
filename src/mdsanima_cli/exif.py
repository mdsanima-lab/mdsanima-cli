# Copyright © 2023 Marcin Różewski MDSANIMA


"""Aadding a exif meta data to images."""


from __future__ import annotations

import piexif
import piexif.helper

from ._version import version  # pylint: disable=E0401


def get_exif_bytes(comment: str) -> None:
    """Adding a `Software` and `UserComment` exif tags. Returning bytes."""

    # Add new exif data.
    software = f"MDSANIMA-CLI {version}"
    user_comment = piexif.helper.UserComment.dump(f"{comment} by mdsanima-cli")

    # Dump exif bytes software and user comment.
    exif_bytes = piexif.dump(
        {
            "0th": {piexif.ImageIFD.Software: software},
            "Exif": {piexif.ExifIFD.UserComment: user_comment},
        },
    )

    return exif_bytes
