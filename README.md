# System Monitoring Tool

This is a Python script designed to monitor system processes and resources on a Windows machine. It collects information about running processes, CPU usage, memory usage, disk usage, network statistics, and more. 

## Features

- Lists all running processes with their PID, name, and user.
- Reports CPU usage.
- Provides memory usage statistics (total and available memory).
- Includes disk usage details (total, used, and free space).
- Shows network statistics (bytes sent and received).
- Lists active network connections and their statuses.
- Displays system uptime.
- Analyzes processes for known threat patterns.

## How to Use

1. Install the required Python package:
   ```bash
   pip install psutil
