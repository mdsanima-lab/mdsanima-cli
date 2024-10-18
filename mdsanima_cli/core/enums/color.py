# Copyright (c) 2023 MDSANIMA

"""Color styles definition in HEX values that share between a group of enumerations."""


from __future__ import annotations

from enum import Enum
from enum import unique


@unique
class Color(Enum):
    """The default color names whose base color is 500 from the shade number and the value is HEX code with the hash."""

    LIGHT = "#cad1d9"
    DARK = "#171b22"
    NIGHT = "#2b3558"
    STORM = "#f45270"
    SHINE = "#84a85c"
    TOKYO = "#277a75"
    TOWN = "#549daa"
    CYAN = "#06b6d4"
    SKY = "#0ea5e9"
    BLUE = "#3b82f6"
    INDIGO = "#6366f1"
    VIOLET = "#8b5cf6"
    PURPLE = "#a855f7"
    FUCHSIA = "#d946ef"
    PINK = "#ec4899"
    ROSE = "#f43f5e"
    RED = "#ef4444"
    ORANGE = "#f97316"
    AMBER = "#f59e0b"
    YELLOW = "#eab308"
    LIME = "#84cc16"
    GREEN = "#22c55e"
    EMERALD = "#10b981"
    TEAL = "#14b8a6"
    GRAPHE = "#2e83b4"
    GITTER = "#476bb2"
    SLATE = "#64748b"
    GRAY = "#6b7280"
    ZINC = "#71717a"
    NEUTRAL = "#737373"
    BASIC = "#777777"
    STONE = "#78716c"
