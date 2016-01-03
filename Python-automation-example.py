Enter file contents here
# This Python automation program demo starts the open source Heavyload stress tool,
# lets it run for a period of time, and then, stops and closes the application.
# Rather than use the uncertain pixel locations on the display, it uses the program hotkeys instead.


#! python3

# Opens, starts, stops, then terminates the Heavyload stress tool
import os, pyautogui, subprocess, time

# Opens the Heavyload stress tool
proc1 = subprocess.Popen('C:\Program Files\JAM Software\Heavyload\HeavyLoad.exe')

# Pauses for a second
time.sleep(1) 

# Starts Heavyload
pyautogui.hotkey('alt', 'f', 's') 

# Lets Heavyload run for 15 sec.
time.sleep(15) 

# Stops Heavyload
pyautogui.hotkey('alt', 'f', 'p') 
time.sleep(3) # Pauses 3 sec.

# Closes Heavyload
proc1.terminate() 
