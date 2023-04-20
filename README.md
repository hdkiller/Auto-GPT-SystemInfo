# System Information Plugin for Auto-GPT

## Overview

This plugin adds an extra line to the prompt, serving as a hint for the AI to use shell commands likely supported by the current system.

**Example prompt**:

   - "Shell commands executed on Linux 64bit Debian GNU/Linux 11 (debian)"

This helps the model provide commands compatible with the current operating system and enables it to use system-specific package managers, for example.

## Installation

Download this repository as a .zip file, copy it to ./plugins/, and rename it to Auto-GPT-SystemInfo.zip.

To download it directly from your Auto-GPT directory, you can run this command:

```
curl -o ./plugins/Auto-GPT-SystemInfo.zip https://github.com/hdkiller/Auto-GPT-SystemInfo/archive/refs/heads/master.zip 
```

## Compatibility

The plugin supports Linux, macOS, and Windows.