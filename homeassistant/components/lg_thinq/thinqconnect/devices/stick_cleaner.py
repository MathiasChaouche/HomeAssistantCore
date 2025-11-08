from __future__ import annotations

"""
    * SPDX-FileCopyrightText: Copyright 2024 LG Electronics Inc.
    * SPDX-License-Identifier: Apache-2.0
"""
from dataclasses import dataclass
from typing import Any

from .connect_device import ConnectBaseDevice, ConnectDeviceProfile
from .const import Property, Resource


class StickCleanerProfile(ConnectDeviceProfile):
    def __init__(self, profile: dict[str, Any]):
        super().__init__(
            profile=profile,
            resource_map={
                "runState": Resource.RUN_STATE,
                "stickCleanerJobMode": Resource.STICK_CLEANER_JOB_MODE,
                "battery": Resource.BATTERY,
            },
            profile_map={
                "runState": {"currentState": Property.CURRENT_STATE},
                "stickCleanerJobMode": {
                    "currentJobMode": Property.CURRENT_JOB_MODE,
                },
                "battery": {"level": Property.BATTERY_LEVEL, "percent": Property.BATTERY_PERCENT},
            },
        )


@dataclass
class StickCleanerDevice(ConnectBaseDevice):
    """StickCleaner Property."""

    PROFILE_TYPE = StickCleanerProfile

    @property
    def profiles(self) -> StickCleanerProfile:
        return self._profiles

    @profiles.setter
    def profiles(self, profiles: StickCleanerProfile):
        self._profiles = profiles
