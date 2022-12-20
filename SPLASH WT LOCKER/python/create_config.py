import os
import os.path
import shutil
import subprocess
from pathlib import Path


def path_header():
    print("====================\n\tChecking for path file...")
    if not os.path.isfile("config_files/path.config"):
        levels_path = path_config()
        return levels_path
    print("ERROR>>\nYou already have a path config file.\nPlease edit the existing banned_maps.config file\n>>\tconfig_files/path.config\n====================\n\n")
def path_config():
    file = "config_files/path.config"
    levels_path = input("Please enter the path to the levels folder\nFor Example - C:\SteamLibrary\steamapps\common\War Thunder\levels\n>>")
    print("Creating path file...")
    with open(file, "w") as f:
        f.write(levels_path)
    print("Success! path.config has been created in the config_files folder.\n====================\n\n")
    return levels_path

def maps_header(levels_path):
    print("====================\n\tChecking for banned maps file...")
    if not os.path.isfile("config_files/banned_maps.config"):
        maps_config(levels_path)
        return
    print("ERROR>>\nYou already have a banned maps config file.\nPlease edit the existing banned_maps.config file\n>>\tconfig_files/banned_maps.config\n====================\n\n")
def maps_config(path, layer=0):
    print("Writing filenames to banned_maps.config...")
    file = "config_files/banned_maps.config"
    with open(file, "w") as f:
        f.write("")
    path=Path(path)
    for p in path.iterdir():
        if p.is_file():
            with open(file, "a") as f:
                f.write(p.name + "\n")
        elif p.is_dir():
            print('\t'*layer, p.name+'/')
            iter_subtree(p, layer+1)
        else:
            raise FileNotFoundError()
    print("Success! banned_maps.config has been created in the config_files folder.\n====================\n\n")

def handler():
    print("SPLASH LOCKER BY ATMOIST")
    if not os.path.exists("config_files/"):
        os.mkdir("config_files/")
    levels_path = path_header()
    maps_header(levels_path)


handler()