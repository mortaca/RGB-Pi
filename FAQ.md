Available in English and Spanish / *Disponible en Ingles y Español*
# Frequently Asked Questions
## This FAQ is meant for the latest available version of the RGB-Pi OS Beta system 19_06_30s, the answers here may not be useful for previous versions.

Questions:
1. What systems are supported?
2. How can I copy a game ROMs?
3. Why is the cable so short?
4. Why doesn't it have a female scart connector?
5. I have a Sony Trinitron TV and red colors look muted.
6. Can I use the cable with Retropie, Recalbox or Lakka?
7. How can I use an external USB/NFS storage?
8. Why do some games displays black bars or are a little off the screen?
9. What romsets are used by the different arcade emulators?
10. Which RPi models are supported?
11. Can I use RGB-Pi on a LCD TV or with some upscaler?
12. Can I connect a fan to the GPIO?
13. Can I connect a power switch or joystick through the GPIO?
14. Why is the TV channel not selected automatically?
15. Vertical games are not displayed vertically, how can I fix that?
16. Handheld games look very small.
17. I don't have sound.
18. What is Netplay and how does it work?
19. Is it a good idea playing with screen bezels enabled?
20. How can I create a backup of my favorites?
21. How can I use my custom scrap images?
22. How can I save my Retroarch FBA remaps?

---------------------------------------------------------------------------------------------------

1. What systems are supported?

* Arcade Machines MAME/FBA (.zip)
* Atari 2600 (.a26 .rom)
* Atari 400/800/XL/XE/5200 (.a52 .atr .bas .car .dcm .xex .xfd)
* Atari 7800 (.a78)
* Atari LYNX (.lnx)
* WonderSwan (.ws)
* WonderSwan Color (.wsc)
* ColecoVision (.col)
* PC Engine (.pce)
* CD-ROM2 System (.ccd .chd .cue)
* Odyssey2 (.o2)
* Nintendo NES (.fds .nes)
* Famicom Disk System (.fds .nes)
* Super Nintendo (.sfc .smc)
* Nintendo 64 (.z64 .n64 .v64)
* Game Boy (.gb)
* Game Boy Color (.gbc)
* Game Boy Advance (.gba)
* SG-1000 (.sg), Master System (.sms)
* Megadrive (.gen .md .smd) 
* Mega-CD (.chd .cue)
* Megadrive 32X (.32x)
* Game Gear (.gg)
* NEOGEO AES & MVS (.zip)
* NEOGEO Pocket (.ngp)
* NEOGEO Pocket Color (.ngc)
* PlayStation (.pbp .cue .cbn .img .iso .m3u)
* Amstrad CPC (.dsk)
* Atari ST (.st .stx .ipf)
* Commodore 64 (.crt .d64)
* Commodore Amiga (.uae .adf)
* MSX (.rom .mx1 .mx2)
* ZX Spectrum (.tap .tzx)
* ScummVM (.svm)
* MS-DOS (.sh)

2. How can I copy a game ROMs?

You have several options to access to the ROMs folder:

a) In Windows, open the file browser and type `\\rgbpi` in the address bar
b) You can connect via SFTP (check the Pi's IP from `[Network]` menu) using the follwing credentials: user: `pi` / password: `rgbpi`
c) If you are on Linux, plug the SD card into your computer from rootfs partition go to `/home/pi/RetroPie/roms folder`
d) Create an external RGB-Pi USB unit using `[Settings > Load Games From > USB/NFS]`


3. Why is the cable so short?

Since the cable is unshielded, it can not exceed 25cm to avoid external interference.
If you need a longer cable, you can use a scart male to female extension cable, but the image quality will depend a lot on the cable you will choose.


4. Why doesn't it have a female scart connector?

We liked the idea that only the RGB-Pi is necessary.
Using a female connector would require an additional male to male cable.
Appart from the additional expense, it would result in a loss of quality depending on the extension cable used as explained in question 3.


5. I have a Sony Trinitron TV and red colors look muted.

In the case of having a Sony Trinitron TV and that the red colors look dark or brown: activate the corresponding fix from `[Display > Trinitron Color Fix]` menu option.
This issue only affects to some Sony Triniton TV models, so only do that if you noticed the colors beeing off.

From the `[Image > Image Adjustmen]` menu screen, a small blue square box is available with the an `OK` text inside. If you cannot read it, you must enable the fix.


6. Can I use the cable with Retropie, Recalbox or Lakka?

Yes, you can use it on any Raspberry Pi supported system, but be aware that these systems doesn't provide any kind of customization for displaying each system and/or game using the original resolution.
|This will result in games being displayed using a fixed resolution and in many cases suffering of glitches, shuttering and/or other image issues.
|That said, if you still want to enable the cable use in any of these systems, you can find instructions [over here](https://github.com/mortaca/RGB-Pi/blob/master/README.md).


7. How can I use an external USB/NFS storage?

To mount a USB unit:

1) Toggle the `[Settings > Load Games From > USB/NFS]` menu option.
2) The system will request a confirmation if formatting the unit is required.
|To connect to NFS drive:

1) Configure the shared unit as RW (read/write) without permissions. 
2) You will need `roms` and `BIOS` folder structure. The easiest way is to copy it from a USB-Drive formatted within RGB-Pi OS.
|3) From RGB-Pi OS go to `[Network > NFS]` and replace the prefilled values `server#path`. I.e.: `192.168.1.25#/srv/nfs/rgbpi`
4) Toggle the `[Settings > Load Games From > USB/NFS]` menu option.

8. Why do some games displays black bars or are a little off the screen?

Many games, even when played in the original system, have these problems because of the way they were originally developed.
|Also, do note that CRT TVs are very different from LCD TVs. Each TV has a slightly different centering adjustment even within the same TV series, so there is not an universal configuration that fits all TVs.
|You have three options for making TV adjustments:

1) Make software image adjustments by using the image assistant tool provided from the`[Image > Image Adjustment]` menu option.
|2) Make image adjustments by using the (commonly hidden) service menu offered by many TV models. Find out how to open your TV's service menu by searching the internet. :D
|3) Make physical adjustments to your TV (Warning - High Voltage). In many cases, applying some minor adjustments to the TV's yoke can fix a multitude of common issues.

9. What romsets are used by the different arcade emulators?

- fbalpha v0.2.97.43
- advmame (MAME 0.106)
- mame2003 (MAME 0.78)
- mame2010 (MAME 0.139)

10. Which RPi models are supported?

RGB-Pi OS has been tested on RPi2, RPi3 and RPi3 Plus models.


11. Can I use RGB-Pi on a LCD TV or with some upscaler?

You can, but there is no point in doing so. To connect to a modern Screen, we recommend using the native HDMI output and the Lakka distribution for Pi.


12. Can I connect a fan to the GPIO?

Many people use fans connected to the 5v and GND GPIO pins. Unfortunatelly the RGB-Pi connector occupies these pins but does not actively use them:
|1) It is possible to solder a cable from behind if you have soldering skills.
2) Another option is to get the 5v from the USB port using a modified cable.


13. Can I connect a power switch or joystick through the GPIO?

It is not possible to connect any device to the GPIO port while the RGB-Pi is connected since almost all pins are used to use the necessary 18 Bits for audio and video.

14. Why is the TV channel not selected automatically?

**Important!: This information is only valid if you are using the first revision of the RGB-Pi cable.**

In order to automatically set the TV to RGB mode, it is necessary to supply 12V to the scart cable but the RPi can only supply 5v.
|Some people have made modifications in their cable to introducing 12v in pin 8 of the scart. This is feasible using an external power supply or using of a step-up convereter that takes 5v in of the cable and converts it to 12v.
|Doing any moddification to the cable/RPi will be at your own risk. It is not necessary to lift the pin 8 of the PCB since it is not connected to ground, and it is designed to be used for modifications.
|NEW! The new version of the cable that is now available from the website, has this feature built-in among other improvements.


15. Vertical games are not displayed vertically, how can I fix that?

By default, vertical games are rotated to play in horizontal mode.
|Not a good option for PixelPerfect lovers, since because of the lack of interlaced resolutions, many vertical lines are lost when downscaling from 320 to 240 lines.

In case you want to play with your screen in a vertical position, you can do it by selecting the `[Display > System Mode > Arcade Vertical]` menu option.


16. Handheld games look very small.

The original resolution of portable consoles is very low. Since we aim to have a pixel perfect image for all systems, this is the expected behavior.


17. I don't have sound.

Check that you don't have anything connected to the HDMI port. This disables the GPIO output.


18. What is Netplay and how does it work?

Netplay is an interface designed to easily configure online gaming.

You have two operational modes, Server and Client. Choose Server if you want to serv other players or Client if you want to join to the online play provided by Server.
|If you are going to play as Server, after selecting this option, other players must select Client option and select your Nick from the Server name list.
After that, Server must start the game in first place followed by the rest of Client players.
|For privacy reassons, once Server option is selected, your friends have 30 seconds to connect with you by selecting the Client option. After that timeframe, you need to repeat the process.
|Note: in order to make the netplay work, please check that you have the port 55439 open in your router.


19. Is it good playing with screen bezels enabled?

It is recommended to disable such option since its continued use can burn-in the same on your TV / Arcade screen.


20. How can I create a backup of my favorites?

Both game list and favorites are stored in the SD card.

If you need to reinstall the system and don't want to lose your data, you can make a backup in two different ways:
|1) No Net (System doesn't boot up)

Even if the SD card is corrupted (if it's your case), probably you can mount it in any Linux distribution:
- Access the drive labeled as rootfs
- Navigate to /home/pi/RGB-Pi/data folder and make a copy of all games*.csv files
|2) By Net (System boots)

You can access by net to make your backup:
- Connect via SFTP (check your IP from [Network] menu) with user: pi and password: rgbpi
- Navigate to /home/pi/RGB-Pi/data folder and make a copy of all games*.csv files
|Finally, you can now restore and replace all the files of your new system by the ones that you have just copied by following the same connection methods you followed for the backup.


21. How can I use my custom scrap images?

You can copy your custom images to:
- SFTP: /home/pi/RetroPie/images
- Windows SMB: \\rgbpi\images

Note: you must create an additional folder with the name of the system to be used.
|The supported image format is .png with a resolution of 320x240.

The use of high resolution images can affect the system performance.
|The name of the image files must follow this format: romfilename.png

Example:

ROM name: shinobi.sms
PNG name: shinobi.png

Finally you must activate [Settings > Brackgrounds > Custom] menu option.


22. How can I save my Retroarch FBA remaps?

RGB-Pi OS has incorporated an automatic remap system for NeoGeo MVS/AES for matching the original systems.
|If you want to make your own remaps for FBA arcade, you must delete the following system files:

- /opt/retropie/configs/all
/retroarch/config/remaps/FB Alpha
/FB Alpha.rmp
- /opt/retropie/configs/all
/retroarch/config/remaps/FB Alpha
/_FB Alpha.rmp

---------------------------------------------------------------------------------------------------------

# Preguntas frecuentes
## Este FAQ está orientado a la ultima verson del sistema RGB-Pi OS Beta 19_06_30s, las respuestas que aquí se encuentran pueden no ser aplicables a versiones anteriores.

Preguntas:
1. Qué sistemas están soportados?
2. Cómo copio ROMs de juegos?
3. Por qué es el cable tan corto?
4. Por qué no tiene un conector scart hembra?
5. Tengo una TV Sony Triniton y los colores rojos se ven apagados.
6. Puedo usar el cable con Retropie, Recalbox o Lakka?
7. Cómo puedo usar una unidad externa USB/NFS?
8. Por qué algunos juegos muestran bandas negras o se salen un poco de la pantalla?
9. Qué romsets son usados por los diferentes emuladores arcade?
10. Qué modelos de RPi están soportados?
11. Puedo usar RGB-Pi en una TV LCD o con un escalador?
12. Puedo conectar un ventilador al GPIO?
13. Puedo conectar un interruptor o joystick al GPIO?
14. Por qué el canal de TV no se selecciona automáticamente?
15. Los juegos verticales no se ven en posición vertical, cómo puedo cambiar esto?
16. Los juegos portátiles se ven muy pequeños.
17. No tengo sonido.
18. Qué es Netplay y como funciona?
19. Es bueno jugar con marcos de pantalla activados?
20. Cómo creo una copia de seguridad de mis favoritos?
21. Cómo usar mis imágenes de escrapeo personalizadas?
22. Cómo guardo mis remaps de FBA Retroarch?

-------------------------------------------------------------------------------------------------------

1. Qué sistemas están soportados?

Máquinas Arcade MAME/FBA (.zip)
Atari 2600 (.a26 .rom)
Atari 400/800/XL/XE/5200 (.a52 .atr .bas .car .dcm .xex .xfd)
Atari 7800 (.a78)
Atari LYNX (.lnx)
WonderSwan (.ws)
WonderSwan Color (.wsc)
ColecoVision (.col)
PC Engine (.pce)
|CD-ROM2 System (.ccd .chd .cue)
Odyssey2 (.o2)
Nintendo NES (.fds .nes)
Famicom Disk System (.fds .nes)
Super Nintendo (.sfc .smc)
Nintendo 64 (.z64 .n64 .v64)
Game Boy (.gb)
Game Boy Color (.gbc)
Game Boy Advance (.gba)
SG-1000 (.sg), Master System (.sms)
Megadrive (.gen .md .smd)
|Mega-CD (.chd .cue)
Megadrive 32X (.32x)
Game Gear (.gg)
NEOGEO (.zip)
NEOGEO Pocket (.ngp)
NEOGEO Pocket Color (.ngc)
PlayStation (.pbp .cue .cbn .img .iso .m3u)
Amstrad CPC (.dsk)
Atari ST (.st .stx .ipf)
Commodore 64 (.crt .d64)
|Commodore Amiga (.uae .adf)
MSX (.rom .mx1 .mx2)
ZX Spectrum (.tap .tzx)
ScummVM (.svm)
MS-DOS (.sh)

2. Cómo copio ROMs de juegos?

Existen varias opciones para acceder a la carpeta de ROMs:

a) Desde Windows, abre el navegador de archivos y escribe \\rgbpi en la barra de direcciones
b) Puedes conectar via SFTP (consulta tu IP desde el menú [Redes]) con el usuario: pi y contraseña: rgbpi
|c) Si usas Linux, conecta la tarjeta SD a tu ordenador y desde la partición rootfs ve a la carpeta /home/pi/RetroPie/roms
d) Puedes crear una unidad RGB-Pi externa USB desde [Ajustes > Cargar Juegos Desde > USB/NFS]

3. Por qué es el cable tan corto?

Debido a que el cable no está blindado, no puede exceder los 25cm para evitar interferencias.
Si necesitas mayor distancia, puedes usar un cable alargador de scart macho a hembra, pero no podemos garantizar que la calidad de la imagen sea la misma que conectando diréctamente RGB-Pi a la TV.

4. Por qué no tiene un conector scart hembra?

Nos gusta la idea de que solo sea necesario el cable RGB-Pi.
El uso de un conector hembra obligaría hacer uso de un cable macho a macho adicional.
|Esto además de un gasto adicional para el usuario, conlleva una pérdida de calidad dependiendo del cable alargador utilizado como se explica en la pregunta 2.

5. Tengo una TV Sony Triniton y los colores rojos se ven apagados.

En caso de tener una TV Sony Triniton y notar que los colores rojos se ven oscuros o marrones, puedes arreglarlo activando el arreglo correspondiente desde el menú de opciones [Imagen > Arreglo Color Trinitron].
|Este problema solo afecta a algunos modelos de Sony Triniton, por lo que si no has notado colores incorrectos no debes activar esta opción.

Desde el menú [Imagen > Ajuste de Imagen] está disponible un pequeño recuadro azul con las letras OK en su interior. Si no puedes leerlo debes activar el fix.

6. Puedo usar el cable con Retropie, Recalbox o Lakka?

Sí, puedes usarlo en cualquier sistema soportado por Raspberry Pi, pero ten en cuenta que estos sistemas no proveen de las personalizaciones para poder mostrar casa sistema y/o juego usando la resolución original.
|Esto resultará en que los juegos se verán usando una resolución fija y en muchos casos sufriendo de errores gráficos, tirones, y otros problemas de imagen.
|Dicho esto, si realmente quieres activar el uso del cable en alguno de estos sistemas, puedes encontrar instrucciones de cómo hacerlo aquí: https://github.com/mortaca/RGB-Pi/blob
/master/README.md

7. Cómo puedo usar una unidad externa USB/NFS?

Para montar una unidad USB:

1) Solo tienes que activar la opción del menú [Ajustes > Cargar Juegos Desde > USB/NFS].
2) El sistema pedirá confirmación para formatear la unidad en caso requerido.
|Para conectar a una unidad NFS:

1) Neceritas configurar tu unidad de red como RW (lectura/escritura) y sin permisos.
2) Necesitarás una estructura de directorios [roms] y [BIOS]. Lo más sencillo es que los copies de un USB formateado por RGB-Pi OS.
|3) Desde RGB-Pi OS ve al menú [Redes > NFS] y sustituye los valores por defecto server#share. Ejemplo: 192.168.1.25#/srv/nfs/rgbpi
4) Ahora solo tienes que activar la opción del menú [Ajustes > Cargar Juegos Desde > USB/NFS].

8. Por qué algunos juegos muestran bandas negras o se salen un poco de la pantalla?

Muchos juegos, incluso jugados en el sistema original, tienen estos problemas debido a la manera en que fueron programados originalmente.
|Además hay que entender que las TV CRT son muy diferente de las LCD. Cada TV tiene unos ajustes algo distindos en centrado incluso tratándose del mismo modelo, de manera que no existe una configuración universal que se ajuste 100% a todas las TVs. 
|Tienes tres diferentes opciones para hacer ajustes en tu TV:

1) Hacer ajustes por software usando el asistente proporcionado desde el menú de opciones [Imagen > Ajuste de Imagen].
|2) Hacer ajustes de imagen usando el menú de servicio ofrecido por muchos fabricantes de TVs (normalmente oculto). Puedes descubrir como abrir este menú buscando en internet.
|3) Hacer ajustes físicos en tu TV (Peligro - Alto Voltage). En muchos casos, aplicando pequeños ajustes al yugo de tu TV puedes corregir los problemas más comunes.

9. Qué romsets son usados por los diferentes emuladores arcade?

- fbalpha v0.2.97.43
- advmame (MAME 0.106)
- mame2003 (MAME 0.78)
- mame2010 (MAME 0.139)

10. Qué modelos de RPi están soportados?

RGB-Pi OS ha sido probado en los modelos RPI2, RPi3 y RPi3 Plus.

11. Puedo usar RGB-Pi en una TV LCD o con un escalador?

Puedes pero no tiene mucho sentido usar el cable en TVs no CRT. Para conectar a TVs planas, recomendamos el uso del conector HDMI y la distribución Lakka.

12. Puedo conectar un ventilador al GPIO?

Mucha gente usa ventiladores conectador a los pines de 5v y GND del GPIO. Desafortunadamente el cable RGB-Pi ocupa estos pines aunque no los utiliza, de manera que:
|1) Es posible soldar un cable por detrás si tienes habilidades soldando.
2) Otra opción es sacar los 5v del puerto USB usando un cable modificado.

13. Puedo conectar un interruptor o joystick al GPIO?

No es posible conectar ningún dispositivo al GPIO mientras RGB-Pi está conectado ya que casi todos los pines son usados para sacar los 18 Bits del audio y vídeo.

14. Por qué el canal de TV no se selecciona automáticamente?

Importante! Esta información solo es válida si estás usando la primera revisión del cable RGB-Pi.

Para poder poner la TV en modo RGB automáticamente, es necesario proveer de 12v al cable scart, pero la RPi solo dispone de 5v.
|Algunas personas has realizado modificadiones en sus cables para introducir 12v en el pin 8 del scart. Esto es factible usando una fuente externa o usando un elevador de tensión que convierta los 5v en 12v.
|Cualquier modificación al cable/RPi será bajo su propio riesgo. En caso de proceder, no es necesario levantar el pin 8 de la PBC ya que no está conectada a negativo y está diseñada para posibles modificaciones.
|NOVEDAD! La nueva versión del cable disponible desde la web oficial, ya dispone de esta funcionalidad además de otras mejoras.

15. Los juegos verticales no se ven en posición vertical, cómo puedo cambiar esto?

Por defecto, los juegos verticales están rotados para su uso en modo horizontal.
|No es la opción preferida para los amantes del PixelPerfect, ya que a causa de la falta de resoluciones entrelazadas, muchas líneas verticales se pierden al pasar de 320 a 240 líneas. 

En caso de que desees jugar con la pantalla en vertical, puedes hacerlo desde el menú de opciones [Imagen > Modo de Sistema > Arcade Vertical].

16. Los juegos portátiles se ven muy pequeños.

La resolución original de las consolas portátiles era muy baja, y dado que intentamos mantener la imagen PixelPerfect para todos los sistemas, este es el comportamiento esperado.

17. No tengo sonido.

Comprueba que no tienes nada conectado al puesrto HDMI. Esto desactiva la salida GPIO.

18. Qué es Netplay y como funciona?

Netplay es una interface diseñado para configurar facilmente el juego online.

Tienes dos modos de operación, Server y Client. Elige Server si quieres servir a otros juegadores o Client si te quieres unir a la partida online provista por un Server.
|Si vas a jugar como Server, después de seleccionar esta opción, los otros jugadores deben seleccionar la opción Client y luego seleccionar tu Nick desde la lista de nombres de Servidor.
Tras esto, el Server debe iniciar el juego el primero seguido del resto de jugadores Client.
|Por privacidad de datos, al seleccionar Server, tus amigos tendrán 30 segundos para conectar contigo seleccionando la opción Client. Pasado ese tiempo deberás repetir la operación.
|Nota: para que el netplay funcione, asegurate de tener abierto el puerto 55439 en tu router.

19. Es bueno jugar con marcos de pantalla activados?

Se recomienda desactivar dicha opción ya que su uso continuado puede dejar marcas en la pantalla de tu TV / Arcade.

20. Cómo creo una copia de seguridad de mis favoritos?

Tanto la lista de juegos como los favoritos se almacenan en la tarjeta SD.

Si necesitas reinstalar el sistema y no quieres perder tus datos, puedes hacer una copia de seguridad de dos maneras:
|1) Sin Red (El sistema no arranca)

Incluso con la tarjeta SD corrupta (si es tu caso), probablemente puedas montarla en cualquier distribución Linux:
- Accede a la unidad con el nombre rootfs
- Navega al directorio /home/pi/RGB-Pi/data y haz una copia de todos los archivos games*.csv
|2) Por Red (El sistema arranca)

Puedes acceder por red para hacer tu copia de seguridad:
- Conecta via SFTP (consulta tu IP desde el menú [Redes]) con el usuario: pi y contraseña: rgbpi
- Navega al directorio /home/pi/RGB-Pi/data y haz una copia de todos los archivos games*.csv
|Finalmente, en tu nuevo sistema ya puedes restaurar y reemplaza todos los archivos del sistema por los que acabas de copiar siguiendo el mismo método de conexión que para hacer la copia de seguridad.

21. Cómo usar mis imágenes de escrapeo personalizadas?

Puedes copiar tus imágenes diréctamente en:
- SFTP: /home/pi/RetroPie/images
- Windows SMB: \\rgbpi\images

Nota: debes crear un subdirectorio adicional con el nombre del sistema a usar.
|El formato de imagen soportado es .png con una resolución de 320x240.

El uso de imágenes de alta resolución puede afectar el rendimiento del sistema.
|El nombre de los archivos de imágenes deben tener el formato: romfilename.png

Ejemplo:

Nombre ROM: shinobi.sms
Nombre PNG: shinobi.png

Finalmente debes activar la opción [Ajustes > Fondos > Personalizado].

22. Cómo guardo mis remaps de FBA Retroarch?

RGB-Pi OS tiene incorporado un sistema automático de remapeo para NeoGeo MVS/AES para ajustarse a los sistemas originales.
|Si quieres hacer remapeos en arcade FBA, tienes que borrar los siguientes archivos de sistema:

- /opt/retropie/configs/all
/retroarch/config/remaps/FB Alpha
/FB Alpha.rmp
- /opt/retropie/configs/all
/retroarch/config/remaps/FB Alpha
/_FB Alpha.rmp


    

