from ntpath import join
import random
from tkinter import Label
num="0123456789"
let="abcdefghijklmnopqrstuvwxyz"
up_let="ABCDEFGHIJKLMNOPQRSTUWXYZ"
syms="!~@#$%^&*()"
pass0=let+up_let+syms+num

password="".join(random.sample(pass0,10))

print("YOUR New Password IS:"+password) 
