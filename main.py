#!/usr/bin/python3.10
from ytdl.variables import youtube, VIDEO, AUDIO
import typer

app = typer.Typer(no_args_is_help=True, add_completion=False)

AUDIO_QUALITY = [64, 128, 256, 320]
VIDEO_QUALITY = [144, 240, 360, 480, 720, 1080]

@app.command()
def audio(
  link: str,
  incognito: bool = typer.Option(False, '-i', '--incognito', help="Doesn't write to archive file"),
  quality: int = typer.Option(320, '-q', '--quality', help='Choose the quality of the audio(Defaults to best)')
  ):
  links = []
  links.append(link)
  quality = int(quality)
  youtube.check_links(link)
  youtube.quality_check(quality, AUDIO_QUALITY)
  if not incognito:
    youtube.download(AUDIO.DEFAULT, links, quality)
  else:
    print('Running incognito')
    youtube.download(AUDIO.INCOGNITO, links, quality)


@app.command()
def video(
  link: str,
  incognito: bool = typer.Option(False, '-i', '--incognito', help="Doesn't write to archive file"),
  quality: int = typer.Option(1080, '-q', '--quality', help='Choose the quality of the video(Defaults to best)')
):
  youtube.check_links(link)
  youtube.quality_check(quality, VIDEO_QUALITY)
  if not incognito:
    youtube.download(VIDEO.DEFAULT, link, quality)
  else:
    print('Running incognito')
    youtube.download(VIDEO.INCOGNITO, link, quality)


if __name__ == "__main__":
  app()