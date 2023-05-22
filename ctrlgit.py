import PySimpleGUI as sg

def _onKeyRelease(event):
    ctrl  = (event.state & 0x4) != 0
    if event.keycode==88 and  ctrl and event.keysym.lower() != "x":
        event.widget.event_generate("<<Cut>>")

    if event.keycode==86 and  ctrl and event.keysym.lower() != "v":
        event.widget.event_generate("<<Paste>>")

    if event.keycode==67 and  ctrl and event.keysym.lower() != "c":
        event.widget.event_generate("<<Copy>>")

font = ("Courier New", 16)
sg.theme('DarkBlue3')
sg.set_options(font=font)

layout = [
    [sg.Input(expand_x=True)],
    [sg.Multiline()],
]

window = sg.Window("Title", layout, finalize=True)
window.TKroot.bind_all("<Key>", _onKeyRelease, "+")

window.read(close=True)