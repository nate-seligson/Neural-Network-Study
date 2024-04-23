from pynput import keyboard
from datetime import datetime
import threading
import simple
import numpy as np
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
    get = simple.forward_prop(np.array(final), simple.w1, simple.b1, simple.w2, simple.b2)
    print(simple.toLetter(get), str(int(np.amax(get) * 100)) + "%")
    finished = True
    get_morsin()
def get_morsin():
    global start,end,released,final,finished, i
    start = 0
    end = 0
    released = True

    final = [-1,-1,-1,-1]
    finished = False
    i = 0
