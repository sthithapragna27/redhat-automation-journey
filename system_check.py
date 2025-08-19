import platform
import os

print("=== My Computer Info ===")
print("Operating System:", platform.system())
print("Computer Name:", platform.node())
print("Current User:", os.getenv("USERNAME"))
print("Python Version:", Platform.python_version())
