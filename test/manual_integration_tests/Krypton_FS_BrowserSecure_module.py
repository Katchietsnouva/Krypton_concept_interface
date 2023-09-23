# Import necessary modules from Python's standard library
from concurrent.futures import ThreadPoolExecutor
from flask import Flask, render_template
import os
from pathlib import Path

# Initialize Firebase with your service account key JSON file
# import sys
import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate("path/to/serviceAccountKey.json")
firebase_admin.initialize_app(cred)




# Create the Flask app using a function
def create_app():
    app = Flask(__name__)
    # Your routes and other app configuration here...
    # Routes for web application
    @app.route('/')
    def index():
        # Get the path of the 'Documents' folder
        documents_folder_path = os.path.expanduser("~/Documents")

        # Create the log file name using the current directory path
        # Get the parent directory of the code file (where the code is located)
        code_parent_directory = os.path.dirname(__file__)
        # Combine the parent directory with the 'bin' folder name to get the log file path
        log_file_name = os.path.join(code_parent_directory, "bin", "1.txt")

        # Check if the 'bin' folder exists, if not, create it
        bin_folder_path = os.path.join(code_parent_directory, "bin")
        if not os.path.exists(bin_folder_path):
            os.makedirs(bin_folder_path)

        # Open the log file with utf-8 encoding
        with open(log_file_name, "w", encoding="utf-8") as log_file:
            # Write the path of the script to the log file
            log_file.write(f"Current Code File Location: {__file__}\n")
            # Add separation (3-line separation)
            log_file.write("\n" * 3)

            # Call the function to list directories and files in the "Documents" folder
            list_directories_and_files(documents_folder_path, log_file, "Documents folder")

            # Add separation (3-line separation)
            log_file.write("\n" * 3)

            # Get the path of the "Downloads" folder and list its directories and files
            try:
                downloads_folder_path = get_downloads_folder_path()
                if downloads_folder_path != documents_folder_path:
                    list_directories_and_files(downloads_folder_path, log_file, "Downloads folder", indent_level=1)
            except Exception as e:
                with open(log_file_name, "a", encoding="utf-8") as log_file:
                    log_file.write(f"\n\nFailed to get folder path for Downloads folder. Error: {e}")

        # Read the contents of the log file
        with open(log_file_name, "r", encoding="utf-8") as read_log_file:
            log_contents = read_log_file.readlines()

        return render_template('index.html', log_contents=log_contents)
    return app



# Function to list directories and files in the specified path
def list_directories_and_files(path, log_file, title, indent_level=0):
    # Write a heading for directories and files in the log file
    log_file.write(f"{title}:\n")
    indent = "\t" * indent_level
    indent_for_files = "\t" * (indent_level + 1)

    # Initialize lists to store the names of directories and files
    directories = []
    files = []

    # Loop through all entries (files and directories) in the specified path
    for entry in os.listdir(path):
        entry_path = os.path.join(path, entry)

        # Check if the entry is a directory
        if os.path.isdir(entry_path):
            # Exclude special directories '.' and '..' from the listing
            if entry not in ('.', '..'):
                directories.append(entry)
        
        # Check if the entry is a file
        elif os.path.isfile(entry_path):
            files.append(entry)

    # Write the directories to the log file
    log_file.write(f"{indent}Path: {path}\n")
    if directories:
        log_file.write(f"{indent}Directories ({len(directories)}):\n")
        for directory in directories:
            log_file.write(f"{indent_for_files}Directory: {directory}\n")
    else:
        log_file.write(f"{indent}Directories (0):\n")

    # Write the files to the log file
    if files:
        log_file.write(f"{indent}Files ({len(files)}):\n")
        for file in files:
            log_file.write(f"{indent_for_files}File: {file}\n")
    else:
        log_file.write(f"{indent}Files (0):\n")

# Function to get the path of the "Downloads" folder
def get_downloads_folder_path():
    # Check if the current system is Windows or non-Windows (like macOS, Linux)
    if os.name == 'nt':  # Windows system
        # Specify the new location of the "Downloads" folder for Windows
        downloads_folder_path = "D:/Downloads"  # Change this to your actual new path on Windows

        # Create the folder if it doesn't exist
        if not os.path.exists(downloads_folder_path):
            try:
                os.makedirs(downloads_folder_path)
            except OSError as e:
                raise OSError(f"Failed to create Downloads folder. Error: {e}")

        return downloads_folder_path
    else:  # Non-Windows system
        # Use the pathlib module to get the "Downloads" folder path for non-Windows systems
        downloads_path = str(Path.home() / "Downloads")

        # Create the folder if it doesn't exist
        if not os.path.exists(downloads_path):
            try:
                os.makedirs(downloads_path)
            except OSError as e:
                raise OSError(f"Failed to create Downloads folder. Error: {e}")
        return downloads_path

    # If the code reaches this point, it means the function couldn't determine the Downloads folder path
    raise OSError("Failed to get folder path for Downloads folder.")




# Main function
def main():
    # Get the path of the 'Documents' folder
    documents_folder_path = os.path.expanduser("~/Documents")

    # Print the current directory and the code file's location
    current_code_file_path = os.path.abspath(__file__)
    print(f"Current Code File Location: {current_code_file_path}")

    # Create the log file name using the current directory path
    # Get the parent directory of the code file (where the code is located)
    code_parent_directory = os.path.dirname(current_code_file_path)
    # Combine the parent directory with the 'bin' folder name to get the log file path
    log_file_name = os.path.join(code_parent_directory, "bin", "1.txt")

    # Check if the 'bin' folder exists, if not, create it
    bin_folder_path = os.path.join(code_parent_directory, "bin")
    if not os.path.exists(bin_folder_path):
        os.makedirs(bin_folder_path)

    # Open the log file with utf-8 encoding
    with open(log_file_name, "w", encoding="utf-8") as log_file:
        # Write the path of the script to the log file
        log_file.write(f"Current Code File Location: {current_code_file_path}\n")
        # Add separation (3-line separation)
        log_file.write("\n" * 3)

        # Call the function to list directories and files in the "Documents" folder
        list_directories_and_files(documents_folder_path, log_file, "Documents folder")

        # Add separation (3-line separation)
        log_file.write("\n" * 3)

        # Get the path of the "Downloads" folder and list its directories and files
        try:
            downloads_folder_path = get_downloads_folder_path()
            if downloads_folder_path != documents_folder_path:
                list_directories_and_files(downloads_folder_path, log_file, "Downloads folder", indent_level=1)
        except Exception as e:
            with open(log_file_name, "a", encoding="utf-8") as log_file:
                log_file.write(f"\n\nFailed to get folder path for Downloads folder. Error: {e}")

    # Print a success message with the log file name
    print(f"Successfully logged to {log_file_name}")

     # Read and print the contents of the log file to the console
    print("\nLogged Contents:")
    with open(log_file_name, "r", encoding="utf-8") as read_log_file:
        for line in read_log_file:
            print(line.rstrip().encode(sys.stdout.encoding, errors='replace').decode(sys.stdout.encoding))


if __name__ == "__main__":
    with ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(main)
        executor.submit(create_app().run)

