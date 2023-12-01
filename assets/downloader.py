import yt_dlp
from typing import Optional
import os
from munch import munchify
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


class Downloader:
  Started = False
  web_use = False
  Status = ''
  def __init__(self, host:Optional[str]=None, 
               host_password:Optional[str]=None, 
               download_path:Optional[str]=None, 
               port:Optional[int]=22):
    if not host == None:
      self.web_use = True
    else:
      pass

  
  def progress_hook(self, d):
    self.Status
    if d['status'] == 'finished':
      print(f'Done Downloading "{d['filename']}"')
      self.Started = False
    if d['status'] == 'downloading':
      if self.Started:
        print(d['_percent_str'], d['_eta_str'])
      else: 
        print(f'Now Downloading "{d['tmpfilename']}"')
        print(d['_percent_str'], d['_eta_str'])
        self.Started = True
        
  def postprocessor_hooks(self, d):
    if d['status'] == 'started':
      self.Status = 'Started'
      pass
    if d['status'] == 'finished':
      self.Status = 'Finished'
      pass

  def ydl_opts(self):
    ydl_opts = {
      'logger': MyLogger(),
      'breakonexisting': True,
      'progress_hooks': [self.progress_hook],
      'postprocessor_hooks': [self.postprocessor_hooks],
      'format': 'bestaudio/best',
      'writethumbnail': True,
      'outtmpl': 'downloads/%(playlist_title)s/%(title)s.%(ext)s',
      'postprocessors': [
        {'key': 'FFmpegExtractAudio',
      'preferredcodec': 'mp3',
      'preferredquality': 'None'},
      {'add_metadata': 'True', 'key': 'FFmpegMetadata'},
      {'already_have_thumbnail': False, 'key': 'EmbedThumbnail'}
    ]}
    return ydl_opts

  
  def download(self, urls):
    
    for x in urls:
      with yt_dlp.YoutubeDL(self.ydl_opts()) as ydl:
          ydl.download(x)
