from __future__ import annotations

"""
    * SPDX-FileCopyrightText: Copyright 2024 LG Electronics Inc.
    * SPDX-License-Identifier: Apache-2.0
"""
from dataclasses import dataclass
from typing import Any

from .connect_device import ConnectBaseDevice, ConnectDeviceProfile
from .const import Property, Resource


class CeilingFanProfile(ConnectDeviceProfile):
    def __init__(self, profile: dict[str, Any]):
        super().__init__(
            profile=profile,
            resource_map={"airFlow": Resource.AIR_FLOW, "operation": Resource.OPERATION},
            profile_map={
                "airFlow": {"windStrength": Property.WIND_STRENGTH},
                "operation": {"ceilingfanOperationMode": Property.CEILING_FAN_OPERATION_MODE},
            },
        )


@dataclass
class CeilingFanDevice(ConnectBaseDevice):
    """CeilingFan Property."""

    PROFILE_TYPE = CeilingFanProfile

    @property
    def profiles(self) -> CeilingFanProfile:
        return self._profiles

    @profiles.setter
    def profiles(self, profiles: CeilingFanProfile):
        self._profiles = profiles

    async def set_wind_strength(self, wind_strength: str) -> dict | None:
        return await self.do_enum_attribute_command(Property.WIND_STRENGTH, wind_strength)

    async def set_ceiling_fan_operation_mode(self, mode: str) -> dict | None:
        return await self.do_enum_attribute_command(Property.CEILING_FAN_OPERATION_MODE, mode)
