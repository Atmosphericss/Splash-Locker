import os
import os.path
import shutil
import subprocess
from pathlib import Path
def cleanup(levels_path):
    bak_path = levels_path + "/bak/"
    shutil.rmtree(bak_path)
def overwrite_locked(bak_path, levels_path):
    locked_files = os.listdir(bak_path)
    for file in locked_files:
        bak_file = f"{bak_path}/{file}"
        shutil.copy2(bak_file, levels_path)
def bak_exists(levels_path):
    if not os.path.isdir(levels_path + "/bak/"):
        print("ERROR>>\nYou do not have a backup folder.\nPlease run the lock script first.\n")
        return False
    return True
def get_path():
    with open("config_files/path.config", "r") as f:
        path = f.read()
    return path
def config_exists():
    if not os.path.isfile("config_files/path.config"):
            print("ERROR>>\nYou do not have a path config file.\nPlease create a path file using\n>>create_config_template.bat\n")
            return False
    return True
def init_unlock():
    print("SPLASH LOCKER BY ATMOIST")
    if not config_exists():
        return
    levels_path = get_path()
    print("====================\nPath config file found!")
    if not bak_exists(levels_path):
        return print("\n====================")
    print("Backup folder found!")
    bak_path = levels_path + "/bak/"
    print("Unlocking maps...")
    overwrite_locked(bak_path, levels_path)
    print("Removing levels backup folder...")
    cleanup(levels_path)
    print("\n====================\nAll maps unlocked!\n====================\n")

init_unlock()