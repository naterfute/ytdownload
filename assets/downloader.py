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
      print('PostProcessing started')
    if d['status'] == 'finished':
      print('PostProcessing finished')

  ydl_opts = {
      'logger': MyLogger(),
      'progress_hooks': [progress_hook],
      'postprocessor_hooks': [postprocessor_hooks],
      # 'format': Downloader.format_selector,
      # 'format': 'mp3',
      
      'postprocessor': [
        {'preferred_codec': 'mp3/bestaudio/best'},
        {'key': 'EmbedThumbnail','already_have_thumbnail': True,}]
  }
  
  def download(self, urls):
    for x in urls:
      with yt_dlp.YoutubeDL(self.ydl_opts) as ydl:
          ydl.download(x)
  
