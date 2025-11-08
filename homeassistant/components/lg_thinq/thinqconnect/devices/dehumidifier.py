from __future__ import annotations

"""
    * SPDX-FileCopyrightText: Copyright 2024 LG Electronics Inc.
    * SPDX-License-Identifier: Apache-2.0
"""
from dataclasses import dataclass
from typing import Any

from .connect_device import ConnectBaseDevice, ConnectDeviceProfile
from .const import Property, Resource


class DehumidifierProfile(ConnectDeviceProfile):
    def __init__(self, profile: dict[str, Any]):
        super().__init__(
            profile=profile,
            resource_map={
                "operation": Resource.OPERATION,
                "dehumidifierJobMode": Resource.DEHUMIDIFIER_JOB_MODE,
                "humidity": Resource.HUMIDITY,
                "airFlow": Resource.AIR_FLOW,
            },
            profile_map={
                "operation": {"dehumidifierOperationMode": Property.DEHUMIDIFIER_OPERATION_MODE},
                "dehumidifierJobMode": {"currentJobMode": Property.CURRENT_JOB_MODE},
                "humidity": {
                    "currentHumidity": Property.CURRENT_HUMIDITY,
                    "targetHumidity": Property.TARGET_HUMIDITY,
                },
                "airFlow": {"windStrengthLevel": Property.WIND_STRENGTH},
            },
        )


@dataclass
class DehumidifierDevice(ConnectBaseDevice):
    PROFILE_TYPE = DehumidifierProfile

    @property
    def profiles(self) -> DehumidifierProfile:
        return self._profiles

    @profiles.setter
    def profiles(self, profiles: DehumidifierProfile):
        self._profiles = profiles

    async def set_dehumidifier_operation_mode(self, mode: str) -> dict | None:
        return await self.do_enum_attribute_command(Property.DEHUMIDIFIER_OPERATION_MODE, mode)

    async def set_target_humidity(self, target_humidity: int) -> dict | None:
        return await self.do_attribute_command(Property.TARGET_HUMIDITY, target_humidity)

    async def set_current_job_mode(self, job_mode: str) -> dict | None:
        return await self.do_enum_attribute_command(Property.CURRENT_JOB_MODE, job_mode)

    async def set_wind_strength(self, wind_strength: str) -> dict | None:
        return await self.do_enum_attribute_command(Property.WIND_STRENGTH, wind_strength)
