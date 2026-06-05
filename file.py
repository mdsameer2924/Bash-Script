import os
import subprocess
import time

def main():
    file_name = input("Enter the file name to check: ")

    if os.path.isfile(file_name):
        print("file is exist")
        time.sleep(2)
        with open(file_name, 'r') as f:
            print(f.read())
    else:
        print("file is not exist")
        time.sleep(2)
        with open(file_name, 'w') as f:
            f.write("#!/bin/bash\n")
        print("file created successfully")
        print("file is opening...")
        time.sleep(3)
        with open(file_name, 'r') as f:
            print(f.read())

    print()
    # Check if file is executable
    if not os.access(file_name, os.X_OK):
        choice = input("Would you like to make it executable [Y/n]: ")
        if choice.lower() == 'y':
            print(f"{file_name} becoming executable ..")
            # Equivalent to calling your 'exe' function
            os.chmod(file_name, 0o755)
        else:
            print("Cancel to executable")

    print()
    choose = input("Would you like to edit this file [Y/n]: ")
    if choose.lower() == 'y':
        # Equivalent to calling your 'open' function
        # Using 'vim' as a placeholder for your 'open_vim.sh' script
        subprocess.run(['vim', file_name])
    else:
        time.sleep(1)
        print("script complete!")

if __name__ == "__main__":
    main()
