# Copyritht © 2023 Marcin Różewski MDSANIMA


"""This module is for several utils that we may be use for command line tools.
The module may be used in development.
"""


from __future__ import annotations

import os


def get_directory_info() -> dict:
    """Checking the directory and returning information about that."""
    real_path = os.path.realpath(os.curdir)
    directory = os.listdir()

    files_count = len(directory)
    image_png_count = 0
    image_jpg_count = 0
    other_file_count = 0

    for file in directory:
        extension = os.path.splitext(file)[-1].lower()
        if extension == ".png":
            image_png_count += 1
        elif extension == ".jpg":
            image_jpg_count += 1
        else:
            other_file_count += 1

    directory_info = {
        "real_path": real_path,
        "files_count": files_count,
        "image_png_count": image_png_count,
        "image_jpg_count": image_jpg_count,
        "other_file_count": other_file_count,
    }

    return directory_info
