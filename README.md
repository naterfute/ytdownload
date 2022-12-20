# ytdownload
Terminal Youtube Downloader using YT-DLP

## Setup
    git clone https://github.com/KalebSchmidlkofer/ytdownload.git
    pip install -r requirements.txt
    
### Usage
To View all available downloaders ***Note Only Youtube is supported*** (for now)

    python main.py --help
    
To Download Audio 

    python main.py audio
    
To Download Video
    
    python main.py video
    
To View all Sub Commands of either

    python main.py audio --help
    python main.py video --help

### Crunchroll
To Download from crunchyroll you must get the cookies from your browser.
To do that open up your browser of choice(must be google chrome or firefox)
I prefer Firefox, Log into your crunchroll account then run 

    yt-dlp --cookies-from-browser firefox/chrome

if you used chrome go into your variables.py file and find ***ydl_optsANIME***
and change ./firefox to Whatever Directory your cookies are in.
