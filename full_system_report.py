import psutil
from datetime import datetime
import csv

def log_system_info_txt(file_path):
    with open(file_path, 'a') as f:
        # Write timestamp
        f.write(f"--- System Information Report - {datetime.now()} ---\n\n")

        # Write process information
        f.write("Listing all running processes:\n")
        for proc in psutil.process_iter(['pid', 'name', 'username']):
            try:
                f.write(f"PID: {proc.info['pid']}, Name: {proc.info['name']}, User: {proc.info['username']}\n")
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                continue
        f.write("\n")

        # Write CPU usage
        cpu_usage = psutil.cpu_percent(interval=1)
        f.write(f"CPU Usage: {cpu_usage}%\n")

        # Write memory usage
        memory = psutil.virtual_memory()
        f.write(f"Memory Usage: {memory.percent}%\n")
        f.write(f"Total Memory: {memory.total / (1024 * 1024):.2f} MB\n")
        f.write(f"Available Memory: {memory.available / (1024 * 1024):.2f} MB\n")
        f.write("\n")

        # Write disk usage
        disk_usage = psutil.disk_usage('/')
        f.write(f"Disk Usage: {disk_usage.percent}%\n")
        f.write(f"Total Disk Space: {disk_usage.total / (1024 * 1024 * 1024):.2f} GB\n")
        f.write(f"Used Disk Space: {disk_usage.used / (1024 * 1024 * 1024):.2f} GB\n")
        f.write(f"Free Disk Space: {disk_usage.free / (1024 * 1024 * 1024):.2f} GB\n")
        f.write("\n")

        # Write network statistics
        net_io = psutil.net_io_counters()
        f.write(f"Bytes Sent: {net_io.bytes_sent / (1024 * 1024):.2f} MB\n")
        f.write(f"Bytes Received: {net_io.bytes_recv / (1024 * 1024):.2f} MB\n")
        f.write("\n")

        # Write active network connections
        f.write("Active Network Connections:\n")
        for conn in psutil.net_connections(kind='inet'):
            f.write(f"Local Address: {conn.laddr}, Remote Address: {conn.raddr}, Status: {conn.status}\n")
        f.write("\n")

        # Write system uptime
        uptime = datetime.now() - datetime.fromtimestamp(psutil.boot_time())
        f.write(f"System Uptime: {uptime}\n")

        # Write process threat analysis
        threat_processes = ["malware", "virus", "spyware"]  # Add known threat process names or patterns
        f.write("Process Threat Analysis:\n")
        for proc in psutil.process_iter(['pid', 'name']):
            try:
                if any(threat in proc.info['name'].lower() for threat in threat_processes):
                    f.write(f"Threat Detected - PID: {proc.info['pid']}, Name: {proc.info['name']}\n")
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                continue
        f.write("\n")

        f.write("End of Report\n\n")

def log_system_info_csv(file_path):
    with open(file_path, 'w', newline='') as csvfile:
        fieldnames = ['Metric', 'Value']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()

        # Write CPU usage
        cpu_usage = psutil.cpu_percent(interval=1)
        writer.writerow({'Metric': 'CPU Usage', 'Value': f'{cpu_usage}%'})

        # Write memory usage
        memory = psutil.virtual_memory()
        writer.writerow({'Metric': 'Memory Usage', 'Value': f'{memory.percent}%'})
        writer.writerow({'Metric': 'Total Memory', 'Value': f'{memory.total / (1024 * 1024):.2f} MB'})
        writer.writerow({'Metric': 'Available Memory', 'Value': f'{memory.available / (1024 * 1024):.2f} MB'})

        # Write disk usage
        disk_usage = psutil.disk_usage('/')
        writer.writerow({'Metric': 'Disk Usage', 'Value': f'{disk_usage.percent}%'})
        writer.writerow({'Metric': 'Total Disk Space', 'Value': f'{disk_usage.total / (1024 * 1024 * 1024):.2f} GB'})
        writer.writerow({'Metric': 'Used Disk Space', 'Value': f'{disk_usage.used / (1024 * 1024 * 1024):.2f} GB'})
        writer.writerow({'Metric': 'Free Disk Space', 'Value': f'{disk_usage.free / (1024 * 1024 * 1024):.2f} GB'})

        # Write network statistics
        net_io = psutil.net_io_counters()
        writer.writerow({'Metric': 'Bytes Sent', 'Value': f'{net_io.bytes_sent / (1024 * 1024):.2f} MB'})
        writer.writerow({'Metric': 'Bytes Received', 'Value': f'{net_io.bytes_recv / (1024 * 1024):.2f} MB'})

        # Write active network connections
        writer.writerow({'Metric': 'Active Network Connections', 'Value': 'See detailed text report for connection details'})

        # Write system uptime
        uptime = datetime.now() - datetime.fromtimestamp(psutil.boot_time())
        writer.writerow({'Metric': 'System Uptime', 'Value': str(uptime)})

        # Write process threat analysis
        threat_processes = ["malware", "virus", "spyware"]  # Add known threat process names or patterns
        threat_found = False
        for proc in psutil.process_iter(['pid', 'name']):
            try:
                if any(threat in proc.info['name'].lower() for threat in threat_processes):
                    writer.writerow({'Metric': 'Threat Detected', 'Value': f'PID: {proc.info["pid"]}, Name: {proc.info["name"]}'})
                    threat_found = True
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                continue
        if not threat_found:
            writer.writerow({'Metric': 'Threat Detected', 'Value': 'No threats detected'})

if __name__ == "__main__":
    # Define file paths
    report_file_txt = "system_report.txt"
    report_file_csv = "system_report.csv"
    
    # Log system information
    log_system_info_txt(report_file_txt)
    log_system_info_csv(report_file_csv)
    
    print(f"System information has been logged to {report_file_txt} and {report_file_csv}")
