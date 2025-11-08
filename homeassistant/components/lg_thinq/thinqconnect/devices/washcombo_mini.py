"""
    * SPDX-FileCopyrightText: Copyright 2024 LG Electronics Inc.
    * SPDX-License-Identifier: Apache-2.0
"""
from dataclasses import dataclass

from .washcombo import WashcomboDevice


@dataclass
class WashcomboMiniDevice(WashcomboDevice):
    location_name: str = "MINI"
