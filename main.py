#!/usr/bin/python3.10
from ytdl.variables import *
import typer, click
from typing import Optional

class NaturalOrderGroup(click.Group):
  def list_commands(self, ctx):
    return self.commands.keys()

workingpath = getcwd()
app = typer.Typer(cls=NaturalOrderGroup, add_completion=False)


# AUDIO DOWNLOADER
@app.command()
def audio(
  link: Optional[list[str]] = typer.Option(None, '-l', '--link'),
  incognito: bool = typer.Option(False, '-i', '--incognito'),
  ):
  if not incognito:
    youtube.download(AUDIO.DEFAULT, link)
  else:
    print('Running incognito')
    youtube.download(AUDIO.INCOGNITO, link)


# VIDEO DOWNLOADER
@app.command()
def video(
  link: Optional[list[str]] = typer.Option(None, '-l', '--link'),
  incognito: bool = typer.Option(False, '-i', '--incognito')
):
  if not incognito:
    youtube.download(VIDEO.DEFAULT, link)
  else:
    print('Running incognito')
    youtube.download(VIDEO.INCOGNITO, link)

try:
  if __name__ == "__main__":
    app()
except AssertionError as e:
  print(e)