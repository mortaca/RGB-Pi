# RGB-Pi

Download the image from [rgb-pi.com](http://RGB-Pi.com)

------------------------------------------------------------------------------

To use the cable in Retropie, Raspbian or any other system you can insert those lines into the `config.txt` file.

Warning, this mode only supports a single resolution. **Multiple resolutions are only supported in RGB-Pi OS**

```
dtparam=audio=on
dtoverlay=pwm-2chan,pin=18,func=2,pin2=19,func2=2
dtoverlay=rgb-pi
enable_dpi_lcd=1
display_default_lcd=1
dpi_output_format=6
dpi_group=2
dpi_mode=87
hdmi_timings=320 1 16 30 34 240 1 2 3 22 0 0 0 60 0 6400000 1
```

And add the file `/overlays/rgb-pi.dtbo` from the repo .dtbo if your OS is 4.1 or .dtb for 4.0
