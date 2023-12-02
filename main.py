from assets.downloader import Downloader
from urllib.parse import unquote
from typer import Typer, Option
from typing import Optional
import requests


app = Typer()
Youtube = Downloader(host='localhost')

@app.command()
def audio(
  urls:Optional[list[str]] = Option(None, '-l', '--link', help='Url to youtube video/playlist'),
  server:Optional[bool] = Option(False, '-s', '--server', help='Send a web request to pre-configured url using urls as request')
):
  url=[]
  for x in urls:
    if 'list=' in x:
      spliturl=x.split('list=')
      url.append(spliturl[-1])
    else:
      spliturl=x.split('v=')
      url.append(spliturl[-1])
  print(url)
  if not server:
    pass
    # Youtube.download(urls=urls)
  else:
    print(f'http://{Youtube.host}:{Youtube.port}/download/{url[0]}')
    response = requests.get(f'http://{Youtube.host}:{Youtube.port}/download/{url[0]}')
    if response.status_code == 200:
      print(response.json())
    else:
      print(f'Failure: {response.status_code}')
    pass

if __name__ == "__main__":
  app()