# lol-for-linux-installer

League of Legends unofficial installer/manager for linux

This software is not affiliated with nor supported by Riot Games.

![Screenshot_20230415_205958](https://user-images.githubusercontent.com/40970965/232259098-0e51d868-cfb8-4312-aab4-6e84728c5f24.png)
![Screenshot_20230512_212003](https://github.com/kassindornelles/lol-for-linux-installer/assets/40970965/1fdd188a-8af5-4401-8b0c-f66a8ff82ff0)

## How to use it (without installing)
- Check if you have all required [dependencies](#dependencies) installed first
- Download the latest release from the [Releases page](https://github.com/kassindornelles/lol-for-linux-bash-installer/releases)
- Extract the files
- Double-click 'lol-for-linux-installer.py' and install the game or manage your already existent install.

## Arch Linux based distributions installation:
- In the folder where the `PKGBUILD`file is located run `makepkg -si` in a terminal.

### Python Script features:
- You can choose where to install the game and also the region you are going to play
- It installs wine-ge-lol with FSYNC/FUTEX2 support enabled by default for better CPU performance
- It creates a desktop file in the system menu (with icons for the game)
- Option to uninstall the game
- Users of hybrid graphics can choose at install time if they want to use the dGPU or not
- obs-gamecapture support.
- Update system for WINE builds, DXVK version selection and more (DXVK installation via our launcher)
- Gamemode support, if installed system wide it will be used automatically.

## <a name="dependencies"></a> Dependencies (install those packages system-wide first):
- `tar`, `python`, `python-requests`, `python-psutil`, `qt5-base` and `pyqt5`

   On ubuntu-based distributions the python packages are called "python3-psutil, python3-requests and python3-pyqt5"
   
- WINE 32-64 bits and its [Dependency hell](https://www.gloriouseggroll.tv/how-to-get-out-of-wine-dependency-hell/)

## Remaining tasks:
- Flatpak package

## Buy me a coffee

<a href="https://www.paypal.com/donate/?hosted_button_id=UMJWYGDH2RC7E"><img src="https://github.com/andreostrovsky/donate-with-paypal/blob/master/grey.svg" alt="Donate with PayPal" width="150" height="40"></a>

