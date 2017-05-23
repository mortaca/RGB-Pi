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
