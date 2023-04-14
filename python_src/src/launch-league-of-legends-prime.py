#!/usr/bin/env python3
import os
import subprocess

# Get the current working directory
cwd = os.getcwd()

# Set up the file paths relative to the current working directory
game_main_dir = os.path.join(cwd)
game_main_wine_dir = os.path.join(game_main_dir, 'wine')
game_prefix_dir = os.path.join(game_main_wine_dir, 'prefix')
game_exe_path = os.path.join(game_prefix_dir, 'drive_c', 'Riot Games', 'Riot Client')
game_exe_file_name = 'RiotClientServices.exe'
wine_loader_path = os.path.join(game_main_wine_dir, 'wine-build', 'bin', 'wine')

# Set up the environment variables
start_game_vars = dict(os.environ,
       PATH=os.path.join(game_main_wine_dir, 'wine-build', 'bin'),
       WINEPREFIX=game_prefix_dir,
       WINELOADER=wine_loader_path,
       DRI_PRIME="1",
       WINEESYNC="1".
       WINEFSYNC="1",
       WINEDEBUG="-all",
       WINEDLLOVERRIDES="winemenubuilder.exe=d",
    )

wine_process = ["wine", os.path.join(game_exe_path, game_exe_file_name), "--launch-product=league_of_legends", "--launch-patchline=live"]
subprocess.run(wine_process, env=start_game_vars, check=True)

