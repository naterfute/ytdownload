#!/usr/bin/python3.10
import yt_dlp
from ytdl.variables import *
import typer, rich, click
from typing import Optional, List, Tuple
import sys
import json
class NaturalOrderGroup(click.Group):
    def list_commands(self, ctx):
        return self.commands.keys()        

workingpath = getcwd()
app = typer.Typer(cls=NaturalOrderGroup, add_completion=False)

#######! AUDIO DOWNLOADER
@app.command()
def audio(
  link: Optional[list[str]] = typer.Option(None, '-l', '--link'),
  incognito: bool = typer.Option(False, '-i', '--incognito'),
  ):
  if incognito:
    print('Running incognito')
    youtube.download(ydl_optsIAA, link)
  else:
    youtube.download(ydl_optsA, link)

#######! VIDEO DOWNLOADER
@app.command()
def video(
  link: Optional[list[str]] = typer.Option(None, '-l', '--link'),
  incognito: bool = typer.Option(False, '-i', '--incognito')
):
  if incognito:
    print('Running incognito')
    youtube.download(ydl_optsIVA, link)
  else:
    youtube.download(ydl_optsV, link)

if __name__ == "__main__":
  app()