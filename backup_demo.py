#!/usr/bin/env python3
import os
import shutil
import datetime

# Demo configuration using test directories
source_dir = "/home/osarugue-enehizena/Documents/code-projects/projects/pythonAutomation/automation-projects/test_source"
destination_dir = "/home/osarugue-enehizena/Documents/code-projects/projects/pythonAutomation/automation-projects/test_destination"

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
            shutil.rmtree(dest_dir)  # Remove existing backup for demo
            
        shutil.copytree(source, dest_dir)
        print(f"Folder successfully copied to: {dest_dir}")
        return True
    except Exception as e:
        print(f"Error occurred during backup: {e}")
        return False

def main():
    print("=== Backup Tool Demo ===")
    print(f"Source: {source_dir}")
    print(f"Destination: {destination_dir}")
    print()
    
    # Show source contents
    print("Source directory contents:")
    for root, dirs, files in os.walk(source_dir):
        level = root.replace(source_dir, '').count(os.sep)
        indent = ' ' * 2 * level
        print(f"{indent}{os.path.basename(root)}/")
        subindent = ' ' * 2 * (level + 1)
        for file in files:
            print(f"{subindent}{file}")
    
    print("\nStarting backup...")
    success = copy_folder_to_directory(source_dir, destination_dir)
    
    if success:
        print("\nBackup completed! Destination contents:")
        for root, dirs, files in os.walk(destination_dir):
            level = root.replace(destination_dir, '').count(os.sep)
            indent = ' ' * 2 * level
            print(f"{indent}{os.path.basename(root)}/")
            subindent = ' ' * 2 * (level + 1)
            for file in files:
                print(f"{subindent}{file}")

if __name__ == "__main__":
    main()
