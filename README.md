# Thanks for using Splash Locker!

Thanks for trying out this short project. All code found within this project is open source, and available for free usage in any non-commercial way. All code was made by:

>**Atmoist🖤⚡💛#7178**

With credits to:

>[unununu](https://github.com/unununununununun/)
For his work on creating a pascaal locker, which is where I have taken the locking mechanism from.

# Important!
### To avoid having to redownload game files every time you load the game, please make sure to use 
> unlock.bat
### BEFORE exiting out of the game.

# Usage and files...

## Finding the War Thunder /levels/ directory

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