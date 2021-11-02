
# Werkstattauftrag W13-PiGlow
<br>

# Inhaltsverzeichnis
 - [Autoren](#1-autoren-versionierung-des-dokumentes)
 - [Einfuerung](#2-einfuehrung)
 - [Hardware-Software](#3-benoetigte-hard--und-software)
 - [Installationsanleitung](#4-installationsanleitung)
 - [Qualitaetskontrolle](#5-qualitaetskontrolle)
 - [Error-Handling](#6-error-handling)
 - [Quellen](#7-quellen)
 - [Opensource Lizenz](#8-opensource-lizenz)





# 1. Autoren, Versionierung des Dokumentes
Autoren: Jonah Gutknecht, Thomas Züger<br>
Version: 1.0
<br>



# 2. Einfuehrung 

   - Beschreibung <br> Mit der installation von PiGlow können verschiedene Lämpchen gesteuert und verwaltet und ein und ausgeschaltet werden. Zusätzlich kann man die Farben-Kombinationen steuern. Man kann es auch soweit benützen, dass die Lampen leuchten, wenn man eine Aktion ausführt. <br>
  
   - Zeitaufwand <br> Die Installation von PiGlow (Werkstatt Auftrag 13) ist bis am 02:11.2021 um 12:00 abgeschlossen.<br>
  
  - Einleitung <br>
  Mit dem GlowPi Module kann man verschiedenste Lämpchen mit einem Python Script ansteuern und konfigurieren. Durch dieses Script können die Lämpchen an- und ausgeschaltet werden und man kann individuell die Farben des Lämpchen steuern. <br>
  Wir haben uns überlegt eine Farbenkombination von Rot und Orange zu wählen passend zu Halloween. 


   - Stolpersteine & Kniffe<br> Die Programmiersprache von dem GlowPi ist Python, da wir noch nie mit Python programmiert haben, musste wir uns Zeit nehmen die essentielle commands von Python zu lernen. Zusätzlich mussten wir uns überlegen wie genau man die einzelnen Lampen steuert.<br>

# 3. Benoetigte Hard- und Software
  ## Hardware Materialliste<br>
  1x RaspberryPI v4 (inkl. Stromkabel)<br>
  1x HDMI zu DVI Adapter<br>
  1x HDMI zu miniHDMI Adapter<br>
  1x Externer Bildschirm<br>
  1x Tastatur<br>
  1x Maus<br>
  1x PiGlow<br>

  ## Software Anforderungen<br>
1x RaspberryPI Linux Image<br>
<br>


# 4. Installationsanleitung
 (Didaktisch reduzierte Anleitung. Lernende sollen eine eigene Lösungswege realisieren)<br>
 <br>

 ## Vorbereitung Raspberry
 Auf dem RaspberryPI WLAN einrichten.
 <br>RaspberryPI Updates durchführen update und upgrade.<br>
 Neues Python Directory im Home verzeichnis erstellen.


## Installation PiGlow<br>
Zuerst PiGlow installieren<br>
<code>sudo apt install python3 -y</code>

Als nächstes muss man ein Python Script erstellen<br>
<code>touch (name ds Scripts)</code>

In die eben erstellte Datei mit der vorinstallierten  Software Geany wechseln und den Code anpassen<br>
<code>geany (name der Datei)</code>

Mit den folgenden Codes kann man die einzelnen lichter steuern und verändern.<br>
<code>import time abfolgen hinzufügen</code>
<code>import piglow importiert das vorhin installierte
PiGlow Module </code> <br>
<code>piglow.set(0, 255) Für die Helligkeit</code>
<code>piglow.set([1,3,5,7,9,11,13,15,17],255) Helligkeit für alle LEDS verändern</code><br>
<code>piglow.all(#Wert) Alle Lampen steuern</code>
<code>piglow.show() </code>
<code>time.sleep(#WERT) Zeitspanne zwischen abfolgen</code>

![Bild](/Bilder/Adressing.jpg)

**Aufgabe: Alle LEDS von 1 bis 18 müssen nacheinander aufleuchten, zusätzlich müssen die LEDS immer heller werden.**



## PiGlow installation (Nur für Lehrer)<br>

Im Webmin Browserfenster können unter dem Punkt «Webmin
Configuration» und dann «Webmin Modules» weiter Module installiert werden.

Mit den drei Punkten auf der rechten Seite können zusätzliche Module installiert werden.<br>
![Bild](/Bilder/webmin_additionally_modules.png)

Wähle das "useradmin" Modul an und gehe unten links auf "Install"<br>
![Bild](/Bilder/install_useradmin.png)

Unter Standard module sollte nun "useradmin" stehen. Anschliessend kann auf "Install Module" geklickt werden.<br>
![Bild](/Bilder/install_module.png)

Im Hauptmenu auf "System" und dann auf "User and Groups". In diesem Menu können nun neue User erstellt werden.<br>
![Bild](/Bilder/create_user.png)

## Admin User Erstellen<br>

Weiter unten bei "Group Membership" kann der User noch in die Admin Gruppe genommen werden, damit dieser auch Admin Rechte hat.<br>
![Bild](/Bilder/group_membership.png)
Zum Schluss ganz unten noch auf "create" klicken.

Anschliessend sieht man den erstellten Benutzer in der Liste<br>
![Bild](/Bilder/created_user.png)

## User erstellen<br>

Hier wird noch ein normaler User Account erstellt.<br>
![Bild](/Bilder/create_user_account.png)

Diesen User einfach in der Gruppe "Users" lassen.<br>
![Bild](/Bilder/group_membership2.png)

## Admin User deaktivieren<br>
Falls der Admin deaktiviert werden soll, kann einfach der Admin Account ausgewählt und auf "Disable selected" geklickt werden.<br>
![Bild](/Bilder/admin_user_deactivate.png)

In der Benutzerliste wird der deaktiviert Account jetzt Kursiv angezeigt.<br>
![Bild](/Bilder/disabled.png)



# 5. Qualitaetskontrolle
Folgende Commands können ausgeführt werden um zu testen, ob alles richtig funktioniert.

**Status von Webmin überprüfen:**<br>
<code>sudo service webmin </code>   

**Webmin re/starten:**<br>
<code>sudo /etc/webmin/start</code>

**sudo service:**<br>
<code>webmin restart</code>

**Webmin stoppen:**<br>
<code>sudo service webmin stop</code>

**Konfiguration überprüfen:**<br>
<code>cd /etc/webmin (Ordner von config files)</code>


# 6. Error-Handling 

Wir hatten bei der Installation von Webmin keine grösseren Probleme.


# 7. Quellen
Anleitung Installation Webmin
https://bscw.tbz.ch/bscw/bscw.cgi/31513531?op=preview&back_url=27527809

RaspberryPI OS
https://www.raspberrypi.org/software/

Markdown code Tag
https://www.w3schools.com/tags/tag_code.asp

# 8. OpenSource Lizenz

<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/3.0/ch/"><img alt="Creative Commons Lizenzvertrag" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/3.0/ch/88x31.png" /></a><br />Dieses Werk ist lizenziert unter einer <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/3.0/ch/">Creative Commons Namensnennung - Nicht-kommerziell - Weitergabe unter gleichen Bedingungen 3.0 Schweiz Lizenz</a>

 