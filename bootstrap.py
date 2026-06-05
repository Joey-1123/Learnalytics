import subprocess

# Install dependencies and run
subprocess.check_call(["uv", "sync"])
subprocess.check_call(["uv", "run", "manage.py", "runserver"])