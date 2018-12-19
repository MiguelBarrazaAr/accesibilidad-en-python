# accesibilidad-en-python
ejemplos de librerías para aplicar accesibilidad con lectores de pantalla en python

lectores de pantallas disponibles:

## en macintos:

  Formas de activar y desactivar VoiceOver: 
- Pulse Comando + F5. Si VoiceOver está activado, puede pulsar Comando + F5 para desactivarlo.
- Utilice el panel Acceso Universal de Preferencias del Sistema.

[mas información](https://www.apple.com/es/voiceover/info/guide/_1124.html)

## linux

  Orca funciona con aplicaciones y kits de herramientas que soportan la interfaz del proveedor de servicios de tecnologías de asistencia (AT-SPI), que es la infraestructura principal de tecnologías de asistencia para Linux y Solaris. Las aplicaciones y kits de herramientas que soportan la AT-SPI incluyen el kit de herramientas GTK+ de GNOME, el kit de herramientas Swing de la plataforma Java, OpenOffice, Gecko, y WebKitGtk.
- Para activar y desactivar Orca en GNOME, pulse Super+Alt+S.
- Escriba orca, con cualquier parámetro opcional, en una ventana de la terminal o en el diálogo Ejecutar y

[mas información](https://help.gnome.org/users/orca/stable/introduction.html.es)

# windows

  En windows se puede activar el narrator desde el centro de accesibilidad pulsando tecla windows+u. En windows 10 la lectura es bastante aceptable, pero se recomienda utilizar el lector NVDA que se puede encontrar en esta web:
[web de NVDA](https://www.nvaccess.org/)
[página de la comunidad en español](https://nvda.es/)

# android

  Desde ajustes / accesibilidad se puede configurar todos los parámetros. El lector se llama talkback.
nota: al activar talkback los gestos cambian, para abrir un elemento se realiza con doble toque.

# librerías en python

[tolk](https://github.com/dkager/tolk)
[accessible_output2](https://bitbucket.org/qsoft/accessible_output2)