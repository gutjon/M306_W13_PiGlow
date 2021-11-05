
import time #importiert das Modul time, wird benötigt für kurze Pausen im Script


import piglow #importiert das PiGlow Modul

i = 0 #Setzt die Variabel "i" auf den Wert "0"

while True: #Schleife wird solange ausgeführt bis das Script abgebrochen wird
  print(i) #Gibt den Wert der Variabel "i" aus
  piglow.all(0) #Setzt alle LED's auf den Wert "0" (aus)
  piglow.set(i % 18, 1) #Schaltet die LED mit dem Wert (i % 18) ein und mit der Helligkeit "1"
  piglow.show() #Die LED's aktualisieren ihren Wert
  i += 1 #Die Variabel "i" wird um den Wert "1" grösser
  time.sleep(0.1) #Das Script wird für 0.1 Sekunden pausiert, damit das LED Muster zu erkennen ist