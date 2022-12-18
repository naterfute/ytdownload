
#! Figure out how to use yml files dumdum
import os
import sys
#! user most Important
Audio_File_Save = '~/Music/Downloaded'
Video_File_Save = '~/Videos/'
AudioArchive = '~/Music/AudioArchive.txt'
VideoArchive = '~/Videos/VideoArchive.txt'

#* Classes

class MyLogger:
    def debug(self, msg):
        # For compatibility with youtube-dl, both debug and info are passed into debug
        # You can distinguish them by the prefix '[debug] '
        if msg.startswith('[debug] '):
            pass
        else:
            self.info(msg)

    def info(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)
        
#* Functions


def my_hook(d):
    if d['status'] == 'finished':
        print('Done downloading, now post-processing ...')

    if d['status'] == 'downloading':
        print(d['_percent_str'], d['_eta_str'])
        
    
#* Classes
    
#* Multi-Line Variables

ydl_optsA = {
            'format': 'bestaudio/best',
            'writethumbnail': True,
            'writesubtitles': True,
            'subtitle': 'write-sub sub-lang en sub-format json3',
            'outtmpl': f'{Audio_File_Save}/%(playlist)s/%(uploader)s/%(playlist_index)s - %(title)s.%(ext)s',
            'breakonexisting': True,
            'ProgressTemplate': 'progress',
            'writeautosubs': False,
            'ignoreerrors': True,
            'logger': MyLogger(),
            'progress_hooks': [my_hook],
            'noplaylist': True,
            'download_archive': AudioArchive,
            'parsemetadata': "${downloadTimestamp}:%(meta_download_date)s",
            'parsemetadata': "%(release_date>%Y-%m-%d,upload_date>%Y-%m-%d)s:%(meta_publish_date)s",
            'embedmeatdata': True,
            'postprocessors':[
            {'key': 'FFmpegExtractAudio', 'preferredcodec': 'mp3','preferredquality': '320'},
            {'key': 'FFmpegMetadata', 'add_metadata': 'True'},
            {'key': 'EmbedThumbnail','already_have_thumbnail': True,}
            ],
        }            

ydl_optsIAA = {
            'format': 'bestaudio/best',
            'writethumbnail': True,
            'writesubtitles': True,
            'subtitle': 'write-sub sub-lang en sub-format json3',
            'outtmpl': f'{Audio_File_Save}/%(playlist)s/%(uploader)s/%(playlist_index)s - %(title)s.%(ext)s',
            'breakonexisting': True,
            'ProgressTemplate': 'progress',
            'writeautosubs': False,
            'ignoreerrors': True,
            'logger': MyLogger(),
            'progress_hooks': [my_hook],
            'noplaylist': True,
            'parsemetadata': "${downloadTimestamp}:%(meta_download_date)s",
            'parsemetadata': "%(release_date>%Y-%m-%d,upload_date>%Y-%m-%d)s:%(meta_publish_date)s",
            'embedmeatdata': True,
            'postprocessors':[
            {'key': 'FFmpegExtractAudio', 'preferredcodec': 'mp3','preferredquality': '320'},
            {'key': 'FFmpegMetadata', 'add_metadata': 'True'},
            {'key': 'EmbedThumbnail','already_have_thumbnail': True,}
            ],
        }            

ydl_optsV = {'format': 'remux/best',
            'writesubtitles': True,
            'subtitle': '--write-sub --sub-lang en --sub-format json3',         
            'outtmpl': Video_File_Save + '/%(title)s.%(ext)s',
            'breakonexisting': True,
            'quite': True,
            'logger': MyLogger(),
            'progress_hooks': [my_hook],
            'ProgressTemplate': 'progress',
            'consoletitle': True,
            'download_archive': VideoArchive,
            'ignoreerrors': True,
            'postprocessors':[
            {'key': 'FFmpegExtractAudio', 'preferredcodec': 'mp4','preferredquality': '1080'},
            {'key': 'FFmpegMetadata', 'add_metadata': 'True'},
            {'key': 'EmbedThumbnail','already_have_thumbnail': False,}
            ],
            }
ydl_optsIVA = {'format': 'remux/best',
            'writesubtitles': True,
            'subtitle': '--write-sub --sub-lang en --sub-format json3',         
            'outtmpl': Video_File_Save + '/%(title)s.%(ext)s',
            'breakonexisting': True,
            'quite': True,
            'logger': MyLogger(),
            'progress_hooks': [my_hook],
            'ProgressTemplate': 'progress',
            'consoletitle': True,
            'ignoreerrors': True,
            'postprocessors':[
            {'key': 'FFmpegExtractAudio', 'preferredcodec': 'mp4','preferredquality': '1080'},
            {'key': 'FFmpegMetadata', 'add_metadata': 'True'},
            {'key': 'EmbedThumbnail','already_have_thumbnail': False,}
            ],
            }



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
