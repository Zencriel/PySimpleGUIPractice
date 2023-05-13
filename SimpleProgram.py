import PySimpleGUI as sg

sg.theme("GreenMono")

layout = [
    [sg.Text("Enter your name")],
    [sg.InputText()],
    [sg.Ok(), sg.Cancel()]
]

win = sg.Window("Form",layout)

while True:
    event, values = win.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break
    print('You entered ', values[0])

win.close()
