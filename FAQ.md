# Frequently Asked Questions
## This FAQ is oriented to the latest available version of the system pre-alpha3, the answers here may not be useful for previous versions.

Questions:
1. Why is the cable so short?
2. Why doesn't it have a female scart?
3. Can I use the cable with Retropie or other than its mmodified version of Recalbox?
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
---------------------------------------------------------------------------------------------------
Answers:
1. The flat cable can not exceed 23cm to avoid getting interference when it is a non-insulated cable.
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
To adjust the centering we have some applications from the section Python where we can access the configuration files or if we want to do from the PC by SSH will be in the folder /share/RGB-Pi/Timings.cfg (for consoles) or / share / RGB-Pi / resolutions / (for arcade)
In these files we will find a long string separated by spaces similar to this:

megadrive 1920 240 59.92 3 4 5 48 192 240 6 15734

The fields we are interested in changing are numbers 3, 5 and 7, which may be other values or negative values.
The number 3 belongs to the horizontal centering, number 5 is horizontal zoom to expand or collapse the image and the number 7 corresponds to the vertical position.
Do not worry about expanding the image horizontally, this does not affect the perfect pixel, the important thing is not to compress or expand the vertical scanlines.

8. This is caused by a problem with the game launcher, it is solved by putting the games inside a .zip Until the problem is corrected.

9. Our system uses custom files to retroarch so any changes will be discarded, if you want to introduce a change in retroarch you can find the files we use segregated by consoles in the folder / share / RGB-Pi / Retroarch

10. 


    

