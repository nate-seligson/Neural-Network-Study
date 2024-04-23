import simple
import usenetwork

simple.train(simple.mydata)
print("Training complete!")

usenetwork.get_morsin()
usenetwork.threading.Thread(target = usenetwork.check_finish).start()
with usenetwork.keyboard.Listener(
        on_press=usenetwork.on_press,
        on_release=usenetwork.on_release) as listener:
    listener.join()