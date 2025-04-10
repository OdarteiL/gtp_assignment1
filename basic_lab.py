import os
import shutil
import requests
from datetime import datetime


folder_name = "michael_lamptey"
file_name = f"{folder_name}.txt"
url = "https://raw.githubusercontent.com/sdg000/pydevops_intro_lab/main/change_me.txt"

# Checking to remove the folder if it already exists
if os.path.exists(folder_name):
    try:
        shutil.rmtree(folder_name)
        print(f"Removed existing folder: {folder_name}")
    except Exception as e:
        print(f"Error removing folder: {e}")


# creating the custom directory
if not os.path.exists(folder_name):
    os.makedirs(folder_name)
    print(f"Created directory: {folder_name}")
else:
    print(f"Directory already exists: {folder_name}")


# Creating a file in the directory
local_file_path = os.path.join(folder_name, file_name)
# print(f"Creating file: {local_file_path}")

# To now download the file from the URL
response = requests.get(url)

if response.status_code == 200:
    print("File downloaded successfully.")
    with open(local_file_path, "wb") as file:
        file.write(response.content)
        print("File saved successfully.")
else:
    print(f"Failed to download file. Status code: {response.status_code}")
    exit(1)


# Modiifying the file
user_input = input("Describe what you have learned so far in a sentence: ")

# Get current date and time
now = datetime.now()
current_time = now.strftime("%Y-%m-%d %H:%M:%S")

# Insert the new content
with open(local_file_path, "w") as file:
    file.write(user_input + "\n")
    file.write(f"Last modified: {current_time}\n")

# Print the contents of the file
print("File successfully modified.")


# final step
with open(local_file_path, "r") as file:
    print("\nYou Entered:")
    print(file.read())