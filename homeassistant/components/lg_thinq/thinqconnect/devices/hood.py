from __future__ import annotations

"""
    * SPDX-FileCopyrightText: Copyright 2024 LG Electronics Inc.
    * SPDX-License-Identifier: Apache-2.0
"""
from dataclasses import dataclass
from typing import Any

from .connect_device import ConnectBaseDevice, ConnectDeviceProfile
from .const import Property, Resource


class HoodProfile(ConnectDeviceProfile):
    def __init__(self, profile: dict[str, Any]):
        super().__init__(
            profile=profile,
            resource_map={
                "ventilation": Resource.VENTILATION,
                "lamp": Resource.LAMP,
                "operation": Resource.OPERATION,
            },
            profile_map={
                "ventilation": {
                    "fanSpeed": Property.FAN_SPEED,
                },
                "lamp": {
                    "lampBrightness": Property.LAMP_BRIGHTNESS,
                },
                "operation": {
                    "hoodOperationMode": Property.HOOD_OPERATION_MODE,
                },
            },
        )


@dataclass
class HoodDevice(ConnectBaseDevice):
    """Oven Property."""

    PROFILE_TYPE = HoodProfile

    @property
    def profiles(self) -> HoodProfile:
        return self._profiles

    @profiles.setter
    def profiles(self, profiles: HoodProfile):
        self._profiles = profiles

    async def set_fan_speed_lamp_brightness(self, fan_speed: int, lamp_brightness: int) -> dict | None:
        return await self.do_multi_range_attribute_command(
            {
                Property.FAN_SPEED: fan_speed,
                Property.LAMP_BRIGHTNESS: lamp_brightness,
            }
        )

    async def set_fan_speed(self, fan_speed: int) -> dict | None:
        return await self.do_multi_range_attribute_command(
            {Property.FAN_SPEED: fan_speed, Property.LAMP_BRIGHTNESS: self.lamp_brightness}
        )

    async def set_lamp_brightness(self, lamp_brightness: int) -> dict | None:
        return await self.do_multi_range_attribute_command(
            {
                Property.FAN_SPEED: self.fan_speed,
                Property.LAMP_BRIGHTNESS: lamp_brightness,
            }
        )
