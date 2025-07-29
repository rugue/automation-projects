import os
import shutil
import datetime
import schedule
import time

# Updated paths for Linux - change these to your actual directories
source_dir = "/home/osarugue-enehizena/Pictures"  # or any source directory you want to backup
destination_dir = "/home/osarugue-enehizena/Documents/Backups"  # backup destination

def copy_folder_to_directory(source, dest):
    today = datetime.date.today()
    dest_dir = os.path.join(dest, str(today))
    
    try:
        shutil.copytree(source, dest_dir)
        print(f"Folder copied to: {dest_dir}")
    except FileExistsError:
        print(f"Folder already exists in: {dest}")


schedule.every().day.at("18:57").do(lambda: copy_folder_to_directory(source_dir, destination_dir))

while True:
    schedule.run_pending()
    time.sleep(60)