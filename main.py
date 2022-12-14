#!/usr/bin/python3.10
import yt_dlp, typer, os.path, sys, json
from ytdl.variables import *
from ytdl.myconf import *
app = typer.Typer(add_completion=False)

def main():
    pass

#######! AUDIO DOWNLOADER

@app.command()
def audio(
    multiple: bool = typer.Option(False, '--multiple', '-m' , help='Insert Multiple Links to Download'),
    dpath: str = typer.Option(Audio_File_Save, '--path', '-p', help='Temp Download Path'),
    incognito: bool = typer.Option(False, '--incognito', '-i', help='Download files without writing to the Archive file')
          ):
        youtubelinks=[]
        link = True
        try:
            pathExist = os.path.exists(dpath)
            
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
                   
                    if allowedlinks in multiplelinks:
                        # yt = YouTube(f'{multiplelinks}')

                        if multiplelinks in youtubelinks:
                            print('Already in List')
                            
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
    multiple: bool = typer.Option(False, '--multiple', '-m' , help='Insert Multiple Links to Download'),
    path: str = typer.Option(Video_File_Save, '--path', '-p', help='Temp Download Path'),
    incognito: bool = typer.Option(False, '--incognito', '-i', help='Download files without writing to the Archive file')
          ):
        youtubelinks=[]
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
                        print('Downloading Video Incognito')
                        for x in youtubelinks:
                            with yt_dlp.YoutubeDL(ydl_optsIVA) as ydl:
                                ydl.download(x)
                    
                    if multiplelinks == 'next':
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
