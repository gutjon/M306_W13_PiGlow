
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
   ## Beschreibung 
   Der PiGlow bietet 18 integrierte LED's mit unterschiedlicher Farben. Diese LED's können relativ simple gesteuert, verwaltet und ein-/ ausgeschalten werden. Zusätzlich kann man die Farben-Kombinationen steuern. Man kann es auch soweit benützen, dass die Lampen leuchten, wenn man eine Aktion ausführt. <br>
  
   ## Zeitaufwand
   Die Installation von PiGlow (Werkstatt Auftrag 13) ist bis am 02:11.2021 um 12:00 abgeschlossen.<br>
  
  ## Einleitung
  Mit dem GlowPi Module kann man verschiedenste Lämpchen mit einem Python Script ansteuern und konfigurieren. Durch dieses Script können die Lämpchen an- und ausgeschaltet werden und man kann individuelle Muster mit diesen LED's erstellen ohne Grenzen zu haben. <br>

  ## Stolpersteine & Kniffe
   Die Programmiersprache von dem GlowPi ist Python, da wir noch nie mit Python programmiert haben, musste wir uns Zeit nehmen die essentielle commands von Python zu lernen. Zusätzlich mussten wir die Dokumentation von GlowPI genauer anschauen, um zu verstehen, wie diese einzelnen Lampen angesteuert werden können.<br>
   Dokumentation GlowPI: https://github.com/pimoroni/piglow


# 3. Benoetigte Hard- und Software
  ## Hardware Materialliste
  1x RaspberryPI v4 (inkl. Stromkabel)<br>
  1x PiGlow<br>
  1x HDMI zu DVI Adapter<br>
  1x HDMI zu miniHDMI Adapter<br>
  1x Externer Bildschirm<br>
  1x Tastatur<br>
  1x Maus<br>

  ## Software Anforderungen<br>
   1x RaspberryPI Linux Image<br>


# 4. Installationsanleitung
   ## GlowPI einstecken
   Wir empfehlen beim Nutzen des GlowPI's den GrovePI zu entfernen und ihn direkt auf die GPIO-PIN's zu setzten.<br>
   ![Bild](/Bilder/GlowPI_installation.jpg)<br>

   ## Vorbereitung Raspberry
   Auf dem RaspberryPI WLAN einrichten.<br>
 
   RaspberryPI Updates<br> 
   <code>sudo apt update </code>

   RaspberryPI upgrade <br>
   <code>sudo apt upgrade </code><br>

## Installation PiGlow
   PiGlow installieren:<br>
   <code>sudo apt-get install python3-piglow</code>

   Python installieren:<br>
   <code>sudo apt install python3 -y</code>

   Python Script erstellen:<br>
   <code>touch python_script.py</code>

   Das Python Script mit Geany öffnen: (Vorinstalliertes Tool zum bearbeiten von Python Scripts) <br>
   <code>geany python_script.py</code>

## Basic GlowPI Commands<br>
   Mit den folgenden Codes kann man die einzelnen LED's steuern und verändern:<br>
   <code>import piglow</code> importiert das vorhin installierte PiGlow Module  <br>
   <code>piglow.all(0)</code> Setzt alle LED's auf den Wert 0 (aus)<br>
   <br>
   <code>piglow.set([LED-Nummer],Helligkeit)</code>Bestimmte LED's ansteuern und Helligkeit ändern<br>
   LED-Nummer: 1 - 18<br>
   Helligkeit: 0-225<br>
   Beispiel:<br>
   <code>piglow.set([1, 2],255)</code>LED 1 und 2 leuchten mit der Helligkeit 255<br>
   <code>piglow.show()</code> Erst nach diesem Befehl werden die Werte auf den GlowPI übertragen.<br>

   ![Bild](/Bilder/Adressing.jpg)

## Aufgaben:
   **Aufgabe 1: Alle LEDS von 1 bis 18 müssen nacheinander aufleuchten.**<br>
   **Tipp:** Verwende eine While Schlaufe und nutze eine Variabel, welche bei jedem Durchgang um den Wert 1 erhöht wird. Dadurch kann nach jedem Durchgang die nächste LED angesteuert werden.

   Falls Probleme oder unklarheiten auftauchen schaue dir folgende Beispiele von GlowPI Python Scripts an:<br>
   https://github.com/pimoroni/piglow/tree/master/examples

**Aufgabe 2: Bei jedem Wechsel der LED's soll die Helligkeit erhöht werden.**<br>
   Tipp:<br>
   <code>piglow.set([LED-Nummer],Helligkeit)</code>


## Lösungen<br>
   **Aufgabe 1:**<br>
   https://github.com/gutjon/M306_W13_PiGlow/blob/main/Python/Aufgabe1.py

   **Aufgabe 2:**<br>
   https://github.com/gutjon/M306_W13_PiGlow/blob/main/Python/Aufgabe2.py

## Live Demo
<a href="https://github.com/gutjon/M306_W13_PiGlow/blob/main/livedemo/video0.mov" title="Demo zur PiGlow">Demo zur PiGlow</a>

# 5. Qualitaetskontrolle
   Um zu überprüfen, ob das Python Script funktioniert, führe das Script aus und überprüfe, ob die LED's wie geplant aufleuchten.
   Wir empfehlen, immer bevor man das Script ausführt zu vermuten, was genau passieren wird. Wenn sich die Vermutung bewarheitet funktioniert das Script wie gewohlt.

# 6. Error-Handling 
   Generell hatten wir keine grössere Probleme. Jedoch haben wir viele Zeit benötigt, um die Python Befehle zu verstehen. Das Wissen haben wir uns durch Beispiel Scripts aufgebaut.<br>
   Dabei ist bei einer Aufgabe jede LED nacheinander aufgeleuchtet. Dafür wurde eine While Schlaufe verwendet und eine Variabel die bei jedem Durchgang den Wert erhöht. Da es nur 18 LED's gibt wurde im Beispiel folgender Code verwendet:<br>
   <code>piglow.set(i % 18, 1)</code>

   Zuerst haben wir nicht verstanden was diese Zeile an Code genau verursacht. Dabei ist uns aber nach einiger Zeit eingefallen, dass das "%" Zeichen in Powershell ebenfalls eine bedeutung hat. In Powershell wird durch das "%" Zeichen bei einer Divisions Rechnung den Restwert Berechnet. <br>
   Hilfreicher Link:<br>
   https://www.gut-erklaert.de/mathematik/division-mit-rest.html

   Nach dieser Erkenntnis haben hat die obere Zeile Code auch Sinn gemacht. Der Wert der Variabel "i" steigt bei jedem Durchgang der While Schlaufe um den Wert "i" und wird dadurch schnell höher sein als der Wert 18 (Anzahl der LED's). Damit weiterhin die LED's 1 - 18 angesteuert werden können wird dieser <code>(i % 18)</code> angewendet, damit der Wert 18 nie überschritten wird. <br>
   Beispiel Rechnungen:<br>
   i = 19 <br>
   i % 18 = 1
   <br>
   <br>
   i = 20<br>
   i % 18 = 2
   <br>
   <br>
   i = 21<br>
   i % 18 = 3

   Falls das die Erklärung noch etwas zu kompliziert war, kann noch folgendes Python Script anlysiert werden, welches diese "%" Funktion simple anwendet:<br>
   https://github.com/gutjon/M306_W13_PiGlow/blob/main/Python/Division_mit_Rest.py<br>

# 7. Quellen
   Anleitung Installation Webmin:<br>
   https://bscw.tbz.ch/bscw/bscw.cgi/31513531?op=preview&back_url=27527809

   Anleitung Installation + Beispiele GlowPI:<br>
   https://github.com/pimoroni/piglow

   Python While Schlaufe:<br>
   https://www.sivakids.de/python-while-schleife/

   Python Modulo Operator:<br>
   https://careerkarma.com/blog/python-modulo/#:~:text=The%20Python%20modulo%20operator%20calculates,then%20the%20remainder%20is%20returned

   Division mit Restwert:<br>
   https://www.gut-erklaert.de/mathematik/division-mit-rest.html

   RaspberryPI OS:<br>
   https://www.raspberrypi.org/software/

   Markdown code Tag:<br>
   https://www.w3schools.com/tags/tag_code.asp

# 8. OpenSource Lizenz
   <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/3.0/ch/"><img alt="Creative Commons Lizenzvertrag" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/3.0/ch/88x31.png" /></a><br />Dieses Werk ist lizenziert unter einer <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/3.0/ch/">Creative Commons Namensnennung - Nicht-kommerziell - Weitergabe unter gleichen Bedingungen 3.0 Schweiz Lizenz</a>

 