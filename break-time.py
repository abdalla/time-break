import webbrowser
import time

REPTIME = 3
count = 0

print('Break time is running - '+ time.ctime())
while (count < REPTIME):
    time.sleep(10);
    webbrowser.open("http://www.youtube.com/watch?v=dQw4w9WgXcQ")
    count = count + 1