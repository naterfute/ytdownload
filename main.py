from typer import Typer, Option, Argument
from requests.exceptions import RequestException
from urllib.parse import urlparse, parse_qs
from assets.downloader import Downloader
from typing import Optional
from munch import munchify
from loguru import logger
import requests
import yaml
import sys
debug = False
trace = False

def debug_init(trace, debug):
  logger.remove()
  if debug:
    logger.add(sys.stderr, level='DEBUG')
  elif trace:
    logger.add(sys.stderr, level='TRACE')
  else:
    logger.add(sys.stderr, level='INFO')
    pass
  pass

def spliturl(urls):
  logger.debug(urls)
  url=[]
  for x in urls:
    parsed_url=urlparse(x)

    query_params = parse_qs(parsed_url.query)
    video_id = query_params.get('v')
    playlist_id = query_params.get('list')
    if not playlist_id == None:
      url.append(playlist_id)
    else:
      url.append(video_id)
    continue
  logger.trace('Done Splitting Urls')
  logger.trace(url)
  return url
  
  
app = Typer(no_args_is_help=True, add_completion=False)
with open('config.yaml') as stream:
  try:
    yamlfile=yaml.safe_load(stream)
  except yaml.YAMLError as exc:
    print(exc)
loadedyaml = munchify(yamlfile)
# Youtube = Downloader(host=f'{loadedyaml.host}', port=loadedyaml.port)

@app.command()
def audio(
  trace:Optional[bool] = Option(False, '-t', '--trace', is_flag=True, help='Enable trace-level debugging.'),
  debug:Optional[bool] = Option(False, '-d', '--debug', is_flag=True, help='Enables debug'),
  urls:list[str] = Argument()
):
  
  debug_init(trace, debug)  
  

    
  try:
    Youtube = Downloader(host=f'{loadedyaml.host}', port=loadedyaml.port)
    r = requests.get(f'http://{loadedyaml.host}:{loadedyaml.port}/ping')
    r = munchify(r.json())
    logger.info(f'Pinging server: {r.ping}')
    logger.debug(r)
  except RequestException as e:
    logger.warning('Failed to connect to webserver run in debug to see more info')
    logger.info("Try making sure the webserver is up and your calling the right host and port!")
    logger.info(f"current host:{loadedyaml.host} port:{loadedyaml.port}")
    logger.debug(e)
    sys.exit()
  url=spliturl(urls)
  if url == []:
    logger.error('No provieded Urls!\nExiting')
    sys.exit()
  else:
    pass
  logger.trace(f'Full Urls: {urls}')
  for x in url:
    logger.debug(f'http://{loadedyaml.host}:{loadedyaml.port}/download/{x[0]}')
    response = requests.get(f'http://{loadedyaml.host}:{loadedyaml.port}/download/{x[0]}')
    if response.status_code == 200:
      logger.info(response.json())
      json_response = munchify(Youtube.getjson())
      logger.trace(json_response.info)
        
    else:
      print(f'Failure: {response.status_code}')
    pass



if __name__ == "__main__":
  app()

