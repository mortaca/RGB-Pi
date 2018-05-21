Available in English and Spanish / *Disponible en Ingles y Español*
# Frequently Asked Questions
## This FAQ is oriented to the latest available version of the system 4.1 Final, the answers here may not be useful for previous versions.

Questions:
1. Why is the cable so short?
2. Why doesn't it have a female scart?
3. Can I use the cable with Retropie or other than its modified version of Recalbox?
5. How can I use an external USB storage?
6. The menu image looks distorted but the games look good.
7. In games I see a black strip or I get off the screen.
8. What romsets are needed for arcade?
9. I make changes in Retroarch and they can not be saved.
10. I have a RPi2 or a previous model, what system do I use?
11. Why is not Kodi available?
12. Can I use RGB-Pi on a LCD TV or with some upscaler?
13. When the TV is silent there is an annoying noise in the audio.
14. Can I connect a fan to the GPIO?
15. Can I connect a power switch or the joysticks through the GPIO?
16. Why the TV channel is no selected automatically?
17. Vertical games are seen on the side, how can I change them?
18. Can I upgrade the system from within Recalbox?
19. Handheld games look very small
20. I do not have sound
21. I have a question that is not on the listfffffffffffffffffffffffffffffffffffffffff

---------------------------------------------------------------------------------------------------
Answers:
1. The flat cable can not exceed 25cm to avoid getting interference when it is a non-insulated cable.
If you need a longuer distance you can use a scart male-female extension, we can not ensure that the quality becomes as         high as connecting the RGB-Pi directly to the TV.

2. The use of a scart female implies the need for an additional scart cable, I liked the idea that only RGB-Pi is necessary and nothing more to work, besides I can not control what type of extensor cable each person could use and may have interference and a bad experience.

3. Yes, it is possible to use it on any system supported by RPI, but attention! You will not have the original resolutions provided by our software for each game, you will see everything through a fixed resolution.
If you want to do it anyway you have the instructions [here](https://github.com/mortaca/RGB-Pi/blob/master/README.md)

4. We are limited by the pace of development of the Recalbox team, they have not yet released version 4.1 and are in Alpha phase, so we have to be Alpha phase also until they release the Beta version.

5. To use USB external storage with RGB-Pi, use only the USB Mount script in the Config section, first you have to format the USB in Fat32 and create the following folders /roms /bios and /saves, then in /roms each system must have its folder with the same name that is used in the SD memory for example /roms/psx, once the system is booted with USB connected we will select USB Mount and the USB folders will be available, it will be necessary to activate this one Last step in each system reboot.

6. This is because Emulationstation uses a peculiar resolution of 450x270 50Hz and on some televisions can give problems.
To solve it just open the ScreenUtility in the RGB-Pi Config section and change the SystemResolution field from 450 to 320.

7. The CRT televisions are very different from the current LCD and each TV had a slightly different centering adjustment, so there is no configuration that is good on all monitors and it is necessary that each one adjust the image to your TV, We offer a centering solution so **no acces to Retroarch is required** to adjust the image.
To adjust the image you have the ScreenUtility application in the RGB-Pi Config section from where you can adjust the horizontal and vertical position, you can also expand or collapse the image horizontally without losing the PixelPerfect, after adjusting the values you can launch a grid-centered option CenteringTest (This test function may be fail sometime for reasons related to Recalbox)

8. For MAME2003 the romset 0.78, AdvanceMAME 0.106 and FBAlpha Libretro v0.2.97.42.

9. Our system uses custom files to retroarch so any changes will be discarded, if you want to introduce a change in retroarch you can find the files we use segregated by consoles in the folder /share/RGB-Pi/Retroarch

10. The latest improvements are only available for the RPi3, if you have a previous version contact me to elaborate a specific distribution for the system that you use, once the Beta version is released it will be available for all systems.

11. Still we can not get an interlaced mode and to display Kodi in necessary 640x480i resolution, a lower resolution makes it totally unusable, at the time that it is possible to use it with an acceptable quality we will support it.

12. It can be but it is totally absurd, it is better to directly use the HDMI output and Recalbox.

13. This is due to interference in the cable by the WiFi signal that the Raspberry emits, disable the WiFi in the menu and the noise will disappear.

14. Many people use a fan connected to +5v and GND in the GPIO, the RGB-Pi connector occupies these pins but does not use it, it is possible to solder a cable from the bottom if you have knowledge of welding, another option is to pick the +5v from the USB port using a cut cable.

15. It is not possible to connect a switch to power the RPi or any joystick to the GPIO port while the RGB-Pi is connected since almost all the pins are used to take out the necessary 18 Bits of video and sound.

16. In order for the TV to be automatically set to RGB mode, it is necessary to supply +12V to the scart and the RPi can only supply +5v which would activate the 16/9 mode and it is necessary to use the remote control to switch to 4/3.
There are those who have made modifications in their cable to introduce +12v in pin 8 of the scart, this is possible to do it through an external power supply or with the use of a step up that takes +5v of the flat cable and make it +12v, **these modifications can be made at your own risk.**
In case of wanting to do it it is not necessary to lift pin 8 of the PCB since it is not connected to ground, and it is designed thus for possible modifications.

17. Trying to always respect the original resolutions of each game the verticals should be seen in this way, in case you want to rotate them 90º it is possible to do it through ScreenUtility in the section RGB-Pi Config with the option Rotate Vertical Games -90.
Not a good option for lovers of PixelPerfect since not having resolutions interlaced for the time lost many vertical lines, a game that normally has 320 lines in a resolution that only shows 240 does not look good, in the assumption That interlaced resolutions may be available in the future, these 320 lines could be encabeled with an interlaced resolution of 480i but a result as good as the original is not obtained.

18. No, if you do this you will lose all the modifications made to support the RGB-Pi cable and the system will stop working.

19. The resolution of the original portables was very low, respecting the PixelPerfect should be seen, if you want to expand it to full screen anyway you can do it from the ScreenUtility by activating the HandheldsStretched 1 option.
Thus, in addition to seeing the huge pixels, the aspect ratio of the image changes from the original.

20. Check that you do not have anything connected by HDMI, this deactivates the output by the GPIO.

21. Please contact us at **info@rgb-pi.com** or in the forums where we participate.

---------------------------------------------------------------------------------------------------------

# Preguntas frecuentes
## Este FAQ está orientado a la ultima verson del sistema 4.1 Final, las respuestas que aquí se encuentran pueden no ser aplicables a versiones anteriores.

Preguntas:
1. ¿Por que el cable es tan corto?
2. ¿Porque no tiene un conector scart hembra?
3. ¿Puedo usar el cable en Retropie u otros sistemas que no sean vuestra versión modificada de Recalbox?
4. Tengo una TV Sony Trinitron y los colores rojos se ven muy apagados.
5. ¿Como puedo utilizar un almacenamiento externo USB?
6. La imagen del menu se ve distorsionada pero los juegos se ven bien.
7. En los juegos veo una franja negra en un lateral o que la imagen se sale de la pantalla.
8. ¿Que romsets se necesitan para arcade?
9. Hago cambios en Retroarch pero no se quedan guardados.
10. Tengo una RPi2 o anterior, ¿que sistema debo utilizar?
11. ¿Porque no está disponible Kodi?
12. ¿Se puede utilizar RGB-Pi en un televisor LCD directo o con algun reescalador?
13. Al quedar la TV en silencio se escucha un ruido molesto en el audio.
14. ¿Puedo conectar un ventilador en el GPIO?
15. ¿Puedo conectar un interruptor de encendido o los joystick al GPIO?
16. ¿Porque el canal AV de la tele no se selecciona automaticamente?
17. Los juegos verticales se ven tumbados, ¿como puedo cambiarlos?
18. ¿Puedo actualizar el sistema desde dentro de Recalbox?
19. Los juegos de portatiles se ven muy pequeños.
20. No tengo sonido.
21. Tengo una duda que no se encuentra en ésta lista
---------------------------------------------------------------------------------------------------
Respuestas:
1. El cable plano no debe superar los 25cm para evitar interferencias al ser un cable no aislado.
Si necesitas una distancia mayor puedes utilizar un alargador scart hembra macho, pero no puedo asegurar que la calidad sea tan alta como conectando el RGB-Pi directo a la tele.

2. El uso de un scart hembra implicaria la necesidad de un cable scart adicional, me gusta la idea de no necesitar nada mas que un RGB-Pi para funcionar, tampoco seria posible controlar que tipo de extensor utilizaria cada persona y posiblemente mucha gente sufriria interferencias que provocaran una mala experiencia.

3. Si, es posible utilizar el cable en cualquier sistema soportado por la RPi, pero atención! No vais a tener las resoluciones originales de cada juego proporcionadas por nuestro software, vais a ver todo a través de una unica resolución fija.
Si de todos modos quereis probar otros sistemas teneis las instrucciones [aquí](https://github.com/mortaca/RGB-Pi/blob/master/README.md)

4. En el caso de tener una TV Sony Trinitron y detectar que los colores rojos se ven muy apagados o marrones debes ir a la sección Config y activar el script Trinitron Fix, si tienes una Trinitron pero no has notado ningún problema con los colores no debes activar el Fix.

5. Para utilizar el amacenamiento externo USB con RGB-Pi hay que hacer uso exclusivamente del script USB Mount en la seccion Config, primero hay que formatear el USB en Fat32 y creat las siguientes carpetas /roms /bios y /saves, después dentro de /roms cada sistema debe tener su carpeta con el mismo nombre que se utiliza en la memoria SD por ejemplo /roms/psx, una vez arrancado el sistema con el USB conectado seleccionaremos USB Mount y las carpetas del USB quedaran disponibles, sera necesario activar éste ultimo paso en cada reinicio del sistema.

6. Esto sucede porque para Emulationstation usamos una resolucion particular de 450x270 50Hz y en algunas televisiones puede causar problemas.
Para solucionarlo solo hay que abrir la ScreenUtility en la seccion RGB-Pi Config y cambiar el campo SystemResolution de 450 a 320.

7. Las teles de tubo son muy distintas de las LCD y cada televisor tiene unos parametros de centrado distintos, de modo que no hay una configuración que se vea bien en todos los televisores y es posible que sea necesario centrar la imagen en tu TV, para ello ofrecemos una solucion propia y **no es necesario el uso de Retroarch**.
Para ajustar la imagen tienes las aplicacion ScreenUtility en la seccion RGB-Pi Config desde donde podrás ajustar la posicion horizontal y vertical, también puedes expandir o contraer la imagen horizontalmente sin perder el PixelPerfect, después de ajustar los valores se puede lanzar una rejilla de centrado en la opción CenteringTest (Es posible que esta funcion de test falle de vez en cuando por motivos relacionados con Recalbox)

8. Para MAME2003 el romset 0.78, AdvanceMAME 0.106 y FBAlpha Libretro v0.2.97.42.

9. Nuestro sistema utiliza archivos personalizados para Retroarch y cualquier cambio que se haga desde el menu sera descartado, si quieres introducir algun cambio en los archivos personalizados de retroarch los puedes encontrar en la carpeta /share/RGB-Pi/Retroarch/ cada uno con el nombre de la consola a la que afecta.

10. Las ultimas mejoras solo están disponibles para la RPi3, si tienes una versión anterior ponte en contacto conmigo para elaborar una distribución especifica para el sistema que utilices, una vez se lance la versión Beta ésta estara disponible para todos los sistemas.

11. De momento no podemos tener resoluciones entrelazadas y para Kodi es necesario 640x480i, una resolucion inferior provoca que sea totalmente inutilizable, en el momento que sea posible manejar Kodi con una calidad aceptable le daremos soporte.

12. Se puede pero es totalmente absurdo, es mejor utilizar directamente la salida HDMI y Recalbox.

13. Esto es debido a interfetencias en el cable por la señal WiFi que emite la Raspberry, desactivar el WiFi en el menu y el ruido desaparecera.

14. Mucha gente utiliza un ventilador conectado al pin de +5v y GND en el GPIO, el conector de RGB-Pi ocupa estos pines pero no los utiliza, es posible soldar los cables por la parte inferior para los que tengan algun conocimiento de soldadura, otra opción es coger los +5v de un cable USB cortado.

15. No es posible utilizar un boton de encendido o ningún joystick conectado al GPIO porque el RGB-Pi está utilizando la mayoria de los pines para sacar los 18 Bits de video necesario y el sonido.

16. Para que la tele se ponga en modo RGB automaticamente es necesario suministrar +12v al scart y la RPi solo puede suministrar +5v con lo que conseguiriamos poner la tele en 16/9 y seria necesario utilizar el mando para cambiar a 4/3.
Hay quien ha modificado su cable para introducir +12v en el pin 8 del scart, se puede utilizar una fuente de alimentación o un step up que cogeria los +5v del cable plano y los convertiria en +12v, **Estas modificaciones deben ser hechas bajo su propio riesgo**
En el caso de querer hacerlo no es necesario levantar el pin 8 del PCB ya que éste no está conectado a tierra, ya se diseño así especificamente para facilitar una posible modificacion.

17. Intentando respetar siempre las resoluciones originales de cada juego los verticales deben verse de éste modo, en caso de querer rotarlos 90º es posible hacerlo mediante la ScreenUtility en la seccion RGB-Pi Config con la opcion Rotate Vertical Games -90.
No es una buena opcion para los amantes del PixelPerfect puesto que al no disponer de resoluciones entrelazadas por el momento se pierden muchas lineas verticales, un juego que normalmente tiene 320 lineas en una resolución que solo muestra 240 no se ve nada bien, en el supuesto de que en un futuro se disponga de resoluciones entrelazadas se podria encaber esas 320 lineas con una resolución entrelazada de 480i pero no se obtiene un resultado tan bueno como el original.

18. No, si haces esto perderas todas las modificaciónes hechas para soportar el cable RGB-Pi y el sistema dejara de funcionar.

19. La resolución de las portatiles originales era muy baja, respetando el PixelPerfect así debe verse, si de todos modos quieres expandirla a pantalla completa puede hacerlo desde la ScreenUtility activando la opción HandheldsStretched 1.
De éste modo además de ver los pixeles enormes la proporción de aspecto de la imagen cambia respecto a la original.

20. Comprueba que no tengas nada conectado por HDMI, ésto desactiva la salida por el GPIO.

21. Por favor contactanos a través de **infor@rgb-pi.com** o en alguno de los foros donde participamos.


    

