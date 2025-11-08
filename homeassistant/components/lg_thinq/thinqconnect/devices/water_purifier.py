from __future__ import annotations

"""
    * SPDX-FileCopyrightText: Copyright 2024 LG Electronics Inc.
    * SPDX-License-Identifier: Apache-2.0
"""
from dataclasses import dataclass
from typing import Any

from .connect_device import ConnectBaseDevice, ConnectDeviceProfile
from .const import Property, Resource


class WaterPurifierProfile(ConnectDeviceProfile):
    def __init__(self, profile: dict[str, Any]):
        super().__init__(
            profile=profile,
            resource_map={"runState": Resource.RUN_STATE, "waterInfo": Resource.WATER_INFO},
            profile_map={
                "runState": {"cockState": Property.COCK_STATE, "sterilizingState": Property.STERILIZING_STATE},
                "waterInfo": {"waterType": Property.WATER_TYPE},
            },
        )


@dataclass
class WaterPurifierDevice(ConnectBaseDevice):
    """WaterPurifier Property."""

    PROFILE_TYPE = WaterPurifierProfile

    @property
    def profiles(self) -> WaterPurifierProfile:
        return self._profiles

    @profiles.setter
    def profiles(self, profiles: WaterPurifierProfile):
        self._profiles = profiles
