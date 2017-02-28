import webbrowser
import time

REPTIME = 3
count = 0

print('Break time is running - '+ time.ctime())
while (count < REPTIME):
    time.sleep(10);
    webbrowser.open("https://youtu.be/44LdLqgOpjo")
    count = count + 1