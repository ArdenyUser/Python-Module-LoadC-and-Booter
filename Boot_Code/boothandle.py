import PySimpleGUI as sg
layout = [[sg.Text("Complete LoadX boot?")], [sg.Button("OK")]]
# Create the window
window = sg.Window("LoadX Boot", layout)
# Create an event loop
while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the OK button
    if event == "OK" or event == sg.WIN_CLOSED:
        import cksum
        import loadx
        import game_boot
        break

window.close()

