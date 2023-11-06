from os import environ, getcwd, path
from sys import platform
import yt_dlp, math, json
from typing import Optional
import yaml
try:
  with open(path.join('ytdl', 'config.yml')) as f:
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
  class youtube(object):
      def __init__(self):
        self.bytes = None
        self.info = None   
      quality = None
      def quality_check(user_quality, quality_list:list):
        if user_quality == None:
          pass
        elif not user_quality in quality_list:
          raise SyntaxError("Invalid Audio/Video Quality")
        else:
          pass

      def title(ydl, x):
        info = ydl.extract_info(x, download=False)
        info = json.dumps(ydl.sanitize_info(info))
        json_dict = json.loads(info)
        title = json_dict.get('title')
        print(title)
        
      def download(ydlopts, links, quality):
        youtube.quality = quality
        with yt_dlp.YoutubeDL(ydlopts) as ydl:
          for x in links:
            #* Set up so that if playlist = NA change download! path
            ydl.download([x])
      
      def hook(self, d):
        if d['status'] == 'finished':
          d.get('')
          print(d['filename'])
          print('Done downloading, now post-processing ...')

        if d['status'] == 'downloading':
          currently_downloaded = d.get('downloaded_bytes')
          self.bytes = currently_downloaded
          print(youtube.exchange())
          print(d['_percent_str'], d['_eta_str'])
          # print(f'Elaspsed:')
          # print(d['elapsed'])

  def base(incognito:bool,format:str, outtmpl:str, post_processor:str, archive:Optional[str] = None):
    try:
      BASE = {
        'writethumbnail': True,
        'breakonexisting': True,
        'consoletitle': True,
        'ProgressTemplate': 'progress',
        'ignoreerrors': True,
        'logger': MyLogger(),
        'progress_hooks': [youtube.hook],
        'noplaylist': True,
        'postprocessors':[
        {'key': 'FFmpegMetadata', 'add_metadata': 'True'},
        {'key': 'EmbedThumbnail','already_have_thumbnail': True,}
        ],
      }
      if incognito:
        BASE['format'], BASE['outtmpl'], BASE['download_archive'] = f'{format}', f'{outtmpl}', archive and BASE['postprocessors'].insert(0, post_processor)
      else:
        BASE['format'], BASE['outtmpl'] = f'{format}', f'{outtmpl}' and BASE['postprocessors'].insert(0, post_processor)
      return BASE
    except:
      print('error')
  #* Multi-Line Variables
#! Must make use of this in meta data '%(playlist_index)s '
  class AUDIO(object):
    DEFAULT = base(incognito=False, format='bestaudio/best', outtmpl=f'{Audio_File_Save}/%(uploader)s/%(title)s.%(ext)s', post_processor={
                    'key': 'FFmpegExtractAudio', 'preferredcodec': 'mp3', 'preferredquality': f'{youtube.quality}'}, archive=AudioArchive)
    INCOGNITO = base(incognito=True, format='bestaudio/best', outtmpl=f'{Audio_File_Save}/%(uploader)s/%(title)s.%(ext)s', post_processor={
                      'key': 'FFmpegExtractAudio', 'preferredcodec': 'mp3', 'preferredquality': f'{youtube.quality}'})

  class VIDEO(object):
      DEFAULT = base(incognito=False, format='remux/best', outtmpl=f'{Video_File_Save}/%(title)s.%(ext)s', post_processor={
                      'key': 'FFmpegExtractAudio', 'preferredcodec': 'mp4', 'preferredquality': f'{youtube.quality}'}, archive=AudioArchive)
      INCOGNITO = base(incognito=True, format='remux/best', outtmpl=f'{Video_File_Save}/%(title)s.%(ext)s', post_processor={
                        'key': 'FFmpegExtractAudio', 'preferredcodec': 'mp4', 'preferredquality': f'{youtube.quality}'})

  class COLOR:
    Red = '\033[91m'
    Green = '\033[92m'
    Blue = '\033[94m'
    Cyan = '\033[96m'
    White = '\033[97m'
    Yellow = '\033[93m'
    Magenta = '\033[95m'
    Grey = '\033[90m'
    Black = '\033[90m'
    Default = '\033[0m'
except TypeError as e:
  print(e)
  raise TypeError('Please Configure config.yml')