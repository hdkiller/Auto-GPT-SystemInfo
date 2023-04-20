"""Gets system information."""
from __future__ import annotations

import distro
import platform


def get_system_information() -> str:
    """
    Gets system information.

    Returns:
        str: The system information.
    """

    # Get system architecture
    arch = platform.architecture()[0]

    # Get system distribution (works on Linux only)
    if platform.system() == "Linux":
        distro_name = distro.name()
        distro_version = distro.version()
        distro_id = distro.id()

        distro_info = f"{distro_name} {distro_version} ({distro_id})"
    else:
        distro_info = None

    # Get Windows version (works on Windows only)
    if platform.system() == "Windows":
        win_ver = platform.win32_ver()
        win_version = f"{win_ver[0]} {win_ver[1]} {win_ver[4]}"
    else:
        win_version = None

    # Get macOS version (works on macOS only)
    if platform.system() == "Darwin":
        mac_ver = platform.mac_ver()
        mac_version = f"{mac_ver[0]} {mac_ver[2]}"
    else:
        mac_version = None

    # Build the prompt
    if distro_info:
        os_info = f"Linux {arch} {distro_info}"
    if win_version:
        os_info = f"Windows {win_version}"
    if mac_version:
        os_info = f"macOS {mac_version}"

    return os_info
