from os import environ, getcwd, path
from sys import platform
import yt_dlp, math, json
from typing import Optional
import yaml
try:
  if not path.isfile(f'./ytdl/config.yml'):
    with open('./ytdl/config.yml', 'w') as f:
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
  with open('./ytdl/config.yml') as f:
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
      quality = None
      def transfer(total_bytes_download):
        return total_bytes_download

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
        INCOGNITO = BASE['format'], BASE['outtmpl'], BASE['download_archive'] = f'{format}', f'{outtmpl}', archive and BASE['postprocessors'].append(post_processor)
      else:
        INCOGNITO = BASE['format'], BASE['outtmpl'] = f'{format}', f'{outtmpl}' and BASE['postprocessors'].append(post_processor)
      return INCOGNITO
    except:
      print('error')
  #* Multi-Line Variables
#! Must make use of this in meta data '%(playlist_index)s '
  class AUDIO(object):
    DEFAULT = base(incognito=False, format='bestaudio/best', outtmpl=f'{Audio_File_Save}/%(uploader)s/%(title)s.%(ext)s', post_processor={'key': 'FFmpegExtractAudio', 'preferredcodec': 'mp3','preferredquality': f'{youtube.quality}'}, archive=AudioArchive)
    INCOGNITO = base(incognito=True, format='bestaudio/best', outtmpl=f'{Audio_File_Save}/%(uploader)s/%(title)s.%(ext)s', post_processor={'key': 'FFmpegExtractAudio', 'preferredcodec': 'mp3','preferredquality': f'{youtube.quality}'})

  class VIDEO(object):
    DEFAULT = base(incognito=False, format='remux/best', outtmpl=f'{Video_File_Save}/%(title)s.%(ext)s', post_processor={'key': 'FFmpegExtractAudio', 'preferredcodec': 'mp4','preferredquality': f'{youtube.quality}'}, archive=AudioArchive)
    INCOGNITO = base(incognito=True, format='remux/best', outtmpl=f'{Video_File_Save}/%(title)s.%(ext)s', post_processor={'key': 'FFmpegExtractAudio', 'preferredcodec': 'mp4','preferredquality': f'{youtube.quality}'})
    
  class anime():
    ydl_optsANIME = {
      'format': 'remux/best',
      'write-subs': True,
      'subtitle': 'write-sub sub-lang *en* sub-format json3',
      'sublang': '*en*',
      'subformat': 'json3',
      'outtmpl': Video_File_Save + '/%(title)s.%(ext)s',
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
      ]}


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

