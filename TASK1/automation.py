import os
import shutil

# WRITE FILE
try:
    with open("sample.txt", "w") as file:
        file.write("Hello from Python file handling project.\n")
        file.write("This file was created automatically.")

    print("File created successfully!")

except Exception as e:
    print("Error:", e)

# READ FILE
try:
    with open("sample.txt", "r") as file:
        content = file.read()

    print("\nFile Content:")
    print(content)

except Exception as e:
    print("Read Error:", e)

# RENAME FILE
try:
    os.rename("sample.txt", "renamed_sample.txt")

    print("\nFile renamed successfully!")

except Exception as e:
    print("Rename Error:", e)

# MOVE FILE
try:
    shutil.move("renamed_sample.txt", "backup/renamed_sample.txt")

    print("File moved successfully!")

except Exception as e:
    print("Move Error:", e)