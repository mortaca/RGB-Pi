Available in English and Spanish / *Disponible en Ingles y Español*
# Frequently Asked Questions
## This FAQ is oriented to the latest available version of the system 4.1 Final 1.1, the answers here may not be useful for previous versions.

Questions:
1. Why is the cable so short?
2. Why doesn't it have a female scart?
3. Can I use the cable with Retropie or other than its modified version of Recalbox?
4. I have a Sony Trinitron TV and the red colors are very muted.
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
21. What is EasyNetplay and how does it work?
22. What are the arcade Cropped and Forced modes?
23. The intro slows down at the first start.
24. My external hard drive or pendrive is not mounted automatically.
25. I have a question that is not on the list
---------------------------------------------------------------------------------------------------
Answers:
1. The flat cable can not exceed 25cm to avoid getting interference when it is a non-insulated cable.
If you need a longuer distance you can use a scart male-female extension, we can not ensure that the quality becomes as         high as connecting the RGB-Pi directly to the TV.

2. The use of a scart female implies the need for an additional scart cable, I liked the idea that only RGB-Pi is necessary and nothing more to work, besides I can not control what type of extensor cable each person could use and may have interference and a bad experience.

3. Yes, it is possible to use it on any system supported by RPI, but attention! You will not have the original resolutions provided by our software for each game, you will see everything through a fixed resolution.
If you want to do it anyway you have the instructions [here](https://github.com/mortaca/RGB-Pi/blob/master/README.md)

4. In the case of having a Sony Trinitron TV and detecting that the red colors are very dark or brown you should go to the Config section and activate the Trinitron Fix script, if you have a Trinitron but you have not noticed any problems with the colors you don't activate the Fix.

5. To use USB external storage with RGB-Pi, use only the USB Mount script in the Config section, first you have to format the USB in Fat32 and create the following folders /roms /bios and /saves, then in /roms each system must have its folder with the same name that is used in the SD memory for example /roms/psx, once the system is booted with USB connected we will select USB Mount and the USB folders will be available, it will be necessary to activate this one Last step in each system reboot.

6. This is because Emulationstation uses a peculiar resolution of 450x270 50Hz and on some televisions can give problems.
To solve it just open the ScreenUtility in the RGB-Pi Config section and change the SystemResolution field from 450 to 320.

7. The CRT televisions are very different from the current LCD and each TV had a slightly different centering adjustment, so there is no configuration that is good on all monitors and it is necessary that each one adjust the image to your TV, We offer a centering solution so **no acces to Retroarch is required** to adjust the image.
To adjust the image you have the ScreenUtility application in the RGB-Pi Config section from where you can adjust the horizontal and vertical position, you can also expand or collapse the image horizontally without losing the PixelPerfect, after adjusting the values you can launch a grid-centered option CenteringTest (This test function may be fail sometime for reasons related to Recalbox)

8. For MAME2003 the romset 0.78, AdvanceMAME 0.106 and FBAlpha Libretro v0.2.97.43.

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

19. The resolution of the original handhelds was very low, respecting the PixelPerfect so it should be seen, if it bothers you to see the black frame around the screen you can activate the bezels with the image of the original console from the ScreenUtility with the warning that leaving a fixed image on a CRT for a long time can leave marks on the phosphorus.

20. Check that you do not have anything connected by HDMI, this deactivates the output by the GPIO.

21. EasyNetplay is an interface of RGB-Pi designed to easily configure the Netplay or online game, once inside we have two operating modes, such as HOST or as a CLIENT, in each game there must be a HOST to which they will connect the rest of the players, if you activate the HOST mode the client mode will be deactivated automatically and you will have to open port 55435 in your router pointing to the IP address of your Pi, depending on your router model this is done differently, it is necessary that you search in google your concrete model and how to open the ports towards an IP.
    Once this is done we can leave the application and check which is our IP published from a mobile phone connected to our network or from the pc to give it to other players.
    In the upper right part of the application you will find a link to the Discord server where there are several voice chat rooms available to be used from the mobile phone during the game, for there you can give your IP safely only to friends with those who go to play.
    In the case of other players who are not going to be host must activate the client mode within EasyNetplay, will have the option to choose 5 storage boxes of different IPs that can be edited without keyboard with the use of the command jumping 1 in 1 or of 10 in 10 the numeric values, once this is finished we can leave the application and from this moment we are ready to play online.
    It is important that all players share the exact same rom and that they are retroarch emulators, for example advmame it is not possible to use it for Netplay.
    With all this we can start playing from one game to another without having to touch anything else in the configuration, remember that if we want to have a good gaming experience it is necessary to use network cable directly to the router, the use of wifi or PLCs goes to make the experience unplayable.
    The first to enter the game must always be the HOST and once inside the CUSTOMERS can enter, to exit the game in the reverse order being the HOST the last to leave.
    There is the possibility when there are games of 4 players to add a bit of input lag so that the synchronization between all players is better, it can also be useful in connections with a little bad latency, you have to enter the menu of retroarch with hotkey + B and search in options and network input_latency_fame box that will be set to 2 can be extended to 3 or 4 if necessary, when you enter the menu the game will be paused for other users, this value will be reset every time leave us a game.
    
22. The arcade selector that shows us the options Forced and Cropped is only activated in games that exceed 240 scanlines, games that are exactly 240 lines are automatically adjusted in height so they will have a bit of vertical overscan but it is better solution to force them because in that mode would be excessive black stripes, the games of 256 lines or more we now have the option to force them by modifying the horizontal frequency of the monitor so that they can be compressed to see the full image of the game plus a small strip black or see them in Cropped mode with the image cut and much vertical overscan, this happens because they are games designed for arcade machines where you could adjust the value of vertical size of the image with a potentiometer that we do not have in commercial TVs, in the same way games of 224 lines but of 55Hz that a TV recognizes as PAL and compresses them we can force them and see them in their original resolution avoiding the s black stripes.

23. This happens because the system is expanding the capacity of the micro SD, you have to let it finish and not turn off the Pi at this point, the next time you start the system you will see the intro correctly.

24. External hard drives or high capacity pendrives may not be mounted automatically at start-up to avoid too slow starting, they must be activated manually with USB Mount.

25. Please contact us at **info@rgb-pi.com** or in the forums where we participate.

---------------------------------------------------------------------------------------------------------

# Preguntas frecuentes
## Este FAQ está orientado a la ultima verson del sistema 4.1 Final 1.1, las respuestas que aquí se encuentran pueden no ser aplicables a versiones anteriores.

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
21. ¿Que es EasyNetplay y como funciona?
22. ¿Que son los modos Cropped y Forced de arcade?
23. La intro se ralentiza en el primer arranque.
24. Mi disco duro externo o pendrive no se monta automaticamente.
25. Tengo una duda que no se encuentra en ésta lista
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

8. Para MAME2003 el romset 0.78, AdvanceMAME 0.106 y FBAlpha Libretro v0.2.97.43.

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

19. La resolución de las portatiles originales era muy baja, respetando el PixelPerfect así debe verse, si te molesta ver el marco negro al rededor de la pantalla puedes activar los bezeles con la imagen de la consola original desde el ScreenUtility con la advertencia de que dejar una imagen fija en un CRT durante mucho tiempo puede dejar marcas enel fosforo.

20. Comprueba que no tengas nada conectado por HDMI, ésto desactiva la salida por el GPIO.

21. EasyNetplay es una interfaz propia de RGB-Pi pensada para configurar de forma sencilla el Netplay o juego en linea, una vez dentro tenemos dos modos de funcionamiento, como HOST o como CLIENTE, en cada partida tiene que haber un HOST al que se van a conectar el resto de jugadores, si activas el modo HOST quedara desactivado el modo cliente automaticamente y deberas abrir el puerto 55435 en tu ruter apuntando hacia la direccion IP de tu Pi, dependiendo de tu modelo de ruter esto se hace de forma distinta, es necesario que busqueis en google vuestro modelo concreto y como abrir los puertos hacia una IP.
    Una vez hecho esto ya podemos salir de la aplicación y comprobaremos cual es nuestra IP publica desde un telefono movil conectado a nuestra red o desde el pc para darsela al resto de jugadores.
    En la parte superior derecha de la aplicación encontrareis un enlace al servidor de Discord donde hay disponibles diversas salas de chat de voz para ser utilizadas desde el telefono movil durante la partida, por ahi mismo podeis dar vuestra IP de forma segura solo a los amigos con los que vayáis a jugar.
    En el caso del resto de jugadores que no van a ser host deben activar el modo cliente dentro de EasyNetplay, tendran la opcion de escoger 5 casillas de almacenamiento de IPs distintas que se pueden editar sin teclado con el uso del mando saltando de 1 en 1 o de 10 en 10 los valores numericos, una vez terminado ésto ya podemos salir de la aplicación y a partir de éste momento estamos listos para jugar en red.
    Es importante que todos los jugadores compartan la misma rom exacta y que sean emuladores de retroarch, por ejemplo advmame no es posible utilizarlo para Netplay.
    Con todo ésto podemos empezar a jugar pasando de un juego a otro sin tener que tocar nada mas en la configuración, recordar que si queremos tener una buena experiencia de juego es necesario utilizar cable de red directamente al ruter, el uso de wifi o PLCs va a hacer la experiencia injugable.
    El primero en entrar en la partida tiene que ser siempre el que haga de HOST y una vez dentro pueden ir entrando los CLIENTES, para salir de la partida seria en el orden inverso siendo el HOST el ultimo en abandonarla.
    Existe la posibilidad cuando hay partidas de 4 jugadores de añadir un poco de input lag para que la sincronización entre todos los jugadores sea mejor, tambien puede ser util en conexiones con una latencia un poco mala, hay que entrar en el menu de retroarch con hotkey+B y buscar en opciones y network la casilla input_latency_fame que estara puesta en 2 se puede ampliar a 3 o 4 si fuese necesario, cuando se entre en el menu la partida se pausara para el resto de usuarios, este valor se reseteara cada vez que abandomenos un juego.
    
22. El selector de arcade que nos muestra las opciones Forced y Cropped solo se activa en juegos que superan las 240 scanlines, los juegos que son exactamente de 240 lineas son ajustados en altura automaticamente con lo que tendran un poco de overscan vertical pero es mejor solución que forzarlos ya que en ese modo se verian unas franjas negras excesivamente grandes, los juegos de 256 lineas o mas tenemos ahora la opción de forzarlos modificando la frecuencia horizontal del monitor para que se compriman pudiendo ver la imagen completa del juego mas una pequeña franja negra o verlos en modo Cropped con la imagen cortada y mucho overscan vertical, esto sucede porque son juegos pensados para maquinas arcade donde se podia ajustar el valor de tamaño vertical de la imagen con un potenciometro que no tenemos en las TVs comerciales, del mismo modo juegos de 224 lineas pero de 55Hz que una TV reconoce como PAL y los comprime podemos forzarlos y verlos en su resolución original evitando las franjas negras.

23. Esto sucede porque el sistema está expandiendo la capacidad de la micro SD, hay que dejar que termine y no apagar la Pi en este punto, en la siguiente vez qye se arranque el sistema se vera la intro correctamente.

24. Los discos duros externos o pendrives de mucha capacidad pueden no ser montados automaticamente en el arranque para evitar un arranque demasiado lento, deben ser activados de forma manual con USB Mount.

25. Por favor contactanos a través de **info@rgb-pi.com** o en alguno de los foros donde participamos.


    

