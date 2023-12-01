import yt_dlp
from typing import Optional
import os
class MyLogger:
    def debug(self, msg):
        # For compatibility with youtube-dl, both debug and info are passed into debug
        # You can distinguish them by the prefix '[debug] '
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


class Downloader():
  Started = False
  def __init__(self, host:Optional[str]=None, host_password:Optional[str]=None, download_path:Optional[str]=None, port:Optional[int]=22):
    pass
  
  
  def progress_hook(d):
    if d['status'] == 'finished':
      print(f'Done Downloading "{d['filename']}"')
    if d['status'] == 'downloading':
      if Downloader.Started:
        print(d['_percent_str'], d['_eta_str'])
      else: 
        print(f'Downloading "{d['tmpfilename']}"')
        print(d['_percent_str'], d['_eta_str'])
        Downloader.Started = True
        
  def postprocessor_hooks(d):
    if d['status'] == 'started':
      pass
      # print('PostProcessing started')
    if d['status'] == 'finished':
      pass
      # print('PostProcessing finished')

  ydl_opts = {
      'logger': MyLogger(),
      'breakonexisting': True,
      'progress_hooks': [progress_hook],
      'postprocessor_hooks': [postprocessor_hooks],
      'format': 'bestaudio/best',
      'writethumbnail': True,
      'outtmpl': '%(playlist_title)s/%(title)s.%(ext)s',
      'postprocessors': [
        {'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': 'None'},
        {'add_metadata': 'True', 'key': 'FFmpegMetadata'},
        {'already_have_thumbnail': False, 'key': 'EmbedThumbnail'}
      ]}

  
  def download(self, urls):
    for x in urls:
      with yt_dlp.YoutubeDL(self.ydl_opts) as ydl:
          ydl.download(x)
  


# {'ProgressTemplate': 'progress',
#  'breakonexisting': True,
#  'consoletitle': True,
#  'format': 'bestaudio/best',
#  'ignoreerrors': True,
#  'logger': <ytdl.variables.MyLogger object at 0x7f4a9d34a870>,
#  'noplaylist': True,
#  'outtmpl': None,
#  'postprocessors': [{'key': 'FFmpegExtractAudio',
#                      'preferredcodec': 'mp3',
#                      'preferredquality': 'None'},
#                     {'add_metadata': 'True', 'key': 'FFmpegMetadata'},
#                     {'already_have_thumbnail': True, 'key': 'EmbedThumbnail'}],
#  'progress_hooks': [<function youtube.hook at 0x7f4a9cafe520>],
#  'writethumbnail': True}



# {'ProgressTemplate': 'progress',
#  'breakonexisting': True,
#  'consoletitle': True,
#  'download_archive': None,
#  'format': 'bestaudio/best',
#  'ignoreerrors': True,
#  'logger': <ytdl.variables.MyLogger object at 0x7f4a9d4a11f0>,
#  'noplaylist': True,
#  'outtmpl': './Audio//%(uploader)s/%(title)s.%(ext)s',
#  'postprocessors': [{'add_metadata': 'True', 'key': 'FFmpegMetadata'},
#                     {'already_have_thumbnail': True, 'key': 'EmbedThumbnail'}],
#  'progress_hooks': [<function youtube.hook at 0x7f4a9cafe520>],
#  'writethumbnail': True}

# {'ProgressTemplate': 'progress',
#  'breakonexisting': True,
#  'consoletitle': True,
#  'format': 'remux/best',
#  'ignoreerrors': True,
#  'logger': <ytdl.variables.MyLogger object at 0x7f4a9cfc7410>,
#  'noplaylist': True,
#  'outtmpl': None,
#  'postprocessors': [{'key': 'FFmpegExtractAudio',
#                      'preferredcodec': 'mp4',
#                      'preferredquality': 'None'},
#                     {'add_metadata': 'True', 'key': 'FFmpegMetadata'},
#                     {'already_have_thumbnail': True, 'key': 'EmbedThumbnail'}],
#  'progress_hooks': [<function youtube.hook at 0x7f4a9cafe520>],
#  'writethumbnail': True}

# {'ProgressTemplate': 'progress',
#  'breakonexisting': True,
#  'consoletitle': True,
#  'download_archive': None,
#  'format': 'remux/best',
#  'ignoreerrors': True,
#  'logger': <ytdl.variables.MyLogger object at 0x7f4a9e92b500>,
#  'noplaylist': True,
#  'outtmpl': './Videos//%(title)s.%(ext)s',
#  'postprocessors': [{'add_metadata': 'True', 'key': 'FFmpegMetadata'},
#                     {'already_have_thumbnail': True, 'key': 'EmbedThumbnail'}],
#  'progress_hooks': [<function youtube.hook at 0x7f4a9cafe520>],
#  'writethumbnail': True}
