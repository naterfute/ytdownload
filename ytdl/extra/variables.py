
import os

#! user most Important
AUDIO_PATH='~/Music/'
VIDEO_PATH='~/Videos/'

# Import Single line variable
USERNAME = os.getenv('USERNAME')
PASSWORD = os.getenv('PASSWORD')
# ARCHIVE = os.getenv('ARCHIVE')
# Single-Line Variables

AUDIO_PATH='~/Music/'
VIDEO_PATH='~/Videos/'
ARCHIVE = '~/ARCHIVE/ARCHIVE.txt'
errormessage='wow.. I gave you clear instructions'
FILE='extra/tempfiles/list.txt'
# Multi-Line Variables

ydl_optsA = {
            'format': 'bestaudio/best',
            'writethumbnail': True,
            'writesubtitles': True,
            'subtitle': '--write-sub --sub-lang en --sub-format json3',
            'outtmpl': f'{AUDIO_PATH}' + '/%(title)s.%(ext)s',
            'breakonexisting': True,
            'consoletitle': True,
            'nowarn': True,
            'quite': True,
            'ProgressTemplate': 'console-title ',
            'nowriteautosubs': True,
            'ignoreerrors': True,
            'postprocessors':[
            {'key': 'FFmpegExtractAudio', 'preferredcodec': 'mp3','preferredquality': '320'},
            {'key': 'FFmpegMetadata', 'add_metadata': 'True'},
            {'key': 'EmbedThumbnail','already_have_thumbnail': True,}
            ],
        }            

ydl_optsV = {'format': 'remux/best',
            'ignoreerrors': True,
            'writesubtitles': True,
            'subtitle': '--write-sub --sub-lang en --sub-format json3',         
            'outtmpl': VIDEO_PATH + '/%(title)s.%(ext)s',
            'breakonexisting': True,
            'nowarn': True,
            'quite': True,
            'ProgressTemplate': 'console-title ',
            'consoletitle': True,
            'nowriteautosubs': True,
            'username': USERNAME,
            'password': PASSWORD,
            'ignoreerrors': True,
            'postprocessors':[
            {'key': 'FFmpegExtractAudio', 'preferredcodec': 'mp4','preferredquality': '1080'},
            {'key': 'FFmpegMetadata', 'add_metadata': 'True'},
            {'key': 'EmbedThumbnail','already_have_thumbnail': False,}
            ],
            }

#! To lazy to sort

s18= ' ' * 18
s20= ' ' * 20
class color:
   HEADER = '\033[95m' 
   PURPLE = '\033[95m'
   DARKCYAN = '\033[36m'
   OKBLUE = '\033[94m'
   OKCYAN = '\033[96m'
   OKGREEN = '\033[92m'
   WARNING = '\033[93m'
   FAIL = '\033[91m'
   CRUNCHYROLL = '#FDAD0E'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   BLINK = '\033[5m'
   END = '\033[0m'

