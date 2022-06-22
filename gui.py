import PySimpleGUI as sg
import overthinker

sg.theme("DarkGreen5")

layout = [[sg.Text('Choose chat log:')],
          [sg.Input(), sg.FileBrowse(file_types=(("JSON Files", ".json"),))],
          [sg.Text('Time (in hours) until new conversation:'), sg.Input(size=(5, 1))],
          [sg.OK()]
         ]

window = sg.Window('Overthinker', layout)
event, values = window.read()

if event == "OK":
    result = overthinker.main(values[0], values[1])
    if not type(result) == str: #If not error
        info = []
        chatters = list(result["textFirst"].keys())
        heading = ["Statistics"] + chatters
        for statistic in result:
            newStat = [statistic]
            for chatter in chatters:
                newStat.append(result[statistic][chatter])
            info.append(newStat)
        
        layout = [[sg.Table(values=info, headings=heading, alternating_row_color='#77A16B')]]
        window = sg.Window("Result", layout)
        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED:
                break
        
    #Maybe the program crashes if any of the statistics don't have a value.
    #So particularly lonely people might have the program crash on them
    else:
        sg.popup('Error', result)