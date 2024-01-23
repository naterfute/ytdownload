#!/usr/bin/python3.10
from ytdl.variables import youtube
import typer

app = typer.Typer(no_args_is_help=True, add_completion=False)

AUDIO_QUALITY = [64, 128, 256, 320]
VIDEO_QUALITY = [144, 240, 360, 480, 720, 1080]
youtubedl = youtube()
@app.command()
def audio(
  link: str,
  incognito: bool = typer.Option(False, '-i', '--incognito', help="Doesn't write to archive file"),
  quality: int = typer.Option(320, '-q', '--quality', help='Choose the quality of the audio(Defaults to best)')
  ):
  links = []
  links.append(link)
  quality = int(quality)
  youtubedl.check_links(link)
  youtubedl.quality_check(quality, AUDIO_QUALITY)
  if not incognito:
    youtubedl.download(youtubedl.DefaultAudio(quality), links, quality)
  else:
    print('Running incognito')
    youtubedl.download(youtubedl.AudioIncognito(quality), links, quality)


@app.command()
def video(
  link: str,
  incognito: bool = typer.Option(False, '-i', '--incognito', help="Doesn't write to archive file"),
  quality: int = typer.Option(1080, '-q', '--quality', help='Choose the quality of the video(Defaults to best)')
):
  links = []
  links.append(link)
  quality = int(quality)
  youtubedl.check_links(link)
  youtubedl.quality_check(quality, VIDEO_QUALITY)
  if not incognito:
    youtubedl.download(youtubedl.DefaultVideo(quality), links, quality)
  else:
    print('Running incognito')
    youtubedl.download(youtubedl.VideoIncognito(quality), links, quality)


if __name__ == "__main__":
  app()