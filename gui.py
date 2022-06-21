import PySimpleGUI as sg
import overthinker

sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('Choose file:'), sg.FileBrowse()],
            [sg.Button('Run')]
         ]

# Create the Window
window = sg.Window('Window Title', layout)
event, values = window.read()
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED: # if user closes window
        break
    elif event == 'Run':
        result = overthinker.main(values['Browse'])
        sg.popup(result["textFirst"],
        result["textLast"],
        result["responseTimes"],
        result["charactersPerBlock"],
        result["totalCharacters"])

window.close()