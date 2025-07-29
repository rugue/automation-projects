#!/usr/bin/env python3
import os
import shutil
import datetime

# Configure your source and destination directories
source_dir = "/home/osarugue-enehizena/Pictures"  # Change this to your source directory
destination_dir = "/home/osarugue-enehizena/Documents/Backups"  # Change this to your backup destination

def copy_folder_to_directory(source, dest):
    """
    Copy a folder to a destination directory with today's date as folder name
    """
    today = datetime.date.today()
    dest_dir = os.path.join(dest, str(today))
    
    # Check if source directory exists
    if not os.path.exists(source):
        print(f"Error: Source directory '{source}' does not exist!")
        return False
    
    # Create destination directory if it doesn't exist
    os.makedirs(dest, exist_ok=True)
    
    try:
        if os.path.exists(dest_dir):
            print(f"Backup for {today} already exists in: {dest_dir}")
            # You can choose to overwrite or skip
            user_input = input("Do you want to overwrite? (y/n): ").lower()
            if user_input == 'y':
                shutil.rmtree(dest_dir)  # Remove existing backup
                shutil.copytree(source, dest_dir)
                print(f"Folder overwritten and copied to: {dest_dir}")
            else:
                print("Backup skipped.")
                return False
        else:
            shutil.copytree(source, dest_dir)
            print(f"Folder successfully copied to: {dest_dir}")
        return True
    except PermissionError:
        print(f"Error: Permission denied. Cannot access '{source}' or '{dest}'")
        return False
    except Exception as e:
        print(f"Error occurred during backup: {e}")
        return False

def main():
    print("=== Backup Tool ===")
    print(f"Source: {source_dir}")
    print(f"Destination: {destination_dir}")
    print()
    
    # Check if directories exist
    if not os.path.exists(source_dir):
        print(f"Warning: Source directory '{source_dir}' does not exist!")
        print("Please update the source_dir variable in the script.")
        return
    
    # Ask user if they want to proceed
    proceed = input("Do you want to start the backup? (y/n): ").lower()
    if proceed == 'y':
        success = copy_folder_to_directory(source_dir, destination_dir)
        if success:
            print("Backup completed successfully!")
        else:
            print("Backup failed!")
    else:
        print("Backup cancelled.")

if __name__ == "__main__":
    main()
