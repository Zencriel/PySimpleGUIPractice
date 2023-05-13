import PySimpleGUI as sg
import math

sg.theme("GreenMono")

clearkeys=['-FIRSTNUM-','-SECONDNUM-','-RESULT-']

layout = [
    [sg.Text("Enter first number"),sg.Input(key= '-FIRSTNUM-')],
    [sg.Text("Enter second number"),sg.Input(key= '-SECONDNUM-')],
    [sg.Text("Your result is"), sg.Input(key='-RESULT-')],
    [sg.Button("Add"), sg.Button("Subtract"), sg.Button("Multiply")],
    [sg.Button("Divide"), sg.Button("Square"), sg.Button("Square Root")],
    [sg.Button("Clear")]
]

win = sg.Window("Calculator",layout)

while True:
    event, values = win.read()
    if event == sg.WIN_CLOSED:
        break
    if event == "Add":
        sum = int(values['-FIRSTNUM-']) + int(values['-SECONDNUM-'])
        win['-RESULT-'].update(sum)
    if event == "Subtract":
        subt = int(values['-FIRSTNUM-']) - int(values['-SECONDNUM-'])
        win['-RESULT-'].update(subt)
    if event == "Multiply":
        mult = int(values['-FIRSTNUM-']) * int(values['-SECONDNUM-'])
        win['-RESULT-'].update(mult)
    if event == "Divide":
        divi = int(values['-FIRSTNUM-']) / int(values['-SECONDNUM-'])
        win['-RESULT-'].update(divi)
    if event == "Square":
        square = int(values['-FIRSTNUM-']) * int(values['-FIRSTNUM-'])
        win['-RESULT-'].update(square)
    if event == "Square Root":
        sqrt = math.sqrt(int(values['-FIRSTNUM-']))
        win['-RESULT-'].update(sqrt)
    if event == "Clear":
        for key in clearkeys:
            win[key]('')

win.close()
