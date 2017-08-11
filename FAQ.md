# Frequently Asked Questions
## This FAQ is oriented to the latest available version of the system pre-alpha3, the answers here may not be useful for previous versions.

Questions:
1. Why is the cable so short?
2. Why doesn't it have a female scart?
3. Can I use the cable with Retropie or other than its modified version of Recalbox?
4. Why are there so many alpha versions of the software?
5. I have a SD of 16GB or 32GB but when installing the image it only recognizes 8GB or less.
6. The menu image looks distorted or black and white but the games look good.
7. In games I see a black strip or I get off the screen.
8. When putting new games sometimes they do not appear in the list.
9. I make changes in Retroarch and they can not be saved.
10. I have a RPi2 or a previous model, what system do I use?
11. Why is not Kodi available or does it look really bad?
12. How can I add new games to the system?
13. Why does Recalbox give me this problem?
14. I can connect a fan to the GPIO?
15. I can connect a power switch or the joysticks through the GPIO?
16. Why the TV channel is no selected automatically?
17. I have a question that is not on the list
---------------------------------------------------------------------------------------------------
Answers:
1. The flat cable can not exceed 25cm to avoid getting interference when it is a non-insulated cable.
If you need a longuer distance you can use a scart male-female extension, we can not ensure that the quality becomes as         high as connecting the RGB-Pi directly to the TV.

2. The use of a scart female implies the need for an additional scart cable, I liked the idea that only RGB-Pi is necessary and nothing more to work, besides I can not control what type of extensor cable each person could use and may have interference and a bad experience.

3. Yes, it is possible to use it on any system supported by RPI, but attention! You will not have the original resolutions provided by our software for each game, you will see everything through a fixed resolution.
If you want to do it anyway you have the instructions [here](https://github.com/mortaca/RGB-Pi/blob/master/README.md)

4. We are limited by the pace of development of the Recalbox team, they have not yet released version 4.1 and are in Alpha phase, so we have to be Alpha phase also until they release the Beta version.

5. By the same fact of the previous point, being an Alpha of Recalbox 4.1 does not have the system called NOOBS of self-installation of the operating system so that it is in 8GB image format and we have to use the same system until the launch of the Beta where all this will not be necessary.
There are two options to solve this:
    1. Expand the partition / sahare of the SD, this is easier to do a Linux or Mac with the program GParted, there are also those who use the RPi itself installing Raspbian and putting the SD to expand into a USB reader.
You will find many tutorials on how to expand a partition in google, [here](https://www.partitionwizard.com/resizepartition/how-to-extend-volume-of-sd-card.html) I leave one example but there are many more.
    2. Install an external USB storage, this allows you to do Recalbox from the menu, you can follow the instructions from your own [repo](https://github.com/recalbox/recalbox-os/wiki/Use-an-external-usb-storage-device-on-recalbox-%28EN%29)

6. This is because Emulationstation uses a peculiar resolution of 450x270 50Hz and on some televisions can give problems.
To solve it, just edit the file /boot/config.txt of your SD and change the first line starting with hdmi_timings.
Attention! It is important that hdmi_timings is on the first line and not another.
We have a [list of others hdmi_timings](https://github.com/mortaca/RGB-Pi/blob/master/HDMI_Timings.txt)  in the repository with which you can try until you find the right one. Make sure the symbol = is present.

7. The CRT televisions are very different from the current LCD and each TV had a slightly different centering adjustment, so there is no configuration that is good on all monitors and it is necessary that each one adjust the image to your TV, we We offer a centering solution so "NO ACCESS TO RETROARCH" is required to adjust the image.
To adjust the centering we have some applications from the section Python where we can access the configuration files or if we want to do from the PC by SSH will be in the folder /share/RGB-Pi/Timings.cfg (for consoles) or /share/RGB-Pi/resolutions/ (for arcade)
In these files we will find a long string separated by spaces like this: 
**megadrive 1920 240 59.92 3 4 5 48 192 240 6 15734** The fields we are interested in changing are numbers 3, 5 and 7, which may be other values or negative values.
The number 3 belongs to the horizontal centering, number 5 is horizontal zoom to expand or collapse the image and the number 7 corresponds to the vertical position.
Do not worry about expanding the image horizontally, this does not affect the perfect pixel, the important thing is not to compress or expand the vertical scanlines.

8. This is caused by a problem with the game launcher, it is solved by putting the games inside a .zip Until the problem is corrected.

9. Our system uses custom files to retroarch so any changes will be discarded, if you want to introduce a change in retroarch you can find the files we use segregated by consoles in the folder /share/RGB-Pi/Retroarch

10. Currently the news are only available for the RPi3, if you have a previous model you must use version 4.0 Beta3 that you can download on the web, but it is a very primitive version, in a short time we will launch all the news for all the models as soon as we have list A stable version of 4.1

11. Still we can not get an interlaced mode and to display Kodi in necessary 640x480i resolution, a lower resolution makes it totally unusable, at the time that it is possible to use it with an acceptable quality we will support it.

12. We can solve problems related to our adaptation of Recalbox to CRT monitors but the questions related to the proper functioning of Recalbox is necessary that you go to your forums and to your documentation, you will find much more documentation, tutorials and support in the [official Recalbox forums.](https://forum.recalbox.com/)

13. A bit the same as in the previous answer, everything that is not related to the adaptation of Recalbox to CRT monitors and our modifications can be consulted in the own [FAQ of Recalbox.](https://www.recalbox.com/faq)

14. Many people use a fan connected to + 5v and GND in the GPIO, the RGB-Pi connector occupies these pins but does not use it, it is possible to solder a cable from the bottom if you have knowledge of welding, another option is to pick the + 5v from the USB port using a cut cable.

15. It is not possible to connect a switch to power the RPi or any joystick to the GPIO port while the RGB-Pi is connected since almost all the pins are used to take out the necessary 18 Bits of video and sound.

16. In order for the TV to be automatically set to RGB mode, it is necessary to supply +12V to the scart and the RPi can only supply +5v which would activate the 16/9 mode and it is necessary to use the remote control to switch to 4/3.
There are those who have made modifications in their cable to introduce +12v in pin 8 of the scart, this is possible to do it through an external power supply or with the use of a step up that takes +5v of the flat cable and make it +12v, **these modifications can be made at your own risk.**
In case of wanting to do it it is not necessary to lift pin 8 of the PCB since it is not connected to ground, and it is designed thus for possible modifications.

17. Please contact us at **info@rgb-pi.com** or in the forums where we participate.


    

