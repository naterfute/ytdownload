#!/usr/bin/python3.10
import os.path
import yt_dlp
from ytdl.variables import *
import typer, click
from typing import Optional, List, Tuple
import yaml

with open('config.yml') as f:
  config = yaml.safe_load(f)

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
  if incognito:
    print('Running incognito')
    youtube.download(AUDIO.INCOGNITO, link)
  else:
    youtube.download(AUDIO.DEFAULT, link)


# VIDEO DOWNLOADER
@app.command()
def video(
  link: Optional[list[str]] = typer.Option(None, '-l', '--link'),
  incognito: bool = typer.Option(False, '-i', '--incognito')
):
  if incognito:
    print('Running incognito')
    youtube.download(VIDEO.INCOGNITO, link)
  else:
    youtube.download(VIDEO.DEFAULT, link)


if __name__ == "__main__":
  app()