"""
    * SPDX-FileCopyrightText: Copyright 2024 LG Electronics Inc.
    * SPDX-License-Identifier: Apache-2.0
"""
from dataclasses import dataclass

from .dryer import DryerDevice


@dataclass
class WashtowerDryerDevice(DryerDevice):
    pass
