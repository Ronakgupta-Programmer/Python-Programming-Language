import sys

def sys_version():
    print("\nPython Version:")
    print(sys.version)

def command_line_arguments():
    print("\nCommand Line Arguments:")
    print("Number of arguments:", len(sys.argv))
    print("Arguments:", sys.argv)

def exit_program():
    print("\nExiting the program...")
    sys.exit()

def system_platform():
    print("\nSystem Platform:")
    print(sys.platform)

def maximum_integer():
    print("\nMaximum Integer Value:")
    print(sys.maxsize)

def stdio_streams():
    print("\nStandard Input, Output, and Error Streams:")
    print("Standard Input:", sys.stdin)
    print("Standard Output:", sys.stdout)
    print("Standard Error:", sys.stderr)

def check_executable():
    print("\nPython Executable Location:")
    print(sys.executable)

def check_version_info():
    print("\nVersion Info:")
    print(sys.version_info)

def path_info():
    print("\nPython Path Information:")
    print("System Path:", sys.path)

def set_recursion_limit():
    current_limit = sys.getrecursionlimit()
    print(f"\nCurrent Recursion Limit: {current_limit}")
    
    new_limit = int(input("Enter a new recursion limit (current is {}): ".format(current_limit)))
    sys.setrecursionlimit(new_limit)
    print("New Recursion Limit:", sys.getrecursionlimit())

def check_bytes_writable():
    print("\nIs Standard Output Writable?")
    print("Writable:", sys.stdout.writable())

def check_io_encoding():
    print("\nStandard Input and Output Encoding:")
    print("Input Encoding:", sys.stdin.encoding)
    print("Output Encoding:", sys.stdout.encoding)

def check_api_version():
    print("\nAPI Version:")
    print("API Version:", sys.api_version)

def get_file_descriptor():
    print("\nFile Descriptors:")
    print("Standard Input File Descriptor:", sys.stdin.fileno())
    print("Standard Output File Descriptor:", sys.stdout.fileno())
    print("Standard Error File Descriptor:", sys.stderr.fileno())

def get_sys_modules():
    print("\nLoaded Modules:")
    print(sys.modules.keys())

def get_current_frame():
    print("\nCurrent Frame:")
    frame = sys._getframe()
    print("Frame Info:", frame)

def get_recursion_limit():
    print("\nRecursion Limit:")
    print("Current Recursion Limit:", sys.getrecursionlimit())

def get_base_executable():
    print("\nBase Executable Path:")
    print("Base Executable:", sys.base_exec_prefix)

def get_prefixes():
    print("\nPython Installation Prefixes:")
    print("Prefix:", sys.prefix)
    print("Base Prefix:", sys.base_prefix)

def get_sys_path():
    print("\nCurrent Python Path:")
    print("\n".join(sys.path))

def get_stdout_isatty():
    print("\nIs Standard Output a TTY?")
    print("Is TTY:", sys.stdout.isatty())

def check_unraisable_hook():
    print("\nUnraisable Hook:")
    print("Unraisable Hook Function:", sys.unraisablehook)

def set_unraisable_hook():
    def custom_unraisable_hook(exc_type, exc_value, exc_tb):
        print("Unraisable exception caught!")
        print("Type:", exc_type)
        print("Value:", exc_value)

    sys.unraisablehook = custom_unraisable_hook
    print("Custom unraisable hook set.")

def main():
    while True:
        print("\nChoose an option:")
        print("1. Display Python Version")
        print("2. Display Command Line Arguments")
        print("3. Display System Platform")
        print("4. Display Maximum Integer Value")
        print("5. Display Standard Input/Output/Error Streams")
        print("6. Display Python Executable Location")
        print("7. Display Version Info")
        print("8. Display Python Path Information")
        print("9. Set Recursion Limit")
        print("10. Check if Standard Output is Writable")
        print("11. Check Standard Input/Output Encoding")
        print("12. Display API Version")
        print("13. Display File Descriptors")
        print("14. Display Loaded Modules")
        print("15. Display Current Frame Info")
        print("16. Get Recursion Limit")
        print("17. Display Base Executable Path")
        print("18. Display Python Installation Prefixes")
        print("19. Display Current Python Path")
        print("20. Check if Standard Output is a TTY")
        print("21. Check Unraisable Hook")
        print("22. Set Unraisable Hook")
        print("23. Exit")
        
        choice = input("Enter your choice (1-23): ")

        if choice == '1':
            sys_version()
        elif choice == '2':
            command_line_arguments()
        elif choice == '3':
            system_platform()
        elif choice == '4':
            maximum_integer()
        elif choice == '5':
            stdio_streams()
        elif choice == '6':
            check_executable()
        elif choice == '7':
            check_version_info()
        elif choice == '8':
            path_info()
        elif choice == '9':
            set_recursion_limit()
        elif choice == '10':
            check_bytes_writable()
        elif choice == '11':
            check_io_encoding()
        elif choice == '12':
            check_api_version()
        elif choice == '13':
            get_file_descriptor()
        elif choice == '14':
            get_sys_modules()
        elif choice == '15':
            get_current_frame()
        elif choice == '16':
            get_recursion_limit()
        elif choice == '17':
            get_base_executable()
        elif choice == '18':
            get_prefixes()
        elif choice == '19':
            get_sys_path()
        elif choice == '20':
            get_stdout_isatty()
        elif choice == '21':
            check_unraisable_hook()
        elif choice == '22':
            set_unraisable_hook()
        elif choice == '23':
            exit_program()
        else:
            print("Invalid choice! Please choose a number between 1 and 23.")

if __name__ == "__main__":
    main()