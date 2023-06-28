import PySimpleGUI as ps

ps.theme('LightBlue7')

layout=[ [ps.Text('Enter Your Username:'), ps.InputText()],
        [ps.Text('Enter Your Password:'), ps.InputText()],
        [ps.Button('Register'), ps.Button('Cancel')]]

window=ps.Window('Login Page', layout)

while True:
    event, values=window.read()
    if event == ps.WIN_CLOSED or event == 'Cancel':
        break
    print('You Have Entered Username as:', values[0],'\nYou have Entered Password as:', values[1])