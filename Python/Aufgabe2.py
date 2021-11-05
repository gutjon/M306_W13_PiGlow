
import time


import piglow

i = 0 

while True: 
  print(i) 
  piglow.all(0) 
  piglow.set(i % 18, i) #Durch das ändern auf den WERT "i" werden die LED's nach jedem Durchgang der Schleife heller bis sie den Wert 255 erreichen
  piglow.show() 
  i += 1 
  time.sleep(0.1) 