#!/usr/bin/python3.10
import yt_dlp
from ytdl.variables import *
import typer, rich, click
from typing import Optional, List, Tuple
import sys
class NaturalOrderGroup(click.Group):
    def list_commands(self, ctx):
        return self.commands.keys()        

workingpath = getcwd()
app = typer.Typer(cls=NaturalOrderGroup, add_completion=False)

#######! AUDIO DOWNLOADER
def download(ydlopts, links):
  for x in links:
    with yt_dlp.YoutubeDL(ydlopts) as ydl:
      ydl.download(x)

@app.command()
def audio(
  ytlink: Optional[list[str]] = typer.Option(None, '-yt', '--ytlink'),
  incognito: bool = typer.Option(False, '-i', '--incognito'),
  ):
  if incognito:
    print('Running incognito')
    download(ydl_optsIAA, ytlink)
  else:
    download(ydl_optsA, ytlink)
#######! VIDEO DOWNLOADER
@app.command()
def video(
  ytlink: Optional[list[str]] = typer.Option(None, '-yt', '--ytlink'),
  incognito: bool = typer.Option(False, '-i', '--incognito')
):
  if incognito:
    print('Running incognito')
    download(ydl_optsIVA, ytlink)
  else:
    download(ydl_optsV, ytlink)

if __name__ == "__main__":
  app()