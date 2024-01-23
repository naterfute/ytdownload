from os import environ, getcwd, path
from sys import platform
import yt_dlp, math, json
from typing import Optional
from munch import munchify
import yaml
try:
  with open(path.join('ytdl', 'config.yml')) as f:
    config = yaml.safe_load(f)
    config = munchify(config)

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
  class youtube():
      Audio_File_Save = config['AUDIO']['path']
      AudioArchive = config['AUDIO']['archive']
      Video_File_Save = config['VIDEO']['path']
      VideoArchive = config['VIDEO']['archive']
      download_path=None
      def quality_check(self, user_quality, quality_list:list):
        if user_quality == None:
          pass
        elif not user_quality in quality_list:
          raise SyntaxError("Invalid Audio/Video Quality")
        else:
          pass
        
      def check_links(self, links):
        if links == []:
          raise TypeError("You didn't supply any link!")
        else:
          pass
        

      def title(self, ydl:yt_dlp.YoutubeDL, x):
        info = ydl.extract_info(x, download=False)
        info = json.dumps(ydl.sanitize_info(info))
        json_dict = json.loads(info)
        title = json_dict.get('title')
        print(title)
        
      def download(self, ydlopts, links, quality):
        self.quality = quality
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
          self.bytes = d.get('downloaded_bytes')
          print(d['_percent_str'], d['_eta_str'])
          # print(f'Elaspsed:')
          # print(d['elapsed'])

      def base(self, incognito:bool,format:str, post_processor:str, archive:Optional[str] = None):
        try:
          BASE = {
            'writethumbnail': True,
            'breakonexisting': True,
            'consoletitle': True,
            'outtmpl': f"{self.download_path}/%(playlist_title)s/%(playlist_autonumber)s - %(title)s.%(ext)s",
            'ProgressTemplate': 'progress',
            'ignoreerrors': True,
            'logger': MyLogger(),
            'progress_hooks': [self.hook],
            'noplaylist': True,
            'postprocessors':[
            {'key': 'FFmpegMetadata', 'add_metadata': 'True'},
            {'key': 'EmbedThumbnail','already_have_thumbnail': True,}
            ],
          }
          if incognito:
            BASE['format'], BASE['download_archive'] = f'{format}', archive and BASE['postprocessors'].insert(0, post_processor)
          else:
            BASE['format'] = f'{format}' and BASE['postprocessors'].insert(0, post_processor)
          return BASE
        except:
          print('error')
      #* Multi-Line Variables

      def DefaultAudio(self, quality):
        DEFAULT = self.base(
          incognito=False, format='bestaudio/best',
          post_processor={'key': 'FFmpegExtractAudio', 'preferredcodec': 'mp3', 'preferredquality': f'{quality}'}, archive=config.AUDIO.archive) # type: ignore
        return DEFAULT

      def AudioIncognito(self, quality):
          INCOGNITO = self.base(incognito=True, format='bestaudio/best',
                                post_processor={'key': 'FFmpegExtractAudio', 'preferredcodec': 'mp3', 'preferredquality': f'{quality}'}) # type: ignore
          return INCOGNITO
      def DefaultVideo(self, quality):
        DEFAULT = self.base(incognito=False, format='remux/best',
                            post_processor={'key': 'FFmpegExtractAudio', 'preferredcodec': 'mp4', 'preferredquality': f'{quality}'}, archive=config.VIDEO.archive) # type: ignore
        return DEFAULT

      def VideoIncognito(self, quality):
        INCOGNITO = self.base(
          incognito=True, format='remux/best',
          post_processor={'key': 'FFmpegExtractAudio', 'preferredcodec': 'mp4', 'preferredquality': f'{quality}'}) # type: ignore
        return INCOGNITO

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