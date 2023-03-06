
#! Figure out how to use yml files dumdum
from os import environ, getcwd
import math, json, yt_dlp
#! user most Important
downloadpath = environ['HOME']
workingpath = getcwd()
Audio_File_Save = f'{downloadpath}/Music/Downloaded'
Video_File_Save = f'{downloadpath}/Videos/'
AudioArchive = f'{downloadpath}/Music/AudioArchive.txt'
VideoArchive = f'{downloadpath}/Videos/VideoArchive.txt'
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
      global filesize 
      filesize = json_dict.get('filesize')
      print(title)

    def download(ydlopts, links):
      with yt_dlp.YoutubeDL(ydlopts) as ydl:
        for x in links:
          #* Set up so that if playlist = NA change download path 
          youtube.title(ydl, x)
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
        currently_downloaded = d.get('downloaded_bytes')
        print(f'{COLOR.Green}{youtube.convert_size(currently_downloaded)}{COLOR.Blue}/{COLOR.Green}{youtube.convert_size(filesize)}{COLOR.Default}')
        print(d['_percent_str'], d['_eta_str'])

#* Multi-Line Variables

ydl_optsA = {
  'format': 'bestaudio/best',
  'writethumbnail': True,
  'outtmpl': f'{Audio_File_Save}/%(playlist)s/%(uploader)s/%(playlist_index)s - %(title)s.%(ext)s',
  'writesubs': True,
  'sublang': 'eng',
  'subformat': 'json3',
  'outtmpl': f'{Audio_File_Save}/%(playlist)s/%(uploader)s/%(playlist_index)s - %(title)s.%(ext)s',
  'breakonexisting': True,
  'ProgressTemplate': 'progress',
  'writeautosubs': False,
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

ydl_optsIAA = {
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

ydl_optsV = {
  'format': 'remux/best',
  'writesubs': True,
  'subtitle': '--write-sub --sub-lang en --sub-format json3',         
  'outtmpl': Video_File_Save + '/%(title)s.%(ext)s',
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
ydl_optsIVA = {
  'format': 'remux/best',
  'writesubs': True,
  'subtitle': '--write-sub --sub-lang en --sub-format json3',
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
  ],
}
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
  ],
    

}


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
