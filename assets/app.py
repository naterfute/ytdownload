from flask import Flask, jsonify, request 
from flask_restful import Resource, Api
from downloader import Downloader
from flask_bcrypt import Bcrypt
from munch import munchify
import threading, queue
import yaml
with open('../config.yaml') as stream:
  try:
    yamlfile=yaml.safe_load(stream)
  except yaml.YAMLError as exc:
    print(exc)
config = munchify(yamlfile)

app = Flask(__name__) 
api = Api(app)
bcrypt = Bcrypt(app)
youtube = Downloader(server=True)

download_queue = queue.Queue()




class Download(Resource):
  t1=None
  active=0
  def get(self, url):
    download_queue.put(url)
    
    if not self.active > 1:
      self.t1 = threading.Thread(target=self.process_download_queue)
      self.t1.start()
      return {'message': 'Download request received and queued'}
    else:
      return {'message': 'Download Failed to queue! Check server logs for more details'}
 
  def process_download_queue(self):
    while not download_queue.empty():
      url = download_queue.get()
      youtube.download(url)
      self.remove_active_thread()
      print(f'Download completed for {url}')

  def remove_active_thread(self):
    self.active - 1


class DownloadInfo(Resource):
  def get(self):
    
    return {}
      
class ping(Resource):
  def get(self):
    
    return {
      'ping': 'pong',
            }

# @app.route('/')
# def home():
  # return 'use /download/youtubeurl to download videos'


api.add_resource(Download, '/download/<string:url>')
api.add_resource(ping, '/ping')


if __name__ == '__main__':
    app.run(debug = True, port=config.port)