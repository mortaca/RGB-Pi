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
3.Yes, it is possible to use it on any system supported by RPI, but attention! You will not have the original resolutions provided by our software for each game, you will see everything through a fixed resolution.
If you want to do it anyway you have the instructions [here](https://github.com/mortaca/RGB-Pi/blob/master/README.md)
4.We are limited by the pace of development of the Recalbox team, they have not yet released version 4.1 and are in Alpha phase, so we have to be Alpha phase also until they release the Beta version.
5.By the same fact of the previous point, being an Alpha of Recalbox 4.1 does not have the system called NOOBS of self-installation of the operating system so that it is in 8GB image format and we have to use the same system until the launch of the Beta where all this will not be necessary.
There are two options to solve this:
 5.1 Expand the partition / sahare of the SD, this is easier to do a Linux or Mac with the program GParted, there are also those who use the RPi itself installing Raspbian and putting the SD to expand into a USB reader.
You will find many tutorials on how to expand a partition in google, here I leave one example but there are many more.
