RGB-Pi 4.1 Final 1.1 for RPi3 - Comingsoon :

    x New ARCADE "Encapsulator" to force games with vertical overscan or underscan
    x Horizontal overscan fixed on arcade games of more than 320 for example CPS games.
    - ScummVM direct link to the games fixed without launcher
    - ScummVM with TrinitronFIX available
    - C64 issue on "Forest & Flat" themes solved
    - Test pattern on TATE mode fixed
    x Tearing on the left side on TATE mode
    x Credits section with easter egg
    - solved issue with interlaced games on AdvMAME
    - fixed little bugs on the game list
    - Items ordered in Config list

RGB-Pi 4.1 Final for RPi3 - 18/05/2018 :

    - System updated to Recalbox 4.1 Final 17.12.02 release
    - Self expansion of the file system on first boot
    - Bug showing red color on Trinitron TV's fixed with TRINITRON FIX script
    - Added ScummVM at 240p resolution
    - USB Mount now mount /roms /bios & /saves folders
    - Custom homebrew welcome selection by Javier
    - Bug to run games inside advancemame folders fixed
    - Multitap on snes emulator disabled
    - Corrected proportion of the logos on themes
    - New vertical themes function auto rotables
    - Two new themes included "Forest & Flat" (Logos proportioned & auto rotables)
    - New function hide all the horizontal systems on rotated mode automatically
    - Amiga homebrew demo by Ironic
    - Original cable use verification system
    - New skins for the frequency selector availables
    - New RGB test screen with color bars
    - Joystick checking on FF_selector & SU

RGB-Pi 4.1 Alpha 3.2 for Rpi3 - 22/11/2017 :

    - USBMount modified to preserve the Config folder
    - 32x 50Hz vertical resolution fixed
    - Replaced modes 450 & 320 from SU by 270 & 240 with 450 H lines without overscan
    - Delay on FF_Selector fixed
    - Aggregation of favorites with one button fixed
    - Framebuffer upgraded from 16 to 18 Bits of color (best image quality in 32/64Bits games)
    - New emulators added: Commodore64
    - New emulator added: AdvanceMAME (romset 0.106) less input lag & best rotation
    - New bezels for handheld availables from ScreenUtility instead stretching mode
    - Auto rotation of directional axis for TATE games in horizontal mode
    - Changed aspect ratio of TATE games rotated -90º from fullscreen to cropped
    - Some black invisible logos fixed in theme detailed list
    - New message when arcade game is not in database and launch it in standar resolution

RGB-Pi 4.1 Alpha 3.1 for Rpi3 - 18/09/2017 :

    - Added FDS,WS,WSC & NGP
    - Compatibility for all joysticks in SU & FF Selector
    - Fixed bugs in SU with test, rotating system & resolution change.
    - Fixed bug exiting from MD
    - Added script IndividualEditor to edit Timings.cfg
    - Added /bios folder to USBMount script
    - Changed folder /python by /config inside /roms
    - Changed logos of PCE & CD-ROM2

RGB-Pi 4.1 Alpha 3 for Rpi3 - 27/08/2017 :

    - Total Recalbox systems added, minus WonderSwan, Game&Watch and FDS
    - New aplication ScreenUtility to manage screen options from TV
    - Script to mount USB storages
    - New frequency selector
    - New theme and custom intro
    
RGB-Pi 4.1 Alpha 2 for Rpi3 - 23/05/2017 :

    - New systems added; segacd, sega32x, atari2600, gba, gbc, gb, gamegear, ngp, pcenginecd.
    - Solved issue with USB storage mount.
    - JoyPad remaping with; select=hotkey, exit=select+start, retroarch menu=select+L

RGB-Pi 4.1 Alpha for Rpi3 - 14/05/2017 :

    - Image compiled only for RaspberryPi3 and 4GB SD expandible.
    - Build based on Recalbox 4.1.
    - Resolution database to select the correct refresh rate and H, V lines for each rom.
    - Script autogenerator of hdmi_timings on the fly with centering, refresh and resolution values.
    - Segregated consoles by 50 or 60 Hz.
    - Segregated arcade games by horizontal (yoko) or vertical (tate) orientation.
    - Theme modified to view big pictures in scraping mode, new icons and new black theme.
    
RGB-Pi 4.0 Beta 3 - 22/01/2017 :

    - Fixed bugs in GameList, Ugly fonts and more space to the name of the game.
    - New aspect ratio selection method, unlocking fixed resolution for every machine to autoselect the own resolution of every       rom in 1:1 pixel aspect ratio, this get pixel perfect for all roms with the main resolution os the machine is knowed like       NeoGeo, now the system recognices betwin 304x240 and 320x240 games and avoid the tearing.

RGB-Pi 4.0 Beta 2 - 19/01/2017 :

    - Recovery and frontend resolutions changed from 320x240 to 480x300 greatly improving the appearance.
    - Solved issues with PSX and N64 resolutions, psx 320x240 and N64 down scaled from 640x480 to 480x300 until we get               interlaced modes.

RGB-Pi 4.0 Beta Firts launch - 12/01/2017 :

    - NOOBS from Recalbox substituided by PINN to view installation progress and recovery mode from CRT, PINN also solved             powerup issues with attached devices to the GPIO.
    - RPi firmaware update to allow resolutions to change on the fly.
    - Udated Recalbox configgen code to get different resolutions for every system from recalbox.conf.
    - Generate custom files .cfg for every machine to set the correct aspect ratio of the games and others custom options.
    - Recompile PINN to add RGB-Pi logo at start, and added logo to the splash screen on Recalbox.
