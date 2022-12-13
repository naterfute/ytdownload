#!/home/kaleb/coding/python/youtube/downloader/cli/.yttcli/bin/python
import yt_dlp, typer, os.path, sys, json
from ytdl.variables import *
from time import sleep
app = typer.Typer()
AUDIO_FILE_SAVE='~/Music'
VIDEO_FILE_SAVE='~/Videos'

#######! AUDIO DOWNLOADER

@app.command()
def audio(
    # link: bool = typer.Option(True,'--link', "-l", help='Insert One Link to Download'),
    multiple: bool = typer.Option(False, '--multiple', '-m' , help='Insert Multiple Links to Download'),
    path: str = typer.Option(AUDIO_FILE_SAVE, '--path', '-p', help='Temp Download Path'),
    # DEPRECATED!   fetch: str = typer.Option(False, autocompletion=autocomplete, help='Fetch youtube links from extra.fetch and download them'),
    incognito: bool = typer.Option(False, '--incognito', '-i', help='Download files without writing to the Archive file (Still writes to archive file!!)')
          ):
        youtubelinks=[]
        youtubelinksedited=[]
        link = True
        try:
            pathExist = os.path.exists(path)
            
            if pathExist == False:
                print('Path Does not exist')
                sys.exit(0)
            if pathExist:
                print('path Exists, Continuing ')

            if multiple:
                print('Insert links to download')
                print('Put Links Here')
            
                while True:
            
                    multiplelinks=input('')
                   
                    if 'https://www.youtube.com' in multiplelinks or 'https://youtu.be/' in multiplelinks or 'http://youtu.be' in multiplelinks or 'https://youtube.com' in multiplelinks or 'youtube.com' in multiplelinks:
                        # yt = YouTube(f'{multiplelinks}')

                        if multiplelinks in youtubelinks:
                            print('already about to download')
                            
                        else:
                            youtubelinks.append(multiplelinks)

                    else:
                        print('Not a valid youtube video')

                    if multiplelinks == 'next' and incognito == True:
                        print('Downloading Audio Incognito')
                        for x in youtubelinks:
                            with yt_dlp.YoutubeDL(ydl_optsA) as ydl:
                                ydl.download(x)
                    
                    if multiplelinks == 'next':
                        print(f'{youtubelinksedited}')
                        sleep(3)
                        print('Downloading Audio')
                        for x in youtubelinks:
                            with yt_dlp.YoutubeDL(ydl_optsA) as ydl:
                                ydl.download(x)
                        sys.exit(0)

            if incognito:
                print('Downloading incognito')
                ytlink=input('Insert One Link: ')
                
                with yt_dlp.YoutubeDL(ydl_optsIAA) as ydl:
                    ydl.download(ytlink)
                            
            if link:
                while True:
                    ytlink=input('Insert One Link: ')

                    if 'https://www.youtube.com' in ytlink or 'https://youtu.be/' in ytlink:
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
    # link: bool = typer.Option(True,'--link', "-l", help='Insert One Link to Download'),
    multiple: bool = typer.Option(False, '--multiple', '-m' , help='Insert Multiple Links to Download'),
    path: str = typer.Option(AUDIO_FILE_SAVE, '--path', '-p', help='Temp Download Path'),
    # DEPRECATED!   fetch: str = typer.Option(False, autocompletion=autocomplete, help='Fetch youtube links from extra.fetch and download them'),
    incognito: bool = typer.Option(False, '--incognito', '-i', help='Download files without writing to the Archive file')
          ):
        youtubelinks=[]
        youtubelinksedited=[]
        link = True
        try:
            pathExist = os.path.exists(path)
            
            if pathExist == False:
                print('Path Does not exist')
                sys.exit(0)
            if pathExist:
                print('path Exists, Continuing ')

            if multiple:
                print('Insert links to download')
                print('Put Links Here')
            
                while True:
            
                    multiplelinks=input('')
                   
                    if 'https://www.youtube.com' in multiplelinks or 'https://youtu.be/' in multiplelinks or 'http://youtu.be' in multiplelinks or 'https://youtube.com' in multiplelinks or 'youtube.com' in multiplelinks:
                        # yt = YouTube(f'{multiplelinks}')

                        if multiplelinks in youtubelinks:
                            print('already in list')
                            
                        else:
                            youtubelinks.append(multiplelinks)

                    else:
                        print('Not a valid youtube video')

                    if multiplelinks == 'next' and incognito == True:
                        print(youtubelinksedited)
                        sleep(3)
                        print('Downloading Video Incognito')
                        for x in youtubelinks:
                            with yt_dlp.YoutubeDL(ydl_optsIVA) as ydl:
                                ydl.download(x)
                    
                    if multiplelinks == 'next':
                        print(f'{youtubelinksedited}')
                        sleep(3)
                        print('Downloading Video')
                        for x in youtubelinks:
                            with yt_dlp.YoutubeDL(ydl_optsV) as ydl:
                                ydl.download(x)
                        sys.exit(0)

            if incognito:
                print('Downloading incognito')
                ytlink=input('Insert One Link: ')
                
                with yt_dlp.YoutubeDL(ydl_optsIVA) as ydl:
                    ydl.download(ytlink)
                            
            if link:
                while True:
                    ytlink=input('Insert One Link: ')

                    if 'https://www.youtube.com' in ytlink or 'https://youtu.be/' in ytlink:
                        with yt_dlp.YoutubeDL(ydl_optsV) as ydl:
                            ydl.download([ytlink])
                        break
                    else:
                        print(f'{color.WARNING}Not a Youtube Link{color.END}')
        except KeyboardInterrupt as e:
            print('\nKeyboard interrupt.')
        except FileNotFoundError as e:
            print(e) 

if __name__ == "__main__":
    # typer.run(app)
    app()
