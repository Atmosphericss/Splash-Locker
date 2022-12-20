import os
import os.path
import shutil
import subprocess
from pathlib import Path
def lock_file(map, levels_path):
    target = "%s/%s" % (levels_path, map)
    print(target)
    with open(target, 'r+b') as f:
        bytes = f.read(1)
        lock_char = b'\xff'
        f.seek(0)
        f.write(lock_char)
def per_file_operations(bak_path, ban_list, levels_path):
    for map in ban_list:
        map = map.replace("\n", "")
        print(f"Locking {map}...")
        shutil.copyfile(f"{levels_path}/{map}", f"{bak_path}{map}")
        lock_file(map, levels_path)
def read_ban_list():
    with open("config_files/banned_maps.config", "r") as f:
            return f.readlines()
def create_bak(levels_path):
    bak_path = levels_path + "/bak/"
    try:
        os.mkdir(bak_path)
        return bak_path
    except FileExistsError:
        print("ERROR>>\nYou already have a bak folder in your levels folder.\nTo remove and restore files from the bak directory, run\n>>unlock.bat\n")
        exit()
def get_path():
    with open("config_files/path.config", "r") as f:
        path = f.read()
    return path
def config_check():
    if not os.path.isfile("config_files/path.config"):
        print("ERROR>>\nYou do not have a path config file.\nPlease create a path file using\n>>create_config_template.bat\n")
        return False
    if not os.path.isfile("config_files/banned_maps.config"):
        print("ERROR>>\nYou do not have a banned maps config file.\nPlease create a banned maps config file using\n>>create_config_template.bat\n")
        return False
    return True
def init_lock():
    print("SPLASH LOCKER BY ATMOIST")
    if not config_check():
        return
    print("====================\nPath and banned maps config files found!")
    levels_path = get_path()
    bak_path = create_bak(levels_path)
    ban_list = read_ban_list()
    per_file_operations(bak_path, ban_list, levels_path)
    print("\n====================\nAll maps locked!\n====================\n")

init_lock()