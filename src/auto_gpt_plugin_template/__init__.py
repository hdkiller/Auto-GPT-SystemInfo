"""This is a system information plugin for Auto-GPT."""
import platform
from typing import TypeVar
import distro

from auto_gpt_plugin_template  import AutoGPTPluginTemplate

PromptGenerator = TypeVar("PromptGenerator")

class SystemInformationPlugin(AutoGPTPluginTemplate):
    """
    This is a system information plugin for Auto-GPT. It adds the system information to the prompt. 
    It works on Linux, Windows and macOS.
    """

    def __init__(self):
        super().__init__()
        self._name = "Auto-GPT-Plugin-SystemInfo"
        self._version = "0.1.0"
        self._description = "This is system info plugin for Auto-GPT."

    def get_system_info(self) -> str:
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

    def post_prompt(self, prompt: PromptGenerator) -> PromptGenerator:
        os_info = self.get_system_info()
        if os_info:
            prompt.add_resource(
                f"Shell commands executed on {os_info}",
            )

        return prompt