import PySimpleGUI as sg
import sqlite3
import matplotlib.pyplot as plt


connection = sqlite3.connect("records.db")
c = connection.execute("Select * from Marks")

sg.set_options(font=("Times", 16), text_color='black')
sg.theme("BlueMono")


def Datapage():
    rows = c.fetchall()

    headings = ['ID', 'NAME', 'MARKS IN SCIENCE', 'MARKS IN MATHS', 'MARKS IN ENGLISH','TOTAL x/300','PERCENTAGE']

    layout_for_display = [
        [sg.Table(values=rows,
                  headings=headings,
                  max_col_width=35,
                  auto_size_columns=True,
                  justification='left',
                  num_rows=10,
                  key="STUDENTTABLE",
                  row_height=60,
                  enable_events=True,
                  tooltip='All Students results')]
    ]

    windr = sg.Window("Data",layout_for_display)

    while True:
        event,values = windr.read()
        if event == sg.WIN_CLOSED:
            break
def Bar():
    datastore = []
    forgraph = connection.execute("Select Percentage from Marks")
    percentagess = forgraph.fetchall()
    for eachvalue in percentagess:
        datastore.append(eachvalue[0])

    data = {'Suhrid': datastore[0], 'Purnika': datastore[1],'Lubin': datastore[2],
            'Suprit': datastore[3],'Saanvi': datastore[4],'Johnny': datastore[5],'Polnareff': datastore[6]}

    courses = list(data.keys())
    valuesss = list(data.values())

    fig = plt.figure(figsize=(10, 5))

    plt.bar(courses, valuesss, color='teal', width=0.4)

    plt.xlabel("Student Roll Number")
    plt.ylabel("Percentage Across 3 Courses")
    plt.title("Percentage of Each student")
    plt.show()

def scattergraph():
    datagain = []
    forgrh = connection.execute("Select Percentage from Marks")
    percentag = forgrh.fetchall()
    for eachvalue in percentag:
        datagain.append(eachvalue[0])
    xaxis = ["Suhrid","Purnika","Lubin","Suprit","Saanvi","Johnny","Polnareff"]
    yaxis = [datagain[0],datagain[1],datagain[2],datagain[3],datagain[4],datagain[5],datagain[6]]

    plt.scatter(xaxis,yaxis,c="teal")
    plt.show()

def Graphoptions():

    laysy = [[sg.Button("Bar Graph")],
             [sg.Button("Line Graph")],
             [sg.Button("Scatter Plot")]
             ]
    powindow = sg.Window("Graphs",laysy)

    while True:
        event,values = powindow.read()
        if event == sg.WIN_CLOSED:
            break
        if event == "Bar Graph":
            Bar()
        if event == "Line Graph":
            import LineGraph
        if event == "Scatter Plot":
            scattergraph()


def mainwindow():

    layout = [
        [sg.Text("Student ID"), sg.Push(), sg.Combo(size=(30,3),values=['1',"2","3",'4','5','6','7','8','9','10'],key='STUID')],
        [sg.Text("Student Name"), sg.Push(), sg.InputText(key='STUNAME')],
        [sg.Text("Science Marks"), sg.Push(), sg.InputText(key='SCIKEY')],
        [sg.Text("Maths Marks"), sg.Push(), sg.InputText(key='MATHKEY')],
        [sg.Text("English Marks"), sg.Push(), sg.InputText(key='ENGKEY')],
        [sg.Button("Insert",expand_x=True)],
        [sg.Button("View Graphs", expand_x=True), sg.Button("View Data",expand_x=True),sg.Button("Clear",expand_x=True)]
    ]

    window = sg.Window("Login Form", layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        if event == "Insert":
            ids = values['STUID']
            names = values['STUNAME']
            scimark = values['SCIKEY']
            mathmark = values['MATHKEY']
            engmark = values['ENGKEY']
            total = int(scimark)+int(mathmark)+int(engmark)
            percent = (total/300) * 100
            try:
                connection.execute("Insert into Marks(Stu_ID,Stu_Name,Science,Maths,English,Total,Percentage) values(?,?,?,?,?,?,?)",
                                   (ids, names, scimark,mathmark,engmark,total,percent))
                connection.commit()
                sg.popup("Data inserted")
            except Exception as e:
                sg.popup("Error")
                print("Error:",e)
        if event == "View Data":
            Datapage()
        if event == "View Graphs":
            Graphoptions()
        if event == "Clear":
            for key in values:
                window['STUID'].update('')
                window['STUNAME'].update('')
                window['SCIKEY'].update('')
                window['MATHKEY'].update('')
                window['ENGKEY'].update('')

mainwindow()
connection.close()
