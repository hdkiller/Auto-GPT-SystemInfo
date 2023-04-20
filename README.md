# System Information plugin for Auto-GPT

This plugin provides an additional line to the prompt which supposed to be a hint for the AI to use shell commands which is probably supported on the current system.

Example prompt:
   "Shell commands executed on Linux 64bit Debian GNU/Linux 11 (debian)"

This helps the model to provide commands which is compatible with the current operation system and makes it able to use system specific package managers for example. 

The plugin supports Linux, MacOs and Windows. 

