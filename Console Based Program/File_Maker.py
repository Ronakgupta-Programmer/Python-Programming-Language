import os
def create_file():
    filename = input("Enter the name of the file to create: ")
    if not os.path.exists(filename):
        open(filename, 'w').close()
        print(f"File'{filename}'create successfully.")
    else:
        print(f"File'{filename}' already exists.")


create_file()