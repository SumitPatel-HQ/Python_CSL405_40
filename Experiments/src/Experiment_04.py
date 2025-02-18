from pathlib import Path

# Get all files in the current directory
files = [file.name for file in Path('.').iterdir() if file.is_file()]

print("Files in the current directory:")
for file in files:
   
