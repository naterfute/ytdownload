#!/usr/bin/python3.10
import yt_dlp, typer, rich, click
from os import path, mkdir
from sys import exit
from ytdl.variables import *
from ytdl.version import __version__
from rich.console import Console

class NaturalOrderGroup(click.Group):
    def list_commands(self, ctx):
        return self.commands.keys()        
    

workingpath = getcwd()
app = typer.Typer(cls=NaturalOrderGroup)
console = Console()


def main():
    pass

#######! AUDIO DOWNLOADER

@app.command()
def audio(
    multiple: bool = typer.Option(False, '--multiple', '-m' , help='Insert Multiple Links to Download'),
    dpath: str = typer.Option(Audio_File_Save, '--path', '-p', help='Temp Download Path'),
    subtitles: bool = typer.Option(False, '--subtitles', '-s', help='Download Subtitles Only'),
    incognito: bool = typer.Option(False, '--incognito', '-i', help='Download files without writing to the Archive file')
          ):
        '''Downloads Youtube Videos as mp3'''
        downloadpath = environ['HOME']
        youtubelinks=[]
        link = True
        try:
            pathExist = path.exists(dpath)
            if path.exists(AudioArchive):
                pass
            else:
                with open(f'{AudioArchive}', 'w') as f:
                    f.close()
                pass
            if pathExist == False:
                print('Path Does not exist')
                exit(0)
            if pathExist:
                print('path Exists, Continuing ')

            if multiple:
                print('Insert links to download')
                print('Put Links Here')
            
                while True:
            
                    multiplelinks=input('')
                   
                    if 'https://www.youtube.com' in multiplelinks or 'https://youtu.be/' in multiplelinks or 'http://youtu.be' in multiplelinks or 'https://youtube.com' in multiplelinks or 'youtube.com' in multiplelinks:

                        if multiplelinks in youtubelinks:
                            print('Already in List')
                            
                        else:
                            youtubelinks.append(multiplelinks)

                    else:
                        print('Not a valid youtube video')

                    if multiplelinks == 'next' and incognito == True:
                        print('Downloading Audio Incognito')
                        for x in youtubelinks:
                            with yt_dlp.YoutubeDL(ydl_optsIAA) as ydl:
                                ydl.download(x)
                    if multiplelinks == 'next' and subtitles == True:
                        print('Downloading Subtitles only')
                        for x in youtubelinks:
                            with yt_dlp.YoutubeDL(ydl_optsAS) as ydl:
                                ydl.download(x)         
                    
                    if multiplelinks == 'next':
                        print('Downloading Audio')
                        for x in youtubelinks:
                            with yt_dlp.YoutubeDL(ydl_optsA) as ydl:
                                ydl.download(x)
                        exit(0)

            if incognito:
                print('Downloading incognito')
                ytlink=input('Insert One Link: ')
                
                with yt_dlp.YoutubeDL(ydl_optsIAA) as ydl:
                    ydl.download(ytlink)
            if subtitles:
                print('Put Link Here')
                subtitles = input('')
                with yt_dlp.YoutubeDL(ydl_optsAS) as ydl:
                    ydl.download(subtitles)
                exit(0) 
                            
            if link:
                while True:
                    ytlink=input('Insert One Link: ')

                    if 'https://www.youtube.com' in ytlink or 'https://youtu.be/' in ytlink or 'http://youtu.be' in ytlink or 'https://youtube.com' in ytlink or 'youtube.com' in ytlink:
                        with yt_dlp.YoutubeDL(ydl_optsA) as ydl:
                            ydl.download([ytlink])
                        break
                    else:
                        print(f'{color.WARNING}Not a Youtube Link{color.END}')
        except KeyboardInterrupt as e:
            print('\nKeyboard interrupt.')
        except FileNotFoundError as e:
            print(e) 


########!VIDEO DOWNLOADER
@app.command()
def video(
    multiple: bool = typer.Option(False, '--multiple', '-m' , help='Insert Multiple Links to Download'),
    dpath: str = typer.Option(Video_File_Save, '--path', '-p', help='Temp Download Path'),
    subtitles: bool = typer.Option(False, '--subtitles', '-s', help='Download Subtitles Only'),
    incognito: bool = typer.Option(False, '--incognito', '-i', help='Download files without writing to the Archive file')
          ):
        '''Downloads Youtube Videos as mp4'''
        downloadpath = environ['HOME']
        youtubelinks=[]
        link = True
        try:
            pathExist = path.exists(dpath)
            if path.exists(VideoArchive):
                pass
            else:
                with open(f'{VideoArchive}', 'w') as f:
                    f.close()
                pass
            if pathExist == False:
                print('Path Does not exist')
                exit(0)
            if pathExist:
                print('path Exists, Continuing ')

            if multiple:
                print('Insert links to download')
                print('Put Links Here')
            
                while True:
            
                    multiplelinks=input('')
                   
                    if 'https://www.youtube.com' in multiplelinks or 'https://youtu.be/' in multiplelinks or 'http://youtu.be' in multiplelinks or 'https://youtube.com' in multiplelinks or 'youtube.com' in multiplelinks:

                        if multiplelinks in youtubelinks:
                            print('Already in List')
                            
                        else:
                            youtubelinks.append(multiplelinks)

                    else:
                        print('Not a valid youtube video')

                    if multiplelinks == 'next' and incognito == True:
                        print('Downloading Audio Incognito')
                        for x in youtubelinks:
                            with yt_dlp.YoutubeDL(ydl_optsIVA) as ydl:
                                ydl.download(x)
                    if multiplelinks == 'next' and subtitles == True:
                        print('Downloading Subtitles only')
                        for x in youtubelinks:
                            with yt_dlp.YoutubeDL(ydl_optsVS) as ydl:
                                ydl.download(x)         

                    
                    if multiplelinks == 'next':
                        print('Downloading Audio')
                        for x in youtubelinks:
                            with yt_dlp.YoutubeDL(ydl_optsV) as ydl:
                                ydl.download(x)
                        exit(0)

            if incognito:
                print('Downloading incognito')
                ytlink=input('Insert One Link: ')
                
                with yt_dlp.YoutubeDL(ydl_optsIVA) as ydl:
                    ydl.download(ytlink)
            if subtitles:
                print('Put Link Here')
                subtitles = input('')
                with yt_dlp.YoutubeDL(ydl_optsVS) as ydl:
                    ydl.download(subtitles)
                exit(0) 
                            
            if link:
                while True:
                    ytlink=input('Insert One Link: ')

                    if 'https://www.youtube.com' in ytlink or 'https://youtu.be/' in ytlink or 'http://youtu.be' in ytlink or 'https://youtube.com' in ytlink or 'youtube.com' in ytlink:
                        with yt_dlp.YoutubeDL(ydl_optsV) as ydl:
                            ydl.download([ytlink])
                        break
                    else:
                        print(f'{color.WARNING}Not a Youtube Link{color.END}')
        except KeyboardInterrupt as e:
            print('\nKeyboard interrupt.')
        except FileNotFoundError as e:
            print(e)
###! Anime Downlaoder
@app.command()
def crunchyroll(
    dpath: str = typer.Option(Anime_File_Save, '--path', '-p'),
    multiple: bool = typer.Option(False, '--multiple', '-m', help='Insert Multiple Links to Download'),
    dub: bool = typer.Option(True, '--dub', '-d', help='Download Crunchyroll Dubbed'),
    sub: bool = typer.Option(False, '--sub', '-s', help='Download Crunchyroll Subbed'),
):
    '''Downloads Crunchyroll Links(As Long as you have an account!)'''
    link = True
    animelinks = []
    pathExist = path.exists(dpath)
    if path.exists(VideoArchive):
        pass
    else:
        with open(f'{VideoArchive}', 'w') as f:
            f.close()
        pass
    if pathExist == False:
        print('Path Does not exist')
        exit(0)
    if pathExist:
        print('path Exists, Continuing ')
    if multiple:
        print('Input links')

        while True:
            
            multiplelinks = input('')
            
            if multiple == 'next':
                print('Downloading')
                if dub:
                    print('Downloading Dubbed')
                if sub:
                    print('Downloading Subbed')
            if 'crunchyroll.com' in multiplelinks:
                if multiplelinks in animelinks:
                    print('Already in List')
                            
                else:
                    animelinks.append(multiplelinks)
    if link:
        while True:
            animelink=input('Insert One Link: ')
            
            if 'crunchyroll.com' in animelink:
                if dub:
                    with yt_dlp.YoutubeDL(ydl_optsANIMEDUB) as ydl:
                        ydl.download(animelink)
                if sub:
                    with yt_dlp.YoutubeDL(ydl_optsANIMESUB) as ydl:
                        ydl.download(animelink)
                break
            else:
                print(f'{color.WARNING}Not a CrunchyRoll Link{color.END}')

@app.command()
def version() -> None:
    """Show project Version."""
    # typer.secho(f"project Version: {__version__}", fg=typer.colors.BRIGHT_GREEN)

    console.print(f"project Version: {__version__}", style="bold green")
        

if __name__ == "__main__":
    app()
