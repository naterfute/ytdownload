
# Using flask to make an api 
# import necessary libraries and functions 
from flask import Flask, jsonify, request 
from flask_restful import Resource, Api
from .downloader import Downloader
import threading
# creating a Flask app 

app = Flask(__name__) 
api = Api(app) 
youtube = Downloader()
class Download(Resource):

  def get(self, url):
    youtube.download(url)
    return youtube.json()
  
  
api.add_resource(Download, '/download/<string:url>')


if __name__ == '__main__': 
    app.run(debug = True) 