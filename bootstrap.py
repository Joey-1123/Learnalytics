import os
import subprocess
import sys

VENV_DIR = ".venv"

# 1. Create virtual environment if it doesn't exist
if not os.path.exists(VENV_DIR):
    print("Creating virtual environment...")
    subprocess.check_call([sys.executable, "-m", "venv", VENV_DIR])

# 2. Determine paths (Windows uses Scripts)
if os.name == "nt":
    python = os.path.join(VENV_DIR, "Scripts", "python.exe")
    pip = os.path.join(VENV_DIR, "Scripts", "pip.exe")
else:
    python = os.path.join(VENV_DIR, "bin", "python")
    pip = os.path.join(VENV_DIR, "bin", "pip")

# 3. Install dependencies
print("Installing requirements...")
subprocess.check_call([pip, "install", "-r", "requirements.txt"])

# 4. Run Django server
print("Starting Django server...")
subprocess.check_call([python, "manage.py", "runserver"])