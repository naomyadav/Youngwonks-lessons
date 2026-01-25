import subprocess
import shlex

app_path = "/Applications/Google Chrome.app"
url = "" # Optional: specify a URL to open

# The command to run in the terminal
cmd = f"open -a '{app_path}' {url}"

# Use shlex.split to handle spaces in the path correctly
cmd_parts = shlex.split(cmd)

try:
    # Run the command
    subprocess.run(cmd_parts, check=True)
    print(f"Opened {app_path}")
except FileNotFoundError:
    print(f"Error: Application not found at {app_path}")
except subprocess.CalledProcessError as e:
    print(f"Error running command: {e}")
except PermissionError as e:
    # This specific error is less likely with the 'open' command but included for completeness
    print(f"Permission denied: {e}")
