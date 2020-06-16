"""User Interface for Geccoi Management"""
import os, sys
import PySimpleGUI as sg


import PySimpleGUI as sg
import tkinter


sg.LOOK_AND_FEEL_TABLE["Geccoi"] = {
    'BACKGROUND': '#757575',
    'TEXT': '#74c93a',
    'INPUT': '#DDE0DE',
    'SCROLL': '#58ad1f',
    'TEXT_INPUT': '#8ced4a',
    'BUTTON': ('white', '#6D9F85'),
    'PROGRESS': sg.DEFAULT_PROGRESS_BAR_COLOR,
    'BORDER': 0,
    'SLIDER_DEPTH': 2,
    'PROGRESS_DEPTH': 0
}

sg.theme("Geccoi")

layout = [
    [sg.Text(" "*100), sg.Button("Exit", button_color=("#e00000", sg.DEFAULT_BACKGROUND_COLOR), size=(6,1))],
    [sg.Text("_"*80, font="Courier 15 bold")],
    [sg.Text(" "), sg.Text("GeCCOI Manager", font="Courier 30 bold")],
    [sg.Text("")],
    [sg.Text(" "*12), sg.Text("            "), sg.Text("        "), sg.Button("Start", font="Courier 15", button_color=("white", "#07c700"), size=(12, 1), key="-S/S-")],
    [sg.Text("")],
    [sg.Text(" "*8), sg.Text('Settings', font="Courier 24 bold")],
    # Rest of the toggleable settings.
    [sg.Text(" "*16), sg.Text("General:", font="Courier 16 bold")],
    [sg.Text("")],
    [sg.Text(" "*16), sg.Text("Keyboard:", font="Courier 16 bold")],
    [sg.Text("")],
    [sg.Text(" "*16), sg.Text("Mouse:", font="Courier 16 bold")],
    [sg.Text("")]
]

# Get Display Resolution.
root = tkinter.Tk()
root.withdraw()
display_width, display_height = root.winfo_screenwidth(), root.winfo_screenheight()

window = sg.Window('GeCCOI Manager', layout, size=(500, display_height), no_titlebar=True)


while True:
    event, values = window.read()
    print(event, values)

    if event == "-S/S-":
        if window["-S/S-"].get_text() == "Start":
            window["-S/S-"]("Stop", button_color=("white", "red"))
        else:
            window["-S/S-"]("Start", button_color=("white", "#07c700"))

        # process_handler.gesture_recog.toggle("on")

    if event in (None, "Exit"):
        break

window.close()


    
