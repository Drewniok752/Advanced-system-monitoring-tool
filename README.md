# Advanced System Monitoring Tool

This repository contains a Python script designed to monitor various aspects of a Windows system. The tool provides detailed information on system processes, resource usage, and potential threats. It generates both text and CSV reports for comprehensive analysis.

## Features

- **Process Listing**: Lists all running processes with their Process ID (PID), name, and user.
- **CPU Usage**: Reports current CPU usage as a percentage.
- **Memory Usage**: Provides details on total memory, available memory, and memory usage percentage.
- **Disk Usage**: Displays total disk space, used space, and free space.
- **Network Statistics**: Shows the amount of data sent and received over the network.
- **Active Network Connections**: Lists active network connections with their local and remote addresses and status.
- **System Uptime**: Shows how long the system has been running since the last boot.
- **Threat Analysis**: Identifies processes that match known threat patterns.

## Installation

1. **Install Python**: Ensure you have Python 3.x installed. You can download it from [python.org](https://www.python.org/downloads/).

2. **Install Required Python Package**:
   Open Command Prompt and install the `psutil` package using pip:

   ```bash
   pip install psutil
