from ntpath import join
import random
import PySimpleGUI as ps

num="0123456789"
let="abcdefghijklmnopqrstuvwxyz"
up_let="ABCDEFGHIJKLMNOPQRSTUWXYZ"
syms="!~@#$%^&*()"
pass0=let+up_let+syms+num

password="".join(random.sample(pass0,10))

ps.theme('LightBlue7')

layout=[ [ps.Text('Enter Your Username:'), ps.InputText()],
        [ps.Text('Enter Your Password:'), ps.InputText()],
        [ps.Text('Suggested Password is:'),ps.Text(password)],
        [ps.Button('Register'), ps.Button('Cancel'),ps.Button('Use Suggested Password')]]
window=ps.Window('Login Page', layout)

while True:
    event, values=window.read()
    if event == ps.WIN_CLOSED or event == 'Cancel':
        break
    if event == 'Use Suggested Password':
        values[1]=password
    if event == 'Register' and values[1] == '' :
        values[1]=password
        print('You Have Entered Username as:', values[0],'\nYou have Entered Password as:', values[1])