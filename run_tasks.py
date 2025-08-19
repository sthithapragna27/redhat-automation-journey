print("===Runing Automation Tasks===")
print("Task 1: Checking system info...")
import subprocess
subprocess.run(["python", "system_check.py"])
print("\nTask 2: Showing current directory...")
subprocess.run(["pwd"], shell=True)
print("\nTask 3: Listing files...")
subprocess.run(["ls", "-la"], shell=True)
print("\n=== All tasks completed! ===")
