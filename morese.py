from pynput import keyboard
from datetime import datetime
import threading
import csv
start = 0
end = 0
released = True

final = [-1,-1,-1,-1]
finished = False
i = 0
def on_press(key):
    global start, released, end
    if key == keyboard.Key.space and released:
        start = datetime.now()
        released = False
        end = 0
def on_release(key):
    global start, end, released, final, i
    if key == keyboard.Key.space and i < 4:
        end = datetime.now()
        released = True
        final[i] = (end-start).total_seconds()
        i+=1
    if i >= 4 and not finished:
        finish()
        return
def check_finish():
    global end, finished
    while True:
        try:
            if (datetime.now() - end).total_seconds() > 1 and not finished:
                finish()
        except:
            continue
def finish():
    global final, finished
    print(final)
    finished = True
    expected = (input("What letter?")).lower()
    jsonData = {
        "input": final,
        "expected": 
        ord(expected)-97
    }
    file = open("trainingdata.csv", "a")
    writer = csv.writer(file)
    writer.writerow(jsonData.values())
    file.close()
    get_morsin()
def get_morsin():
    global start,end,released,final,finished,i
    start = 0
    end = 0
    released = True

    final = [-1,-1,-1,-1]
    finished = False
    i = 0
get_morsin()
threading.Thread(target = check_finish).start()
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()