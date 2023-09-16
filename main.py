#!/usr/bin/python3.10
from ytdl.variables import youtube, VIDEO, AUDIO
import typer, click
from typing import Optional

class NaturalOrderGroup(click.Group):
  def list_commands(self, ctx):
    return self.commands.keys()

app = typer.Typer(cls=NaturalOrderGroup, add_completion=False)

AUDIO_QUALITY = [64, 128, 256, 320]
VIDEO_QUALITY = [144, 240, 360, 480, 720, 1080]

# AUDIO DOWNLOADER
@app.command()
def audio(
  link: Optional[list[str]] = typer.Option(None, '-l', '--link'),
  incognito: bool = typer.Option(False, '-i', '--incognito'),
  quality: Optional[int] = typer.Option(None, '-q', '--quality', help='Choose the quality of the audio(Defaults to best)')
  ):
  if quality == None:
    pass
  elif not quality in AUDIO_QUALITY:
    raise SyntaxError('Invalid Audio Quality')
  else:
    pass
  if not incognito:
    youtube.download(AUDIO.DEFAULT, link, quality)
  else:
    print('Running incognito')
    youtube.download(AUDIO.INCOGNITO, link, quality)


# VIDEO DOWNLOADER
@app.command()
def video(
  link: Optional[list[str]] = typer.Option(None, '-l', '--link'),
  incognito: bool = typer.Option(False, '-i', '--incognito'),
  quality: Optional[int] = typer.Option(None, '-q', '--quality', help='Choose the quality of the Video(Defaults to best)')
):
  if quality == None:
    pass
  elif not quality in VIDEO_QUALITY:
    raise SyntaxError('Invalid Video Quality')
  else:
    pass
  if not incognito:
    youtube.download(VIDEO.DEFAULT, link, quality)
  else:
    print('Running incognito')
    youtube.download(VIDEO.INCOGNITO, link, quality)

try:
  if __name__ == "__main__":
    app()
except AssertionError as e:
  print(e)