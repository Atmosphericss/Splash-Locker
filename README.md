Feel free to check my kofi out to donate if you like any of the open source projects I'm working on. It really helps me to stay motivated, and allows me to run services like servers I otherwise wouldn't be able to
<br>
<a href='https://ko-fi.com/atmoist' target='_blank'><img height='35' style='border:5px;height:46px;' src='https://az743702.vo.msecnd.net/cdn/kofi6.png?v=22' border='1' alt='If you appreciate free releases made by me :)' />

# Thanks for using Splash Locker!

Thanks for trying out this short project. All code found within this project is open source, and available for free usage in any non-commercial way. I hope you find this program, or it's source code useful. All code was made by:

>[Atmosphericss](https://github.com/Atmosphericss/) | **Atmoist🖤⚡💛#7178**

With credits to:

>[unununu](https://github.com/unununununununun/)
For his work on creating a pascaal locker, which is where I have taken the locking mechanism from.

# Important!
### To avoid having to redownload game files every time you load the game, please make sure to use 
> unlock.bat
### BEFORE exiting out of the game.

# Usage and files...

## Finding the War Thunder /levels/ directory
  
  - Steam: Here is an example of what your path may look like if you installed the game via steam: 
  > `C:\Program Files (x86)\Steam\steamapps\common\War Thunder\levels`
  
  **Note**: Space between War and Thunder in path
  **Easy way to find**: Find War THunder within your Steam Client Library, then right click on it and navigate to *Manage>Browse Local Files*. This should open a folder that contains **/levels/**
  - Gaijin Launcher: This will be...wherever you installed it, for example mine is:
  > `D:\WarThunder\levels`
  
  **Note**: No space between War and Thunder on the official gaijin launcher installation.
   **Easy way to find**: Right click on your desktop War Thunder shortcut, and clicking on  **Open file location**. In the folder you are taken to, should be **/levels/**

## Files
|                |.py                          |Description                         |
|----------------|-------------------------------|-----------------------------|
|create_config_template.bat|`python/create_config.py`            |This runnable script file starts create_config and asks for the path to ur your War Thunder levels folder.            |
|lock.bat          |`python/lock.py`            |Locks maps left within config_files/banned_maps.config            |
|unlock.bat          |`python/unlock.py`|Unlocks all maps found within levels/bak/|

## Config
After running **create_config_template.bat**, the **config_files** directory will be created, with **path.config** & **banned_maps.config** found inside.
>`path.config` - This file holds the full path of the war thunder levels folder, as request within create_config_template.

>`banned_maps.config` - This file dictates the files that will become locked after running the lock file. *IMPORTANT* Learn more about this file, and what it should contain in the banned maps section below *IMPORTANT*

## Usage
### First steps

**Please DO NOT FORGET TO EDIT banned_maps.config**

- Run `create_config_template.bat` - This will generate a folder with config files within. These config files can be changed any time

- Editing `banned_maps.config` & `path.config` - These are very important files and **SHOULD** be changed before running the lock function - **banned_maps.config** is generated containing *every* map.bin file in the game included. Running lock with this config will cause every match to be ended early. Instead, use this file to find the maps you wish to ban. **path.config** is generated with the path given to **create_config_template.bat**, and should only really be changed if you decide to change or move the warthunder/levels directory

### Next

Once you are happy with the config files you prepared, you should be safe to use `lock.bat` & `unlock.bat`.

- Running `lock.bat` - Running this script will "lock", the War Thunder binary files found in **banned_maps.config**. This will still allow for War Thunder to *attempt* to access the bin file, but causing them to fail. Backups of every "locked" mapfile are stored in a */bak/* directory until unlock.bat is run.

- Running `unlock.bat` - Unluck **MUST** be run before closing the War Thunder game to avoid having to reinstall the missing files on your next launch. It copies the backups, from */bak/*, back into the levels directory, overwriting the "locked" files.

## How it works...
`lock.bat` writes a special byte to the start of the "banned" maps. This causes the maps to crash before loading in game, while also not taking ur SL, or banning you from vehicles (normal effects of leaving). Effectively, this program allows you to have unlimited map bans.
#### Please do note the following points however:
- Playing with this in a squad will cause you to be kicked, as per normal, and your squad to continue into the game. In short, you either all need to use this locker (or other similar ones), or none in order to play together.
- Though I nor anyone I know has been banned using this form of "mod". It is definitely one of the more aggressive and invasive types of mod that are not outright cheating. -- HOWEVER after the release of Arctic and getting it too many times recently, I am releasing this program, I refuse to play that map again.



# Licensing!
## GNU General Public License

This Project is protected under the above license. This can be observed in full, in **COPYING.txt** with the source code.
