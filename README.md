# System Information plugin for Auto-GPT

## Overview

This plugin provides an additional line to the prompt which supposed to be a hint for the AI to use shell commands which is probably supported on the current system.

**Example prompt**:

   - "Shell commands executed on Linux 64bit Debian GNU/Linux 11 (debian)"

This helps the model to provide commands which is compatible with the current operation system and makes it able to use system specific package managers for example. 

## Installation

Download this repository as a .zip file and copy to ./plugins/ and rename it Auto-GPT-SystemInfo.zip

You can run this command from your Auto-GPT directory to download:

```
curl -o ./plugins/Auto-GPT-SystemInfo.zip https://github.com/hdkiller/Auto-GPT-SystemInfo/archive/refs/heads/master.zip 
```

## Compatibility

The plugin supports Linux, MacOs and Windows. 



