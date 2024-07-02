import subprocess

# Command to start VPN connection
vpn_command = "<command_to_start_vpn>"
# Command to start your application
application_command = "<command_to_start_application>"

# Execute VPN command
subprocess.run(vpn_command, shell=True)

# Execute application command
subprocess.run(application_command, shell=True)

urls = [
    "https://mail.google.com/mail/u/0/#inbox",
    "https://outlook.office.com/mail/"
    "https://www.linkedin.com/jobs/"
]

edge_path = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"  # Path to your Edge executable

for url in urls:
    subprocess.Popen([edge_path, url])
