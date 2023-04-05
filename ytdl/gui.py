import PySimpleGUI as sg
import tkinter

from os import environ, getcwd, path
from sys import platform, exit
from pathlib import Path
import yt_dlp, math, json
import yaml
try:
  if not path.isfile(f'./config.yml'):
    with open('./config.yml', 'w') as f:
      f.write('''AUDIO:
  # Leave field blanks for the directory that your script is located
  # EXAMPLE: 
  # path: /home/user/Music/download/
  # In this example archive would go to /home/user/Music/AudioArchive.txt
  # archive: AudioArchive.txt

  path: 
  archive: 


VIDEO:
  # Leave field blanks for the directory that your script is located
  # EXAMPLE: 
  # path: /home/user/Videos/downloaded/
  # In this example archive would go to /home/user/Videos/VideoArchive.txt
  # archive: VideoArchive.txt

  path: 
  archive: 
      ''')
      raise TypeError('Please Configure You config.yaml Now')

  with open('./config.yml') as f:
    config = yaml.safe_load(f)
  Audio_File_Save = config['AUDIO']['path']
  AudioArchive = config['AUDIO']['archive']
  Video_File_Save = config['VIDEO']['path']
  VideoArchive = config['VIDEO']['archive']
  workingpath = getcwd()
  #* Classes
  class MyLogger:
    def debug(self, msg):
      if msg.startswith('[debug] '):
        pass
      else:
        self.info(msg)

    def info(self, msg):
      pass

    def warning(self, msg):
      pass

    def error(self, msg):
      print(msg)

  #* Class/Functions
  filesize = ''
  class youtube(object):
      def transfer(total_bytes_download):
        return total_bytes_download

      def title(ydl, x):
        info = ydl.extract_info(x, download=False)
        info = json.dumps(ydl.sanitize_info(info))
        json_dict = json.loads(info)
        title = json_dict.get('title')
        print(title)

      def download(ydlopts, links):
        with yt_dlp.YoutubeDL(ydlopts) as ydl:
          ydl.download([links])

      def convert_size(size_bytes):
        if not isinstance(size_bytes, (int, float)):
          raise TypeError("Input must be a numeric value")
        if size_bytes == 0:
          return "0B" 
        size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
        i = int(math.floor(math.log(size_bytes, 1024)))
        p = math.pow(1024, i)
        s = round(size_bytes / p, 2)
        return "%s %s" % (s, size_name[i])

      def hook(d):
        if d['status'] == 'finished':
          d.get('')
          print(d['filename'])
          print('Done downloading, now post-processing ...')

        if d['status'] == 'downloading':
          global currently_downloaded
          d.get('')
          currently_downloaded = d.get('downloaded_bytes')

          # print(f'{COLOR.Green}{youtube.convert_size(currently_downloaded)}{COLOR.Blue}/{COLOR.Green}{youtube.convert_size(filesize)}{COLOR.Default}')
          print(d['_percent_str'], d['_eta_str'])
          print(f'Elaspsed:')
          print(d['elapsed'])
          
  #* Multi-Line Variables
#! Must make use of this in meta data '%(playlist_index)s '
  class AUDIO(object):
    MP3 = {
      'format': 'bestaudio/best',
      'outtmpl': f'{Audio_File_Save}/%(uploader)s/%(title)s.%(ext)s',
      'write_info_json': './file.json',
      'writethumbnail': True,
      'breakonexisting': True,
      'ProgressTemplate': 'progress',
      'ignoreerrors': True,
      'logger': MyLogger(),
      'progress_hooks': [youtube.hook],
      'noplaylist': True,
      'download_archive': AudioArchive,
      'postprocessors':[
      {'key': 'FFmpegExtractAudio', 'preferredcodec': 'mp3','preferredquality': '320'},
      {'key': 'FFmpegMetadata', 'add_metadata': 'True'},
      {'key': 'EmbedThumbnail','already_have_thumbnail': True,}
      ],
    }            
    INCOGNITO = {
      'format': 'bestaudio/best',
      'writethumbnail': True,
      'writesubs': True,
      'write_info_json': 'file.json',
      'outtmpl': f'{Audio_File_Save}/%(playlist)s/%(uploader)s/%(title)s.%(ext)s',
      'breakonexisting': True,
      'ProgressTemplate': 'progress',
      'writeautosubs': False,
      'ignoreerrors': True,
      'logger': MyLogger(),
      'progress_hooks': [youtube.hook],
      'noplaylist': True,
      'postprocessors':[
      {'key': 'FFmpegExtractAudio', 'preferredcodec': 'mp3','preferredquality': '320'},
      {'key': 'FFmpegMetadata', 'add_metadata': 'True'},
      {'key': 'EmbedThumbnail','already_have_thumbnail': True,}
      ],
    }            
  class VIDEO(object):
    MP4 = {
      'format': 'remux/best',
      'writesubs': True,
      'subtitle': '--write-sub --sub-lang en --sub-format json3',         
      'outtmpl': f'Video_File_Save/%(title)s.%(ext)s',
      'breakonexisting': True,
      'quite': True,
      'logger': MyLogger(),
      'progress_hooks': [youtube.hook],
      'ProgressTemplate': 'progress',
      'consoletitle': True,
      'download_archive': VideoArchive,
      'ignoreerrors': True,
      'postprocessors':[
      {'key': 'FFmpegExtractAudio', 'preferredcodec': 'mp4','preferredquality': '1080'},
      {'key': 'FFmpegMetadata', 'add_metadata': 'True'},
      {'key': 'EmbedThumbnail','already_have_thumbnail': False,}
      ],
    }
    INCOGNITO = {
      'format': 'remux/best',
      'writesubs': True,
      'subtitle': '--write-sub --sub-lang en --sub-format json3',
      'outtmpl': f'{Video_File_Save}/%(title)s.%(ext)s',
      'breakonexisting': True,
      'quite': True,
      'logger': MyLogger(),
      'progress_hooks': [youtube.hook],
      'ProgressTemplate': 'progress',
      'consoletitle': True,
      'ignoreerrors': True,
      'postprocessors':[
      {'key': 'FFmpegExtractAudio', 'preferredcodec': 'mp4','preferredquality': '1080'},
      {'key': 'FFmpegMetadata', 'add_metadata': 'True'},
      {'key': 'EmbedThumbnail','already_have_thumbnail': False,}
      ],
    }
except TypeError as e:
  raise TypeError('Please Configure config.yml')

#! Start of the gui
sg.theme('DarkAmber')
menu_def = [
  ['Config', ['Audio', 'Video']],
  ['Help', ['About...', 'Update']]
]
layout = [
  [sg.Menu(menu_def, pad=(30,30))],
  [sg.Text('YoutubeLink:'), sg.InputText(do_not_clear=False), sg.OptionMenu(values=['.mp3', '.mp4'], default_value='.mp3')],
  [sg.Button('DOWNLOAD'), sg.Button('CANCEL')],
]

window = sg.Window('Youtube Downloader Beta-V1.0', layout, size=[500, 400], element_justification='c')

while True:
  event, values = window.read()
  print(event, values)
  if event == 'CANCEL' or event == sg.WIN_CLOSED:
    break
  if event == 'DOWNLOAD':
    list = []
    list.append(f'{values[1]}')
    if values[2] == '.mp3':
      youtube.download(AUDIO.MP3, list[0])
    elif values[2] == '.mp4':
      youtube.download(VIDEO.MP4)

