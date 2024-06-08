import PySimpleGUI as sg
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import sqlite3

percentscore = []

conn = sqlite3.connect('records.db')
forgraph = conn.execute("Select Percentage from Marks")
percentageslol = forgraph.fetchall()
for eachvalue in percentageslol:
    percentscore.append(eachvalue[0])


studentName = ["Suhrid","Purnika","Lubin","Suprit","Saanvi","Johnny","Polnareff"]

def create_plot(studentName, percentscore):
    plt.plot(studentName,percentscore,color="teal", marker = 'o')
    plt.title("Percent vs Student", fontsize = 14)
    plt.xlabel('Student Name',fontsize = 14)
    plt.ylabel('Percentage Score',fontsize = 14)
    plt.grid(True)
    return plt.gcf()

layout = [
    [sg.Text("Line plot")],
    [sg.Canvas(size=(1000,1000), key='CANVAS')],
    [sg.Exit()]
]

def draw_figure(canvas, figure):
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side='top',fill='both',expand=1)
    return figure_canvas_agg

linewindow = sg.Window("PySimpleGUI + MatPlotLip Line Plot",layout,finalize=True,element_justification='center')

draw_figure(linewindow['CANVAS'].TKCanvas,create_plot(studentName,percentscore))

while True:
    event, values = linewindow.read()
    if event == sg.WIN_CLOSED or event == "Exit":
        break

conn.close()
linewindow.close()

