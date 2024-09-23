import os
import shutil
import tempfile
import stat

def display_current_directory():
    print("Current Working Directory:", os.getcwd())

def create_directory():
    dir_name = input("Enter directory name to create: ")
    try:
        os.makedirs(dir_name)
        print(f"Directory '{dir_name}' created successfully.")
    except FileExistsError:
        print(f"Directory '{dir_name}' already exists.")
    except Exception as e:
        print(f"Error creating directory: {e}")

def delete_directory():
    dir_name = input("Enter directory name to delete: ")
    try:
        os.rmdir(dir_name)
        print(f"Directory '{dir_name}' deleted successfully.")
    except FileNotFoundError:
        print(f"Directory '{dir_name}' not found.")
    except Exception as e:
        print(f"Error deleting directory: {e}")

def list_files():
    directory = input("Enter directory to list files (leave blank for current directory): ") or "."
    try:
        files = os.listdir(directory)
        print(f"Files in '{directory}': {files}")
    except FileNotFoundError:
        print(f"Directory '{directory}' not found.")
    except Exception as e:
        print(f"Error listing files: {e}")

def copy_file():
    src = input("Enter source file name: ")
    dst = input("Enter destination file name: ")
    try:
        shutil.copy(src, dst)
        print(f"File '{src}' copied to '{dst}'.")
    except FileNotFoundError:
        print(f"File '{src}' not found.")
    except Exception as e:
        print(f"Error copying file: {e}")

def move_file():
    src = input("Enter source file name: ")
    dst = input("Enter destination file name: ")
    try:
        shutil.move(src, dst)
        print(f"File '{src}' moved to '{dst}'.")
    except FileNotFoundError:
        print(f"File '{src}' not found.")
    except Exception as e:
        print(f"Error moving file: {e}")

def rename_file_or_directory():
    old_name = input("Enter old file/directory name: ")
    new_name = input("Enter new file/directory name: ")
    try:
        os.rename(old_name, new_name)
        print(f"Renamed '{old_name}' to '{new_name}'.")
    except FileNotFoundError:
        print(f"'{old_name}' not found.")
    except Exception as e:
        print(f"Error renaming: {e}")

def get_file_status():
    file_name = input("Enter file name to get status: ")
    try:
        status = os.stat(file_name)
        print(f"Status of '{file_name}':")
        print(f"Size: {status.st_size} bytes")
        print(f"Last modified: {status.st_mtime}")
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
    except Exception as e:
        print(f"Error getting file status: {e}")

def is_file_or_directory():
    path = input("Enter path to check: ")
    if os.path.isfile(path):
        print(f"'{path}' is a file.")
    elif os.path.isdir(path):
        print(f"'{path}' is a directory.")
    else:
        print(f"'{path}' is neither a file nor a directory.")

def get_environment_variables():
    env_vars = os.environ
    print("Environment Variables:")
    for key, value in env_vars.items():
        print(f"{key}: {value}")

def remove_file():
    file_name = input("Enter file name to remove: ")
    try:
        os.remove(file_name)
        print(f"File '{file_name}' removed successfully.")
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
    except Exception as e:
        print(f"Error removing file: {e}")

def change_directory():
    new_directory = input("Enter new directory path: ")
    try:
        os.chdir(new_directory)
        print(f"Changed current directory to '{new_directory}'.")
    except FileNotFoundError:
        print(f"Directory '{new_directory}' not found.")
    except Exception as e:
        print(f"Error changing directory: {e}")

def get_current_user():
    print("Current User:", os.getlogin())

def list_files_recursively():
    directory = input("Enter directory to list files recursively (leave blank for current directory): ") or "."
    for root, dirs, files in os.walk(directory):
        print(f"Root: {root}")
        for file in files:
            print(f"  File: {file}")

def check_disk_usage():
    total, used, free = shutil.disk_usage("/")
    print(f"Disk Usage:\nTotal: {total // (2**30)} GiB\nUsed: {used // (2**30)} GiB\nFree: {free // (2**30)} GiB")

def create_temp_file():
    temp_file = tempfile.NamedTemporaryFile(delete=False)
    print(f"Temporary file created at: {temp_file.name}")
    return temp_file.name

def get_parent_directory():
    path = input("Enter a path to get its parent directory: ")
    parent_dir = os.path.dirname(path)
    print(f"Parent directory of '{path}': {parent_dir}")

def list_files_with_extension():
    extension = input("Enter file extension to list (e.g., .txt): ")
    directory = input("Enter directory to search (leave blank for current directory): ") or "."
    try:
        files = [f for f in os.listdir(directory) if f.endswith(extension)]
        print(f"Files with '{extension}' in '{directory}': {files}")
    except FileNotFoundError:
        print(f"Directory '{directory}' not found.")
    except Exception as e:
        print(f"Error listing files: {e}")

def get_file_permissions():
    file_name = input("Enter file name to get permissions: ")
    try:
        permissions = os.stat(file_name).st_mode
        print(f"Permissions for '{file_name}': {oct(permissions)}")
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
    except Exception as e:
        print(f"Error getting file permissions: {e}")

def create_and_write_file():
    file_name = input("Enter file name to create and write to: ")
    content = input("Enter content to write to the file: ")
    try:
        with open(file_name, 'w') as file:
            file.write(content)
        print(f"File '{file_name}' created and content written.")
    except Exception as e:
        print(f"Error creating or writing to file: {e}")

def read_from_file():
    file_name = input("Enter file name to read from: ")
    try:
        with open(file_name, 'r') as file:
            content = file.read()
        print(f"Content of '{file_name}':\n{content}")
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
    except Exception as e:
        print(f"Error reading from file: {e}")

def list_subdirectories():
    directory = input("Enter directory to list subdirectories (leave blank for current directory): ") or "."
    try:
        subdirs = [d for d in os.listdir(directory) if os.path.isdir(os.path.join(directory, d))]
        print(f"Subdirectories in '{directory}': {subdirs}")
    except FileNotFoundError:
        print(f"Directory '{directory}' not found.")
    except Exception as e:
        print(f"Error listing subdirectories: {e}")

def check_file_exists():
    file_name = input("Enter file name to check if it exists: ")
    if os.path.exists(file_name):
        print(f"File '{file_name}' exists.")
    else:
        print(f"File '{file_name}' does not exist.")

def change_file_permissions():
    file_name = input("Enter file name to change permissions: ")
    permissions = input("Enter new permissions in octal (e.g., 0o755): ")
    try:
        os.chmod(file_name, int(permissions, 8))
        print(f"Permissions for '{file_name}' changed to {permissions}.")
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
    except Exception as e:
        print(f"Error changing permissions: {e}")

def list_processes():
    try:
        if os.name == 'posix':  # Unix-based systems
            processes = os.popen('ps aux').read()
            print("Current Processes:\n", processes)
        else:
            print("This feature is available only on Unix-based systems.")
    except Exception as e:
        print(f"Error listing processes: {e}")

def get_file_path():
    file_name = input("Enter file name to get its path: ")
    if os.path.isfile(file_name):
        print(f"Absolute path of '{file_name}': {os.path.abspath(file_name)}")
    else:
        print(f"File '{file_name}' does not exist.")

def main_menu():
    while True:
        print("\n--- Menu ---")
        print("1. Display Current Directory")
        print("2. Create Directory")
        print("3. Delete Directory")
        print("4. List Files")
        print("5. Copy File")
        print("6. Move File")
        print("7. Rename File/Directory")
        print("8. Get File Status")
        print("9. Check if Path is File or Directory")
        print("10. Get Environment Variables")
        print("11. Remove File")
        print("12. Change Directory")
        print("13. Get Current User")
        print("14. List Files Recursively")
        print("15. Check Disk Usage")
        print("16. Create Temporary File")
        print("17. Get Parent Directory")
        print("18. List Files with Specific Extension")
        print("19. Get File Permissions")
        print("20. Create and Write to a File")
        print("21. Read from a File")
        print("22. List Subdirectories")
        print("23. Check If File Exists")
        print("24. Change File Permissions")
        print("25. List Processes")
        print("26. Get File Path")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            display_current_directory()
        elif choice == '2':
            create_directory()
        elif choice == '3':
            delete_directory()
        elif choice == '4':
            list_files()
        elif choice == '5':
            copy_file()
        elif choice == '6':
            move_file()
        elif choice == '7':
            rename_file_or_directory()
        elif choice == '8':
            get_file_status()
        elif choice == '9':
            is_file_or_directory()
        elif choice == '10':
            get_environment_variables()
        elif choice == '11':
            remove_file()
        elif choice == '12':
            change_directory()
        elif choice == '13':
            get_current_user()
        elif choice == '14':
            list_files_recursively()
        elif choice == '15':
            check_disk_usage()
        elif choice == '16':
            create_temp_file()
        elif choice == '17':
            get_parent_directory()
        elif choice == '18':
            list_files_with_extension()
        elif choice == '19':
            get_file_permissions()
        elif choice == '20':
            create_and_write_file()
        elif choice == '21':
            read_from_file()
        elif choice == '22':
            list_subdirectories()
        elif choice == '23':
            check_file_exists()
        elif choice == '24':
            change_file_permissions()
        elif choice == '25':
            list_processes()
        elif choice == '26':
            get_file_path()
        elif choice == '0':
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main_menu()