import PySimpleGUI as sg
import sqlite3

connection = sqlite3.connect("UserInfoTest.db")
c = connection.execute("Select * from SignUp")

sg.theme("BlueMono")


def newwindow():
    signpage = [
        [sg.Text("Username"), sg.InputText(key='-USERNEW-')],
        [sg.Text("Email"), sg.InputText(key='-EMAIL-')],
        [sg.Text("Password"), sg.InputText(key='-PASSNEW-')],
        [sg.Text("Confirm Password"), sg.InputText(key='-REPASSNEW-')],
        [sg.Button("Cancel",expand_x=True),sg.Button("Sign Up",expand_x=True)]
    ]

    newwin= sg.Window("Sign Up form", signpage)

    while True:
        event, values = newwin.read()
        if event == sg.WIN_CLOSED or event == 'Cancel':
            break
        if event == "Sign Up":
            myuser = values['-USERNEW-']
            mypassword = values['-PASSNEW-']
            remypassword = values['-REPASSNEW-']
            myemail = values['-EMAIL-']
            try:
                if (mypassword) and mypassword==remypassword:
                    connection.execute("Insert into SignUp(Username,Password,Email) values(?,?,?)",(myuser,mypassword,myemail))
                    connection.commit()
                    sg.popup("Data inserted")
            except Exception as e:
                print("Error",e)
    connection.close()

    newwin.close()

def loginpage():
    rows = c.fetchall()

    layout1 = [
        [sg.Table(values="", headings=['Username', 'Password', 'Email'], max_col_width=25,
                  auto_size_columns=True, justification='center', num_rows=5)],
        [sg.Button("Display")]]

    layout2 = [
        [sg.Table(values=rows, headings=['Username', 'Password', 'Email'], max_col_width=25,
                  auto_size_columns=True, justification='center', num_rows=5)],
        [sg.Button("Display")]
    ]

    window = sg.Window('Home Page', layout1)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        if event == 'Display':
            window = sg.Window('Home Page', layout2)

    window.close()
    connection.close()



def mainwindow():
    flag = False

    layout = [
        [sg.Text("Username"), sg.InputText(key='-USERNAME-')],
        [sg.Text("Password"), sg.InputText(key='-PASSWORD-')],
        [sg.Button("Login",expand_x=1)],
        [sg.Button("Go to Sign Up", expand_x=20), sg.Button("Cancel",expand_x=20)]
    ]

    win = sg.Window("Login Form", layout)

    while True:
        event, values = win.read()
        if event == sg.WIN_CLOSED or event == 'Cancel':
            break
        if event == "Go to Sign Up":
            newwindow()
        if event == "Login":
            try:
                alldatadb = connection.execute("select Username, Password from SignUp")
                loginname = values['-USERNAME-']
                loginpass = values['-PASSWORD-']

                for eachrow in alldatadb:
                    if loginname == eachrow[0] and loginpass == eachrow[1]:
                        flag = True
                        loginpage()
                if flag == False:
                    sg.popup("Error: Check Username or Password.")
                    break

            except Exception as e:
                print(f"Error in sql: {e}")

    win.close()
mainwindow()

