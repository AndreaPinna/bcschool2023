# Andrea Pinna - Università di Cagliari
# Blockchain School 2023
# AA 2022-23
# CC-BY

# Simple user interface

import PySimpleGUI as sg

import datetime
import userApp

text_data = "Data: {} -  Timestamp: {}"
text_hash = "TX hash: {}"

layout = [
    [sg.Button("GET DATA")],
    [sg.Text(text_data, key = ('-VALUES-'))],
    [sg.Button("REQUEST UPDATE"), sg.Text("", key = ('-WAIT-'))],
    [sg.Text(text_hash, key = ('-HASH-'))],

    ]


# Create the window
window = sg.Window("My dAPP", layout, size=(500,150))

# Create an event loop
while True:
    event, values = window.read()
    if event == "GET DATA":
        #get from SC
        result = userApp.get()
        #timestamp to iso:
        result[1]=datetime.datetime.fromtimestamp(result[1]).isoformat()
        window["-VALUES-"].update(text_data.format(result[0],result[1]))

    if event == "REQUEST UPDATE":
        #emit request to SC
        tx_hash = userApp.request()
        window["-HASH-"].update(text_hash.format(str(tx_hash)))

    if event == sg.WIN_CLOSED:
        break

window.close()
