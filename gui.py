# import PySimpleGUI as sg
# import overthinker



# sg.theme('DarkGreen5')
# fileName = sg.popup_get_file('Choose file:')
# result = overthinker.main(fileName)
# if not result == "Invalid file." and not result == "Improperly formatted chat log.":
#     # layout = [ [result["textFirst"]],
#     #            [result["textLast"]],
#     #            [result["responseTimes"]],
#     #            [sg.Text('_'  * 100, size=(65, 1))],
#     #            [result["charactersPerBlock"]],
#     #            [result["totalCharacters"]]
#     #          ]
#     # window = sg.Window('Results', layout)
#     info = []
#     chatters = list(result["textFirst"].keys())
#     heading = ["Statistics"] + chatters
#     for statistic in result:
#         newStat = [statistic]
#         for chatter in chatters:
#             newStat.append(result[statistic][chatter])
#         info.append(newStat)
    
#     layout = [[sg.Table(values=info, headings=heading, alternating_row_color='#77A16B')]]
#     window = sg.Window("Result", layout)
#     while True:
#         event, values = window.read()
#         if event == sg.WIN_CLOSED:
#             break
    
# #Maybe the program crashes if any of the statistics don't have a value.
# #So particularly lonely people might have the program crash on them
# else:
#     sg.popup('Error', result)





import PySimpleGUI as sg
import overthinker

sg.theme("DarkGreen5")  # please make your windows colorful

layout = [[sg.Text('Choose JSON Chat Log File')],
          [sg.Input(), sg.FileBrowse(file_types=(("JSON Files", ".json"),))],
          [sg.OK()]
         ]

window = sg.Window('Overthinker', layout)
event, values = window.read()

if event == "OK":
    result = overthinker.main(values[0])
    if not result == "Invalid file." and not result == "Improperly formatted chat log.":
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