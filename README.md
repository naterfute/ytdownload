# ytdownload
Terminal Youtube Downloader using YT-DLP

## Setup
    git clone https://github.com/KalebSchmidlkofer/ytdownload.git
#### Its best practice to create a virtual enviorment
    python -m venv venv
    
    source venv/bin/activate

    pip install -r requirements.txt
    
### Usage
### WIP
In order to use the links you must do :

    python main.py -yt "https://www.youtube.com/watch?v=dQw4w9WgXcQ&" or -yt 'https://www.youtube.com/watch?v=dQw4w9WgXcQ&'

if you dont and instead run this:

    python main.py -yt https://www.youtube.com/watch?v=dQw4w9WgXcQ&

you will get an error like this:

    no matches found: https://www.youtube.com/watch?v=dQw4w9WgXcQ

