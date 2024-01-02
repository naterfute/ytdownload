import os
import yt_dlp
from munch import munchify
from yt_dlp.utils import DownloadError
from typing import Optional
from json import JSONEncoder


if __name__ == 'downloader':
  from db import database
else:
  pass


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
      pass





class Downloader:
  Started=False
  web_use=False
  host=None
  port=None
  download_path=None
  Status=None
  filename=None
  time_elapse=None
  percent=None
  eta=None
  url=None
  title=None

  def __init__(
    self, host:Optional[str]=None, 
    port:Optional[int]=5000,
  ):
    if not host == None:
      self.web_use = True
      self.host = host
      self.port = port
      self.download_path = 'downloads/'

    
  
  def progress_hook(self, d):
    d = munchify(d)
    if d.status == 'error':
      pass
    if d.status == 'finished':
      print(f'Done Downloading "{d["filename"]}"')
      self.Started = False
      self.filename = d['filename']
      self.time_elapse = d['elapsed']
      self.album = d.info_dict.playlist_title, 'unknown'
      self.playlist = d.info_dict.playlist_id, 'unknown'
      
      db = database()
      db.write_to_videoDB(self.title, self.url, self.download_path, self.time_elapse)
      db.write_to_albumDB(self.album, self.playlist)

    if d.status == 'downloading':
      print(f'Now Downloading "{d["tmpfilename"]}"')
      self.filename = d['tmpfilename']
      self.percent = d['_percent_str']
      self.eta = d['_eta_str']
      if not self.Started:
        self.Started = True
        
  def postprocessor_hooks(self, d):
    d = munchify(d)
    if d.status == 'started':
      info = munchify(d['info_dict'])
      self.url = info.webpage_url
      self.title = info.title
      self.download_path = info.filepath
      self.Status = 'Started'
      pass
    if d.status == 'finished':
      self.Status = 'Finished'
      pass

  def ydl_opts(self):
    ydl_opts = {
      # 'ratelimit': 62500, # Kilobytes
      'logger': MyLogger(),
      'breakonexisting': True,
      'progress_hooks': [self.progress_hook],
      'postprocessor_hooks': [self.postprocessor_hooks],
      'format': 'bestaudio/best',
      'writethumbnail': True,
      'outtmpl': 'downloads/%(playlist_title)s/%(video_autonumber)s-%(title)s.%(ext)s',
      'skip_broken': True,
      'ignoreerrors': True,
      'postprocessors': [
      {'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '0'},
      {'add_metadata': 'True', 'key': 'FFmpegMetadata'},
      {'already_have_thumbnail': False, 'key': 'EmbedThumbnail'}
    ]}

    return ydl_opts


  def download(self, urls):
    with yt_dlp.YoutubeDL(self.ydl_opts()) as ydl:
      ydl.download(urls)
    
  def getjson(self):
    data = {
      'WebUse': {
        'use': self.web_use,
        'host': self.host,
        'port': self.port
        },
      'Started': self.Started,
      'info': {
      'Download_path': self.download_path,
      'filename': self.filename,
      'time_elapse': self.time_elapse,
      'percent': self.percent,
      'eta': self.eta
      },
    }
    return data
  