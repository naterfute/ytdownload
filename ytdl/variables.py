from os import environ, getcwd, path
from sys import platform
import math, json, yt_dlp
import yaml
try:
  if not path.isfile(f'./ytdl/config.yml'):
    with open('./ytdl/config.yml', 'w') as f:
      f.write('''
AUDIO:
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
  downloadpath = environ['HOME']
  workingpath = getcwd()
  Anime_File_Save = f'{downloadpath}/Videos/Anime'
  AnimeArchive = f'{downloadpath}/Videos/AnimeArchive.txt'
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
        # global filesize 
        # filesize = json_dict.get('filesize')
        print(title)

      def download(ydlopts, links):
        with yt_dlp.YoutubeDL(ydlopts) as ydl:
          for x in links:
            #* Set up so that if playlist = NA change download! path
            # youtube.title(ydl, x)
            ydl.download([x])

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
          print('Done downloading, now post-processing ...')

        if d['status'] == 'downloading':
          global currently_downloaded
          d.get('')
          currently_downloaded = d.get('downloaded_bytes')
          # print(f'{COLOR.Green}{youtube.convert_size(currently_downloaded)}{COLOR.Blue}/{COLOR.Green}{youtube.convert_size(filesize)}{COLOR.Default}')
          print(d['_percent_str'], d['_eta_str'])

  #* Multi-Line Variables

  class AUDIO(object):
    DEFAULT = {
      'format': 'bestaudio/best',
      'outtmpl': f'{Audio_File_Save}/%(playlist)s/%(uploader)s/%(playlist_index)s - %(title)s.%(ext)s',
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
      'subtitle': 'write-sub sub-lang en sub-format json3',
      'outtmpl': f'{Audio_File_Save}/%(playlist)s/%(uploader)s/%(playlist_index)s - %(title)s.%(ext)s',
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
    DEFAULT = {
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
  raise TypeError('Please Configure config.yml')