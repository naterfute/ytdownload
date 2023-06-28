import PySimpleGUI as sg
import tkinter
from pathlib import Path
from ytdl.gui_variables import youtube, AUDIO, VIDEO

#! Start of the gui
youtube_check_list = [
  'https://youtube.com',
  'youtube.com',
  'youtu.be'
                      
]
def check_link(list1):
  '''Check if the provided List has a youtube link in it'''
  if list1 in youtube_check_list:
     print(list1)
     return list1
  else:
    print(list1)
    raise KeyError('Something broke')
def popup_text(filename, text):
  layout = [
      [sg.Multiline(text, size=(80, 25)),],
  ]
  win = sg.Window(filename, layout, modal=True, finalize=True)
  
  while True:
      event, values = win.read()
      if event == sg.WINDOW_CLOSED:
          break
  win.close()

background_color='#ffffff'
menu_def = [
  ['Config', ['config.yml']],
  ['Help', ['About...', 'Update']]
]
layout = [
  [sg.Menu(menu_def, pad=(30,30))],
  [sg.Text('YoutubeLink:'), sg.InputText(do_not_clear=False), sg.OptionMenu(values=['.mp3', '.mp4'], default_value='.mp3')],
  [sg.Button('DOWNLOAD'), sg.Button('CANCEL')],
]

window = sg.Window('Youtube Downloader Beta-V1.0', layout, size=[500, 100], element_justification='c')

while True:
  event, values = window.read()
  print(event)
  if event == 'CANCEL' or event == sg.WIN_CLOSED:
    break
  if event == 'DOWNLOAD':
    list = []
    list.append(f'{values[1]}')
    if values[2] == '.mp3':
      check_link(list[0])
      youtube.download(AUDIO.MP3, list[0])
    elif values[2] == '.mp4':
      check_link(list[0])
      youtube.download(VIDEO.MP4, list[0])
  if event == 'config.yml':
    filename = f'ytdl/config.yml'
    if Path(filename).is_file():
      try:
          with open(filename, "rt", encoding='utf-8') as f:
              text = f.read()
          popup_text(filename, text)
      except Exception as e:
          print("Error: ", e)

      
      