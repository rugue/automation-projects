#!/usr/bin/env python3
"""
Simple Backup Script - Manual Version
Run this to perform a one-time backup without scheduling
"""

import os
import shutil
import datetime

def backup_folder(source_dir, destination_dir):
    """Backup a folder with today's date"""
    
    # Get today's date for folder naming
    today = datetime.date.today()
    backup_folder_name = str(today)
    dest_path = os.path.join(destination_dir, backup_folder_name)
    
    print(f"Starting backup...")
    print(f"Source: {source_dir}")
    print(f"Destination: {dest_path}")
    
    # Check if source exists
    if not os.path.exists(source_dir):
        print(f"❌ Error: Source directory '{source_dir}' does not exist!")
        return False
    
    # Create destination directory if needed
    os.makedirs(destination_dir, exist_ok=True)
    
    try:
        # Check if backup already exists
        if os.path.exists(dest_path):
            print(f"⚠️  Backup for {today} already exists!")
            choice = input("Overwrite existing backup? (y/n): ")
            if choice.lower() != 'y':
                print("Backup cancelled.")
                return False
            shutil.rmtree(dest_path)
        
        # Perform the backup
        shutil.copytree(source_dir, dest_path)
        print(f"✅ Backup completed successfully!")
        print(f"📁 Backup saved to: {dest_path}")
        
        # Show backup size
        total_size = sum(os.path.getsize(os.path.join(dirpath, filename))
                        for dirpath, dirnames, filenames in os.walk(dest_path)
                        for filename in filenames)
        print(f"📊 Backup size: {total_size / (1024*1024):.2f} MB")
        
        return True
        
    except PermissionError:
        print(f"❌ Permission error: Cannot access source or destination")
        return False
    except Exception as e:
        print(f"❌ Error during backup: {e}")
        return False

if __name__ == "__main__":
    # 🔧 CONFIGURE THESE PATHS FOR YOUR SYSTEM:
    SOURCE_DIR = "/home/osarugue-enehizena/Pictures"  # Change this!
    DEST_DIR = "/home/osarugue-enehizena/Documents/Backups"  # Change this!
    
    print("=" * 50)
    print("🔄 BACKUP TOOL")
    print("=" * 50)
    
    backup_folder(SOURCE_DIR, DEST_DIR)
