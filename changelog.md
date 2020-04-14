**RGB-Pi OS 2 (Alpha - 20200501) Soon**
```
- Added default OS turbo mode for improved performance.
- Changed to native video driver for improved frame latency.
- Changed to latest retroarch + core updates.
- Added experimental Sharp x68000.
- Changed FB Alpha by FB Neo.
- Added NEOGEO CD system.
- Changed system menu and system options interface.
- Added full CW and CCW UI rotation modes. 
- Added new Skin UI engine.
- Added new unified search + scrap engine.
- Added support for video previews.
- Changed game list and favorite data are now saved per unit.
- Added new game list options menu.
- Added quick sort modes by letter, year, players and system.
- Added forward and backward for all the quick search modes.
- Added Virtual Keyboard for data entry.
- Added Kiosk mode password protected. 
- Added 5 new languages (EN,ES,FR,DE,IT,PT,JP).
- Added display menu music title.
- Added rom folder auto-regeneration.
- Added NFS2/3 and NFS4 modes.
- Added NFS check to avoid overwrite hi-scores.
- Added current selected external unit icon.
- Added three new screen savers, black screen, video previews and CRT power off.
- Added Image List menu type.
- Added system power and temperature alarms.
- Added arcade FreePlay mode.
- Added controller and button layout association. 
- Fixed some firewall blocking issues.
- Fixed SSID and Password char issues.
- Fixed all remaps on real RGB-Pi JAMMA mode.
- Changed unified Start hotkey for solving issues with PC-Engine, MegaDrive and JAMMA.
- Changed main music to Evan King chiptune albums.
- Added new custom music album option.
- Added new Bluetooth menu.
- Added new Netplay menu.
- Added new External Unit menu.
- Changed all RetroArch options to specific menus.
- Changed EQ menu.
- Changed controller mapping by direct selection.
- Added new manual power off option.
- Added power off sequence image indicators.
- Removed auto scan games on boot for super fast load.
- Added videoplayer UI integration.
- Removed cable check restriction.
```
**RGB-Pi OS (Beta - Update) 2019 08 06**
```
- Fixed UI font. Now is fully monospace
- Fixed cls error cls on system boot
- Fixed some english translations
- Fixed performance issue in arcade image selector screen
- Fixed advmame paths for reading from the current selected unit
- Fixed vertical games overlay displayed on horizontal games
- Added apostrophe character support in Wifi configuration
- Added .hdf, .t64 and .adf as supported files (core not tested)
```
**RGB-Pi OS (Beta - Update) 2019 07 14**
```
- Changed VSync FIX from 3 to 4 (grid readjustment required)
- Fixed some Arcade games image distortion (i.e gigawing)
- Fixed DOSBox launcher and verbosity output
- Fixed Wifi firewall rules
- Fixed Remaps folder permissions
- Added help on rotating image to the left
- Increased keyrepeat response time
- Fixed Sega CD (JP) games not loading
```
**RGB-Pi OS (Beta - Image) 2019 06 30**
```
- Added game statistics information in Info screen
- Added Extras menu for special retroarch options
- Added new menu music modes and songs
- Added configuration upload option
- Added 2 speeds key repeat functionality in game lists
- Added 3s auto restore resolution on FIX option
- Added new scraper custom mode
- Added option to skip all analog buttons when mapping
- Added new gamepad sorting engine to match retroarch system
- Added quick skip to letter search functionality
- Added especial rom badges for pirate, unlicense, prototype, translated, hack, etc.
- Added new info popup in quick load functionality
- Added NAS/NFS option for reading games remotely
- Added new rules for some special gamepads
- Added country flag badges on gamelist
- Added new original/forced arcade selector
- Added filter to the game scanner to avoid displaying Linux/Mac hidden files
- Added improved file extension filter to DOSBox and ScummVM
- Added new automatic position adjustment of video intro
- Changed to new Bluetooth gamepad module. Now works properly and faster.
- Changed to new game search engine. Now is 2x faster
- Changed all UI image assets
- Changed UI hdmi_timings
- Changed/Fixed some UI texts
- Changed Netplay QR image by simple text URL
- Changed image Zoom algorithm
- Changed FIX VSync from 5 to 3 (grid readjustment required)
- Changed some buttons for screen assistant to fit with JAMMA board
- Updated help
- Updated JAMMA image
- Removed back/cancel option from screen assistant
- Removed testing BIOS folder for public Release
- Fixed lang selector on first boot for JAMMA board
- Fixed resolution change issue in the middle of video intro
- Fixed file permissions in Arcade folder
- Fixed sceen assistant not using the correct timing when FIX is active
- Fixed favorites not saving changes sometimes
- Fixed grid image proportions
- Fixed black screen happening sometimes in no-games screen
- Fixed analog sticks in retroarch mappings
- Fixed restore option to clean up gamelist and UI gamepad mapping
- Fixed 50/60Hz selector appearing in incorrect scenarios
- Fixed keyboard input on screen assistant with FIX
- Fixed virtual keyboard on Spectrum emulator
- Fixed mapping images for JAMMA/MVS/NEOGEO
- Fixed button A missing key press when returning to UI from game
- Fixed DOSBox breaking UI in some games
- Fixed some TATE games not being displayed with the correct orientation
- Fixed screen assistant to avoid displaying the screen saver
- Fixed screen position when changing zoom values
- Fixed ScummVM crashes
- Fixed bugs in countdown in arcade mode
- Fixed Arcade 240p forced mode
- Fixed centering on Arcade original mode
- Fixed centering on Arcade 256p games
- Fixed timmings on Arcade 224p games
- Fixed FIX game timmings
- Fixed Wifi connection
- Fixed shuffle menu music
- Fixed overscan of all systems
```
**RGB-Pi OS (Alpha - Image) 2019 06 22**

*Initial RGB-Pi OS Release. You can check the most important features described down below:*
```
- Custom interface specially adapted for CRT TVs
- New screen configuration assistant
- Special horizontal and vertical arcade mode visualizations
- Personalized interface button skins
- Improved sound system with equalizer engine
- Simplified bluetooth configuration system
- New simplified Netplay
- Game visualization by list or folder modes
- New SD/USB/NFS manager system
- Online system updates
- Integrated Scraper
- Integrated Help
- Soft screen rotation with no performance impact
- Updated emulators and cores
- Raspberry Pi 2B, 3B and 3B Plus support
- Video player
```
