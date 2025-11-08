from __future__ import annotations

"""
    * SPDX-FileCopyrightText: Copyright 2024 LG Electronics Inc.
    * SPDX-License-Identifier: Apache-2.0
"""
from dataclasses import dataclass
from typing import Any

from .connect_device import ConnectBaseDevice, ConnectDeviceProfile
from .const import Property, Resource


class RobotCleanerProfile(ConnectDeviceProfile):
    def __init__(self, profile: dict[str, Any]):
        super().__init__(
            profile=profile,
            resource_map={
                "runState": Resource.RUN_STATE,
                "robotCleanerJobMode": Resource.ROBOT_CLEANER_JOB_MODE,
                "operation": Resource.OPERATION,
                "battery": Resource.BATTERY,
                "timer": Resource.TIMER,
            },
            profile_map={
                "runState": {"currentState": Property.CURRENT_STATE},
                "robotCleanerJobMode": {"currentJobMode": Property.CURRENT_JOB_MODE},
                "operation": {"cleanOperationMode": Property.CLEAN_OPERATION_MODE},
                "battery": {"level": Property.BATTERY_LEVEL, "percent": Property.BATTERY_PERCENT},
                "timer": {
                    "absoluteHourToStart": Property.ABSOLUTE_HOUR_TO_START,
                    "absoluteMinuteToStart": Property.ABSOLUTE_MINUTE_TO_START,
                    "runningHour": Property.RUNNING_HOUR,
                    "runningMinute": Property.RUNNING_MINUTE,
                },
            },
        )


@dataclass
class RobotCleanerDevice(ConnectBaseDevice):
    """RobotCleaner Property."""

    PROFILE_TYPE = RobotCleanerProfile

    _CUSTOM_SET_PROPERTY_NAME = {
        Property.ABSOLUTE_HOUR_TO_START: "absolute_time_to_start",
        Property.ABSOLUTE_MINUTE_TO_START: "absolute_time_to_start",
    }

    @property
    def profiles(self) -> RobotCleanerProfile:
        return self._profiles

    @profiles.setter
    def profiles(self, profiles: RobotCleanerProfile):
        self._profiles = profiles

    async def set_clean_operation_mode(self, mode: str) -> dict | None:
        return await self.do_enum_attribute_command(Property.CLEAN_OPERATION_MODE, mode)

    async def set_absolute_time_to_start(self, hour: int, minute: int) -> dict | None:
        return await self.do_multi_attribute_command(
            {
                Property.ABSOLUTE_HOUR_TO_START: hour,
                Property.ABSOLUTE_MINUTE_TO_START: minute,
            }
        )
