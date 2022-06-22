import PySimpleGUI as sg
import overthinker

fileName = sg.popup_get_file('Choose file:')
result = overthinker.main(fileName)
if not result == "Invalid file." and not result == "Improperly formatted chat log.":
    sg.popup('Results', result["textFirst"],
            result["textLast"],
            result["responseTimes"],
            sg.Text('_'  * 100, size=(65, 1)),
            result["charactersPerBlock"],
            result["totalCharacters"])
else:
    sg.popup('Error', result)

# sg.popup('Results', 'The value returned from popup_get_file', text)
# sg.theme('DarkAmber')   # Add a touch of color
# # All the stuff inside your window.
# layout = [  [sg.Text('Choose file:'), sg.FileBrowse()],
#             [sg.Button('Run')]
#          ]

# # Create the Window
# window = sg.Window('Window Title', layout)
# event, values = window.read()
# # Event Loop to process "events" and get the "values" of the inputs
# while True:
#     event, values = window.read()
#     if event == sg.WIN_CLOSED: # if user closes window
#         break
#     if event == 'Run':
#         result = overthinker.main(values['Browse'])
#         sg.popup('Results', result["textFirst"],
#         result["textLast"],
#         result["responseTimes"],
#         result["charactersPerBlock"],
#         result["totalCharacters"])

# window.close()