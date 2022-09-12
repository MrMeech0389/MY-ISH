import tkinter

wn = tkinter.Tk()


def down(e):
    print('Down\n', e.char, '\n', e)

def up(e):
    print('Up\n', e.char, '\n', e)

down_key = wn.bind('<KeyPress>', down)
up_key = wn.bind('<KeyRelease>', up)

if down_key:
    print("you bitch")
elif up_key:
    print()


wn.mainloop()
